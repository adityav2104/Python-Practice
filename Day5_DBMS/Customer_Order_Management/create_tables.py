import sqlite3

conn = sqlite3.connect("orders.db")
cursor = conn.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS Customers 
               ( customer_id INTEGER PRIMARY KEY AUTOINCREMENT, 
               name TEXT NOT NULL, email TEXT UNIQUE NOT NULL)
               """)

cursor.execute("""
               CREATE TABLE IF NOT EXISTS Orders 
               ( order_id INTEGER PRIMARY KEY AUTOINCREMENT, customer_id INTEGER, 
               product TEXT NOT NULL, quantity INTEGER NOT NULL, order_date TEXT,  
               FOREIGN KEY (customer_id) REFERENCES Customers(customer_id))
               """)


conn.commit()
conn.close()
