import csv
import sqlite3

# 1. Connect to SQLite database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# 2. Create the table
cursor.execute(
    "CREATE TABLE IF NOT EXISTS users (name TEXT, email TEXT)"
)

# 3. Read the CSV file and insert rows into the database
with open("C:\\Users\\Shruti\\Documents\\GitHub\\ProblemStatementSolutions\\ProblemStatement1\\Task3\\Users.csv", mode="r") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row (name, email)

    for row in csv_reader:
        name = row[0]
        email = row[1]
        cursor.execute(
            "INSERT INTO users VALUES (?, ?)",
            (name, email),
        )

# 4. Save changes and close connection
conn.commit()

# 5. Read and display data from the database 
cursor.execute("SELECT * FROM users")
for user in cursor.fetchall():
    print("Name:", user[0], "| Email:", user[1])

conn.close()