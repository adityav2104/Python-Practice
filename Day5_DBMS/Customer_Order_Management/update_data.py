import sqlite3

conn = sqlite3.connect("orders.db")
cursor = conn.cursor()

# Update customer name
cursor.execute ("UPDATE Customers SET name = 'Raghav Kumar' WHERE customer_id = 2")

# Update order quantity
cursor.execute("UPDATE Orders SET quantity = 5 WHERE order_id = 2")

conn.commit()
conn.close()

print(" Updated successfully!")