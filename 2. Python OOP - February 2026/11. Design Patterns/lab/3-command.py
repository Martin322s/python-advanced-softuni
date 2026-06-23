import sys

class Window:
    def exit(self):
        sys.exit(0)

class Document:
    def __init__(self, filename):
        self.filename = filename
        self.contents = "This file cannot be modified"

    def save(self):
        with open(self.filename, "w") as file:
            file.write(self.contents)

class ToolbarDocument:
    def __init__(self, name, iconname):
        self.name = name
        self.iconname = iconname
        self.command = None

    def click(self):
        if self.command:
            self.command.execute()

class MenuItem:
    def __init__(self, menu_name, item_name):
        self.menu = menu_name
        self.item = item_name
        self.command = None

    def click(self):
        if self.command:
            self.command.execute()

class KeyboardShortcut:
    def __init__(self, key, modifier):
        self.key = key
        self.modifier = modifier
        self.command = None

    def keypress(self):
        if self.command:
            self.command.execute()

class SaveCommand:
    def __init__(self, document):
        self.document = document

    def execute(self):
        self.document.save()


class ExitCommand:
    def __init__(self, window):
        self.window = window

    def execute(self):
        self.window.exit()

if __name__ == "__main__":
    doc = Document("example.txt")
    win = Window()

    save_cmd = SaveCommand(doc)
    exit_cmd = ExitCommand(win)

    toolbar = ToolbarDocument("Save", "save_icon.png")
    menu_item = MenuItem("File", "Save")
    shortcut = KeyboardShortcut("S", "Ctrl")

    toolbar.command = save_cmd
    menu_item.command = save_cmd
    shortcut.command = save_cmd

    toolbar.click()
    menu_item.click()
    shortcut.keypress()