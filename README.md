# 📚 Library Book Finder

![Library Banner](https://images.unsplash.com/photo-1512820790803-83ca734da794?auto=format&fit=crop&w=800&q=80)

## Project Description
The **Library Book Finder** is a web-based project built using **Python** and **Streamlit**.  
It allows users to search for books in a library efficiently using the **Binary Search algorithm**.  
The project features a visually appealing web interface, interactive search inputs, and instant feedback for users.

---

## Algorithm Used

### Binary Search
Binary Search is an efficient algorithm to find an element in a **sorted list**.  
The list is repeatedly divided in half, comparing the middle element with the target value.  
- If the middle element is the target, the search ends.  
- Otherwise, the search continues in the left or right half until the target is found or the list ends.

**Pseudocode:**
```text
function binary_search(array, target):
    left = 0
    right = length(array) - 1

    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        else if array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
Project Interface
Main Web Page

Book Found

Book Not Found

How to Run Locally
Install Python 3.8+

Install Streamlit:

bash
Copy code
pip install streamlit
Navigate to the project folder:

bash
Copy code
cd "C:\Users\gogua\OneDrive\Desktop\DAA Project"
Run the app:

bash
Copy code
streamlit run main.py
The app will open automatically in your default browser.

Features
Interactive web app using Python + Streamlit

Displays sorted library book list

Users can type or select a book from dropdown

Binary Search implemented from scratch

Visual feedback with success and error images

Beginner-friendly and easy to understand

Complexity Analysis
Operation	Time Complexity	Space Complexity
Binary Search (Best Case)	O(1)	O(1)
Binary Search (Average/Worst Case)	O(log N)	O(1)

Technologies Used
Python 3

Streamlit

Conclusion
This project demonstrates the practical use of algorithms in solving real-world problems.
It combines algorithmic thinking with a web-based interactive interface, making it easy for users to search for books efficiently.

yaml
Copy code

---

This is a **single Markdown file** (`README.md`) that you can push to GitHub.  

If you want, I can also **add a section for “Screenshots of your actual app”** so it looks even more professional for your submission.  

Do you want me to do that?