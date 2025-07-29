import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()
cursor.execute("""INSERT INTO students (id, name, age) VALUES (1,"Aditya", 23)""")
cursor.execute("""INSERT INTO students (id, name, age) VALUES (2,"Raghav", 22)""")
cursor.execute("""INSERT INTO students (id, name, age) VALUES (3,"Jahnvi", 23)""")
cursor.execute("""INSERT INTO courses (id, branch_name, course_name) VALUES (1,"CSE", "DBMS")""")
cursor.execute("""INSERT INTO courses (id, branch_name, course_name) VALUES (2,"CSE", "Java")""")
cursor.execute("""INSERT INTO courses (id, branch_name, course_name) VALUES (3,"CSE", "QA")""")
conn.commit()
conn.close()
print("Data is being inserted!")