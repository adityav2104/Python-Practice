import sqlite3

conn = sqlite3.connect("students.db")

cursor = conn.cursor()


cursor.execute("UPDATE students SET age = 24 WHERE name = 'Jahnvi'")

conn.commit()

conn.close()

print("Data Updated Succesfully!")