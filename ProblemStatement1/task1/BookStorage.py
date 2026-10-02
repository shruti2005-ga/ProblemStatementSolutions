import sqlite3
import requests

# Step 1: Fetch real book data from a live internet API
url = "https://openlibrary.org/subjects/fiction.json?limit=5"
response = requests.get(url)
data = response.json()
books = data["works"]

# Step 2: Connect to SQLite database
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Step 3: Create table for title, author, and year
cursor.execute(
    "CREATE TABLE IF NOT EXISTS books (title TEXT, author TEXT, year INT)"
)

# Step 4: Extract fields and insert into database
for book in books:
    title = book["title"]#gets title
    author = book["authors"][0]["name"]  # Gets the author's name
    year = book["first_publish_year"]  # Gets the publication year

    cursor.execute(
        "INSERT INTO books VALUES (?, ?, ?)",
        (title, author, year),
    )

conn.commit()

# Step 5: Read and print data from SQLite
cursor.execute("SELECT * FROM books")
records = cursor.fetchall()

for row in records:
    print("Title:", row[0])
    print("Author:", row[1])
    print("Year:", row[2])
    print("-" * 30)

conn.close()
