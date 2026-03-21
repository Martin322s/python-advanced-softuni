def classify_books(*args, **kwargs):
    title_to_isbn = {title: isbn for isbn, title in kwargs.items()}

    fiction_books = {}
    non_fiction_books = {}

    for genre, title in args:
        isbn = title_to_isbn[title]
        if genre == "fiction":
            fiction_books[isbn] = title
        else:
            non_fiction_books[isbn] = title

    fiction_sorted = sorted(fiction_books.items(), key=lambda x: x[0])
    non_fiction_sorted = sorted(non_fiction_books.items(), key=lambda x: x[0], reverse=True)

    lines = []

    if fiction_sorted:
        lines.append("Fiction Books:")
        for isbn, title in fiction_sorted:
            lines.append(f"~~~{isbn}#{title}")

    if non_fiction_sorted:
        lines.append("Non-Fiction Books:")
        for isbn, title in non_fiction_sorted:
            lines.append(f"***{isbn}#{title}")

    return "\n".join(lines)