from __future__ import annotations

import csv
import io
import json
import os
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Dict, Optional, Tuple

from flask import Flask, request, render_template_string

@dataclass(frozen=True)
class FileInfo:
    filename: str
    content_type: str
    size_bytes: int


@dataclass(frozen=True)
class ImportResult:
    ok: bool
    message: str
    file_info: Optional[FileInfo] = None
    details: Optional[Dict[str, Any]] = None

class ParserStrategy(ABC):
    """Strategy interface for parsing/validating uploaded files."""

    @abstractmethod
    def supports(self, filename: str, content_type: str) -> bool:
        ...

    @abstractmethod
    def parse(self, raw_bytes: bytes) -> Dict[str, Any]:
        """
        Parse and validate file content.
        Return details dict if OK, raise ValueError if invalid.
        """
        ...


class CsvParser(ParserStrategy):
    ALLOWED_CT = {"text/csv", "application/csv", "application/vnd.ms-excel"}

    def supports(self, filename: str, content_type: str) -> bool:
        return filename.lower().endswith(".csv") and (content_type in self.ALLOWED_CT or content_type.startswith("text/"))

    def parse(self, raw_bytes: bytes) -> Dict[str, Any]:
        try:
            text = raw_bytes.decode("utf-8-sig")
        except UnicodeDecodeError as e:
            raise ValueError("CSV must be UTF-8 encoded") from e

        stream = io.StringIO(text)
        reader = csv.reader(stream)

        rows = list(reader)
        if not rows:
            raise ValueError("CSV is empty")

        header = rows[0]
        if not header or all(h.strip() == "" for h in header):
            raise ValueError("CSV has no header")

        if len(header) < 1:
            raise ValueError("CSV header must have at least 1 column")

        data_rows = rows[1:]
        if len(data_rows) < 1:
            raise ValueError("CSV must have at least 1 data row")

        bad = [i for i, r in enumerate(data_rows, start=2) if len(r) != len(header)]
        if bad:
            raise ValueError(f"CSV row length mismatch at lines: {bad[:5]}{'...' if len(bad) > 5 else ''}")

        return {
            "type": "csv",
            "rows": len(data_rows),
            "columns": len(header),
            "header": header,
            "preview": data_rows[:3],
        }

class JsonParser(ParserStrategy):
    ALLOWED_CT = {"application/json", "text/json"}

    def supports(self, filename: str, content_type: str) -> bool:
        return filename.lower().endswith(".json") and (content_type in self.ALLOWED_CT or content_type in {"application/octet-stream", ""})

    def parse(self, raw_bytes: bytes) -> Dict[str, Any]:
        try:
            text = raw_bytes.decode("utf-8")
        except UnicodeDecodeError as e:
            raise ValueError("JSON must be UTF-8 encoded") from e

        try:
            obj = json.loads(text)
        except json.JSONDecodeError as e:
            raise ValueError("Invalid JSON") from e

        if not isinstance(obj, (dict, list)):
            raise ValueError("JSON must be an object or array")

        return {
            "type": "json",
            "root_type": "object" if isinstance(obj, dict) else "array",
            "keys_preview": list(obj.keys())[:10] if isinstance(obj, dict) else None,
            "items_preview": obj[:3] if isinstance(obj, list) else None,
        }

class ParserFactory:
    def __init__(self):
        self._strategies = [CsvParser(), JsonParser()]

    def get_parser(self, filename: str, content_type: str) -> Optional[ParserStrategy]:
        for s in self._strategies:
            if s.supports(filename, content_type):
                return s
        return None

class ImportWorkflow(ABC):
    """
    Template Method: fixed algorithm skeleton:
    1) validate request + file
    2) select parser
    3) parse content
    4) log info
    5) return result
    """

    def __init__(self, parser_factory: ParserFactory):
        self.parser_factory = parser_factory

    def run(self, file_storage) -> ImportResult:
        try:
            file_info = self._extract_info(file_storage)
            parser = self._select_parser(file_info)
            details = self._parse(parser, file_storage)
            self._log_success(file_info, details)
            return ImportResult(ok=True, message="File uploaded successfully", file_info=file_info, details=details)
        except ValueError:
            return ImportResult(ok=False, message="Invalid content type for import")

    def _extract_info(self, file_storage) -> FileInfo:
        if file_storage is None or file_storage.filename is None or file_storage.filename.strip() == "":
            raise ValueError("No file")

        filename = os.path.basename(file_storage.filename)
        content_type = (file_storage.content_type or "").strip()

        raw = file_storage.read()
        size = len(raw)
        file_storage.stream.seek(0)

        if not (filename.lower().endswith(".csv") or filename.lower().endswith(".json")):
            raise ValueError("Unsupported extension")

        return FileInfo(filename=filename, content_type=content_type, size_bytes=size)

    def _select_parser(self, file_info: FileInfo) -> ParserStrategy:
        parser = self.parser_factory.get_parser(file_info.filename, file_info.content_type)
        if not parser:
            raise ValueError("Unsupported content type")
        return parser

    def _parse(self, parser: ParserStrategy, file_storage) -> Dict[str, Any]:
        raw_bytes = file_storage.read()
        return parser.parse(raw_bytes)

    @abstractmethod
    def _log_success(self, file_info: FileInfo, details: Dict[str, Any]) -> None:
        ...

class ConsoleLoggingImportWorkflow(ImportWorkflow):
    def _log_success(self, file_info: FileInfo, details: Dict[str, Any]) -> None:
        print("=== Upload OK ===")
        print(f"Filename: {file_info.filename}")
        print(f"Content-Type: {file_info.content_type}")
        print(f"Size: {file_info.size_bytes} bytes")
        print("Parsed details:", details)
        print("=================")

class UploadService:
    def __init__(self, workflow: ImportWorkflow):
        self.workflow = workflow

    def handle_upload(self, file_storage) -> ImportResult:
        return self.workflow.run(file_storage)
    
app = Flask(__name__)

HTML_FORM = """
<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Upload CSV/JSON</title>
    <style>
      body { font-family: Arial, sans-serif; margin: 40px; }
      .card { max-width: 520px; padding: 16px; border: 1px solid #ddd; border-radius: 10px; }
      .msg { margin-top: 14px; padding: 10px; border-radius: 8px; }
      .ok { background: #e8fff0; border: 1px solid #b7f0c6; }
      .bad { background: #fff0f0; border: 1px solid #f2b5b5; }
      label { display:block; margin: 10px 0 6px; }
      input[type=file] { width: 100%; }
      button { margin-top: 12px; padding: 10px 14px; border-radius: 8px; border: 0; cursor: pointer; }
    </style>
  </head>
  <body>
    <div class="card">
      <h2>Upload a CSV or JSON file</h2>
      <form action="/upload" method="POST" enctype="multipart/form-data">
        <label for="file">Choose file (.csv or .json)</label>
        <input id="file" name="file" type="file" accept=".csv,.json" required />
        <button type="submit">Upload</button>
      </form>

      {% if message %}
        <div class="msg {{ 'ok' if ok else 'bad' }}">
          {{ message }}
        </div>
      {% endif %}
    </div>
  </body>
</html>
"""

factory = ParserFactory()
workflow = ConsoleLoggingImportWorkflow(factory)
service = UploadService(workflow)


@app.get("/")
def index():
    return render_template_string(HTML_FORM, message=None, ok=None)


@app.post("/upload")
def upload():
    file = request.files.get("file")
    result = service.handle_upload(file)

    return render_template_string(
        HTML_FORM,
        message=result.message,
        ok=result.ok
    )


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)