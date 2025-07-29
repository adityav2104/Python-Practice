import sqlite3

conn = sqlite3.connect("students.db")

cursor = conn.cursor()

#cursor.execute("DROP TABLE IF EXISTS students")

#cursor.execute("""CREATE TABLE IF NOT EXISTS students ( id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, age INTEGER)""")

#cursor.execute("""CREATE TABLE courses ( id INTEGER PRIMARY KEY AUTOINCREMENT, branch_name TEXT, course_name TEXT)""")

print("Students table :")
cursor.execute("PRAGMA table_info(students)")
print(cursor.fetchall())

print("Courses table :")
cursor.execute("PRAGMA table_info(courses)")
print(cursor.fetchall())

conn.commit()

conn.close()