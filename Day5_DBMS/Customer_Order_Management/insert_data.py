import sqlite3

conn = sqlite3.connect("orders.db")
cursor = conn.cursor()

cursor.execute("""
    INSERT INTO customers (name, email)
    VALUES
    ('Aditya Verma', 'adityaverma7799@gmail.com'),
    ('Raghav Patidar', 'ravi@gmail.com'),
    ('Priya Singh', 'priya@gmail.com')
""")

cursor.execute("""
    INSERT INTO orders (customer_id, product, quantity)
    VALUES
    (1, 'Laptop', 55000),
    (2, 'Smartphone', 20000),
    (1, 'Headphones', 2500)
""")

conn.commit()
conn.close()

print("Data inserted successfully!")