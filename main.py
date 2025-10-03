"""
Project: Library Book Finder using Binary Search
Author: Your Name
Date: 2025-10-04
"""

class BookFinder:
    def __init__(self, books):
        # books should already be sorted
        self.books = books

    def binary_search(self, target):
        left, right = 0, len(self.books) - 1

        while left <= right:
            mid = (left + right) // 2
            if self.books[mid] == target:
                return mid  # Found at position mid
            elif self.books[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1  # Not found


if __name__ == "__main__":
    # Example dataset (sorted list of book names)
    library_books = [
        "Algorithms Unlocked",
        "Clean Code",
        "Data Structures in Python",
        "Design Patterns",
        "Introduction to Algorithms",
        "Operating Systems Concepts",
        "Python Crash Course",
        "The C Programming Language"
    ]

    print("📚 Library Book Finder 📚")
    print("Available Books (sorted):")
    for i, book in enumerate(library_books, 1):
        print(f"{i}. {book}")

    search_book = input("\nEnter the book name you want to search: ")

    finder = BookFinder(library_books)
    result = finder.binary_search(search_book)

    if result != -1:
        print(f"\n✅ '{search_book}' found at position {result + 1} in the library.")
    else:
        print(f"\n❌ '{search_book}' not found in the library.")
