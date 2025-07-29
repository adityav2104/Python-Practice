import sqlite3

conn = sqlite3.connect("students.db")

cursor = conn.cursor()

print("STUDENT TABLE DATA: ")
cursor.execute("SELECT * FROM students")

rows = cursor.fetchall()
for row in rows:
    print(row)

print("\n\nCOURSES TABLE DATA: ")
cursor.execute("SELECT * FROM courses")

rows = cursor.fetchall()
for row in rows:
    print(row)


conn.close()