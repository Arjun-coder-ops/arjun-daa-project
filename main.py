# app.py
import streamlit as st

# --------------------------
# Binary Search Implementation
# --------------------------
class BookFinder:
    def __init__(self, books):
        self.books = books

    def binary_search(self, target):
        left, right = 0, len(self.books) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.books[mid] == target:
                return mid
            elif self.books[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

# --------------------------
# Library Collection
# --------------------------
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

library_books.sort()

# --------------------------
# Streamlit Web Interface
# --------------------------
st.set_page_config(page_title="Library Book Finder", page_icon="📚")
st.title("📚 Library Book Finder")

# Banner Image (online)
st.image(
    "https://images.unsplash.com/photo-1512820790803-83ca734da794?auto=format&fit=crop&w=800&q=80",
    caption="Welcome to the Library!",
    use_container_width=True
)

st.write("Search for your book from the library collection below:")

# Show all available books
st.subheader("Available Books (Sorted Alphabetically):")
for i, book in enumerate(library_books, start=1):
    st.write(f"{i}. {book}")

# --------------------------
# User Inputs
# --------------------------
st.markdown("### 🔍 Type the book name:")
typed_book = st.text_input("Or type the book name here:")

st.markdown("### 📚 Or select a book from the list:")
selected_book = st.selectbox("Choose a book:", [""] + library_books)

search_book = typed_book.strip() if typed_book.strip() != "" else selected_book

# --------------------------
# Search Button
# --------------------------
if st.button("Search"):
    if search_book == "":
        st.warning("⚠️ Please type or select a book to search.")
    else:
        finder = BookFinder(library_books)
        result = finder.binary_search(search_book)
        
        if result != -1:
            st.success(f"✅ '{search_book}' found at position {result + 1} in the library!")
            # Success Image
            st.image(
                "https://images.unsplash.com/photo-1581090700227-9fa041ef2d12?auto=format&fit=crop&w=400&q=80",
                width=250
            )
        else:
            st.error(f"❌ '{search_book}' not found in the library.")
            # Not Found Image
            st.image(
                "https://images.unsplash.com/photo-1601582582196-18c7c6bda5ea?auto=format&fit=crop&w=400&q=80",
                width=250
            )
