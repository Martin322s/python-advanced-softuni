from abc import ABC, abstractmethod

class Borrowable(ABC):
    @abstractmethod
    def borrow(self, user_id: str) -> None:
        pass

class Readable(ABC):
    @abstractmethod
    def read(self) -> None:
        pass

class Listenable(ABC):
    @abstractmethod
    def listen(self) -> None:
        pass

class BorrowableMixin(Borrowable):
    def __init__(self):
        self._borrowed = False

    def borrow(self, user_id: str) -> None:
        self._borrowed = True
        print(f"{self.__class__.__name__} borrowed by user {user_id}.")

    def _ensure_borrowed(self) -> None:
        if not self._borrowed:
            raise RuntimeError(f"{self.__class__.__name__} must be borrowed first.")

class Book(BorrowableMixin, Readable):
    def __init__(self):
        super().__init__()
        self.progress = 0

    def read(self) -> None:
        self._ensure_borrowed()
        self.progress += 10
        print(f"Reading the book. Progress: {self.progress}%")

class EBook(BorrowableMixin, Readable):
    def __init__(self):
        super().__init__()
        self.drm_applied = False
        self.progress = 0

    def borrow(self, user_id: str) -> None:
        self.drm_applied = True
        super().borrow(user_id)
        print("DRM applied.")

    def read(self) -> None:
        self._ensure_borrowed()
        self.progress += 20
        print(f"Reading the eBook. Progress: {self.progress}%")

class Audiobook(BorrowableMixin, Listenable):
    def __init__(self):
        super().__init__()
        self.progress = 0

    def listen(self) -> None:
        self._ensure_borrowed()
        self.progress += 15
        print(f"Listening to the audiobook. Progress: {self.progress}%")

book = Book()
book.borrow("user123")
book.read()

try:
    book.listen()
except AttributeError as e:
    print(e)

ebook = EBook()
ebook.borrow("user456")
ebook.read()

try:
    ebook.listen()
except AttributeError as e:
    print(e)

audiobook = Audiobook()
audiobook.borrow("user789")
audiobook.listen()

try:
    audiobook.read()
except AttributeError as e:
    print(e)