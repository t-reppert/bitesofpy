from datetime import datetime


def ontrack_reading(books_goal: int, books_read: int,
                    day_of_year: int = None) -> bool:
    if not day_of_year:
        day_of_year = datetime.now().timetuple().tm_yday
    remaining_days = 365 - day_of_year
    book_read_rate = books_read / day_of_year
    remaining_books = books_goal-books_read
    if (remaining_days * book_read_rate) >= remaining_books:
        return True
    elif (remaining_days * book_read_rate) < remaining_books:
        return False
    return False