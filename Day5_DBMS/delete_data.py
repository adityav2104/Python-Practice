import sqlite3

conn = sqlite3.connect("students.db")

cursor = conn.cursor()

cursor.execute("DELETE FROM students WHERE name = 'Jahnvi'")

conn.commit()
conn.close()

print("Data Deleted successfully")