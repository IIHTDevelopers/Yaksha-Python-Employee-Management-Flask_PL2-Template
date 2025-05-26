# setup_db.py
import sqlite3

conn = sqlite3.connect("employees.db")
cursor = conn.cursor()

# Drop the old tables if they exist (optional)
cursor.execute("DROP TABLE IF EXISTS employees")
cursor.execute("DROP TABLE IF EXISTS users")

# Create users table
cursor.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
""")

# Create employees table
cursor.execute("""
CREATE TABLE employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    department TEXT,
    salary TEXT,
    address TEXT
)
""")

# Add 5 sample employees (required by tests)
sample_data = [
    ("Peter Smith", 35, "Sales", "50000", "Main road, London"),
    ("Alice Johnson", 29, "Engineering", "75000", "123 Elm St, New York, NY"),
    ("Catherine Lee", 41, "Finance", "85000", "789 Pine Rd, Chicago, IL"),
    ("Raj Patel", 38, "Marketing", "62000", "67 Queen St, Toronto"),
    ("Sara Ahmed", 30, "HR", "56000", "44 King Ave, Dubai")
]

cursor.executemany("INSERT INTO employees (name, age, department, salary, address) VALUES (?, ?, ?, ?, ?)", sample_data)

# Add specific test data that tests are looking for
test_employees = [
    ("Jhon", 30, "IT", "56000", "24 King Ave, Dubai"),
    ("Raj Patel", 58, "Marketing", "62000", "67 Queen St, Toronto"),
    ("Alice Watson", 35, "Engineering", "72000", "55 Sunset Blvd, LA")
]

cursor.executemany("INSERT INTO employees (name, age, department, salary, address) VALUES (?, ?, ?, ?, ?)", test_employees)

conn.commit()
conn.close()

print("Database initialized with sample data and users table.")
