import sqlite3

conn = sqlite3.connect("orders.db")
cursor = conn.cursor()

cursor.execute("""
    SELECT c.customer_id, c.name, o.product, o.quantity, o.order_date
    FROM Customers c
    JOIN Orders o ON c.customer_id = o.customer_id
""")

results = cursor.fetchall()

print("Customer Orders:\n")
for row in results:
    print(f"Customer ID: {row[0]}, Name: {row[1]}, Product: {row[2]}, Qty: {row[3]}, Date: {row[4]}")

conn.close()