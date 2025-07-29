import sqlite3

conn = sqlite3.connect("orders.db")
cursor = conn.cursor()

try:
    conn.execute("BEGIN")

    #Insert a new customer 
    cursor.execute("""
        INSERT INTO Customers (name, email)
        VALUES ('Kunal Sharma', 'adityaverma7799@gmail.com')
    """)

    #Insert order for that customer (assuming customer_id = 4)
    cursor.execute("""
        INSERT INTO Orders (customer_id, product, quantity)
        VALUES (4, 'Tablet', 1)
    """)

    conn.commit()
    print("Transaction completed successfully!")

except Exception as e:
    conn.rollback()
    print("Transaction failed:", e)

finally:
    conn.close()