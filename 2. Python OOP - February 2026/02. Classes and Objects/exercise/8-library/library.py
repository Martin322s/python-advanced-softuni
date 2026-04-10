from project.user import User

class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        for _, books_dict in self.rented_books.items():
            if book_name in books_dict:
                days_left = books_dict[book_name]
                return f'The book "{book_name}" is already rented and will be available in {days_left} days!'

        if author in self.books_available and book_name in self.books_available[author]:
            self.books_available[author].remove(book_name)
            user.books.append(book_name)

            if user.username not in self.rented_books:
                self.rented_books[user.username] = {}
            self.rented_books[user.username][book_name] = days_to_return

            return f"{book_name} successfully rented for the next {days_to_return} days!"

        return f'The book "{book_name}" is not available in the library!'

    def return_book(self, author: str, book_name: str, user: User):
        if book_name not in user.books:
            return f"{user.username} doesn't have this book in his/her records!"

        user.books.remove(book_name)

        if author not in self.books_available:
            self.books_available[author] = []
        self.books_available[author].append(book_name)

        if user.username not in self.rented_books:
            self.rented_books[user.username] = {}

        if book_name in self.rented_books[user.username]:
            del self.rented_books[user.username][book_name]