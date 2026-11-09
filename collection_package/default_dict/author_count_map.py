"""
create a function for author mapping

"""
from collections import defaultdict


class CookBook:
    """cookbook class author"""

    def __init__(self, author: str, book_name: str):
        self.author = author
        self.book_name = book_name

    def __repr__(self):
        return f"CookBook(author='{self.author}')"

def create_author_count_mapping(cookbook: list) -> dict:
    """ author count map"""
    counter = defaultdict(lambda: 0)
    for book in cookbook:
        counter[book.author] += 1
    return dict(counter)


if __name__ == "__main__":
    cookbooks = [
        CookBook("John"),
        CookBook("Mary"),
        CookBook("John"),
        CookBook("Alice"),
        CookBook("Mary"),
    ]
    author_counts = create_author_count_mapping(cookbooks)
    print(author_counts)
