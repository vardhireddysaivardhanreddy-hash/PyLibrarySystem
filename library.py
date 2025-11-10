import mysql.connector
import os
from datetime import date

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="library_user",
    password="Password@123",
    database="library"
)

cur = conn.cursor()


def add_book():
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    cur.execute("INSERT INTO books (title, author) VALUES (%s, %s)", (title, author))
    conn.commit()
    print("✅ Book added successfully!\n")

def view_books():
    cur.execute("SELECT * FROM books")
    books = cur.fetchall()
    print("\n📚 Available Books:")
    for book in books:
        status = "Available" if book[3] else "Issued"
        print(f"ID: {book[0]} | Title: {book[1]} | Author: {book[2]} | Status: {status}")
    print()

def issue_book():
    book_id = int(input("Enter Book ID to issue: "))
    student_name = input("Enter Student Name: ")

    # Check availability
    cur.execute("SELECT available FROM books WHERE book_id = %s", (book_id,))
    result = cur.fetchone()
    if not result:
        print("❌ Book not found!\n")
        return
    if not result[0]:
        print("⚠️ Book already issued!\n")
        return

    cur.execute("INSERT INTO issued_books (book_id, student_name, issue_date) VALUES (%s, %s, %s)", (book_id, student_name, date.today()))
    cur.execute("UPDATE books SET available = FALSE WHERE book_id = %s", (book_id,))
    conn.commit()
    print("✅ Book issued successfully!\n")

def return_book():
    book_id = int(input("Enter Book ID to return: "))
    cur.execute("SELECT * FROM issued_books WHERE book_id = %s AND return_date IS NULL", (book_id,))
    issue = cur.fetchone()
    if not issue:
        print("❌ This book is not currently issued.\n")
        return

    cur.execute("UPDATE issued_books SET return_date = %s WHERE book_id = %s AND return_date IS NULL", (date.today(), book_id))
    cur.execute("UPDATE books SET available = TRUE WHERE book_id = %s", (book_id,))
    conn.commit()
    print("✅ Book returned successfully!\n")

def delete_book():
    book_id = int(input("Enter Book ID to delete: "))
    # First, delete issued records for this book
    cur.execute("DELETE FROM issued_books WHERE book_id = %s", (book_id,))
    # Then, delete the book itself
    cur.execute("DELETE FROM books WHERE book_id = %s", (book_id,))
    conn.commit()
    print("✅ Book deleted successfully!\n")

def view_issued_books():
    cur.execute("""
        SELECT i.issue_id, b.title, i.student_name, i.issue_date, i.return_date
        FROM issued_books i
        JOIN books b ON i.book_id = b.book_id
    """)
    records = cur.fetchall()
    print("\n📖 Issued Books:")
    for r in records:
        print(f"Issue ID: {r[0]} | Title: {r[1]} | Student: {r[2]} | Issued: {r[3]} | Returned: {r[4]}")
    print()

def main():
    while True:
        print("========= Library Management System =========")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Delete Book")
        print("6. View Issued Books")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            issue_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            delete_book()
        elif choice == "6":
            view_issued_books()
        elif choice == "7":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
