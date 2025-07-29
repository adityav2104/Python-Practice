import sqlite3

conn = sqlite3.connect('orders.db')
cursor = conn.cursor()

# View all customers
cursor.execute("SELECT * FROM Customers")
customers = cursor.fetchall()

print("Customers:")
for customer in customers:
    print(customer)

cursor.execute("SELECT * FROM Orders")
orders = cursor.fetchall()
print("\n\nOrders Table:")
for order in orders:
    print(order)


conn.close()