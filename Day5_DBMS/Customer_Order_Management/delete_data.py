import sqlite3

conn = sqlite3.connect("orders.db")
cursor = conn.cursor()

# Delete a customer by ID
cursor.execute("DELETE FROM Customers WHERE customer_id = 3")

# Delete an order by ID
cursor.execute("DELETE FROM Orders WHERE order_id = 2")

conn.commit()
conn.close()

print(" Deleted successfully!")