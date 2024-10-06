import sqlite3
from datetime import datetime

# Database setup
def create_connection():
    conn = None
    try:
        conn = sqlite3.connect("inventory.db")
        return conn
    except sqlite3.Error as e:
        print(f"Error: {e}")
    return conn

# Create table
def create_table(conn):
    try:
        sql_create_products_table = """
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL,
            restock_date TEXT NOT NULL
        );
        """
        cursor = conn.cursor()
        cursor.execute(sql_create_products_table)
    except sqlite3.Error as e:
        print(f"Error: {e}")

# CRUD Operations
# 1. Add a new product
def add_product(conn, name, quantity, price, restock_date):
    try:
        sql = '''INSERT INTO products(name, quantity, price, restock_date)
                 VALUES (?, ?, ?, ?);'''
        cursor = conn.cursor()
        cursor.execute(sql, (name, quantity, price, restock_date))
        conn.commit()
        print("Product added successfully.")
    except sqlite3.Error as e:
        print(f"Error: {e}")

# 2. Update an existing product
def update_product(conn, product_id, name, quantity, price, restock_date):
    try:
        sql = '''UPDATE products
                 SET name = ?, quantity = ?, price = ?, restock_date = ?
                 WHERE id = ?;'''
        cursor = conn.cursor()
        cursor.execute(sql, (name, quantity, price, restock_date, product_id))
        conn.commit()
        print("Product updated successfully.")
    except sqlite3.Error as e:
        print(f"Error: {e}")

# 3. Delete a product
def delete_product(conn, product_id):
    try:
        sql = 'DELETE FROM products WHERE id = ?;'
        cursor = conn.cursor()
        cursor.execute(sql, (product_id,))
        conn.commit()
        print("Product deleted successfully.")
    except sqlite3.Error as e:
        print(f"Error: {e}")

# 4. Query products
def query_products(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall()
        print("\nInventory List:")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Quantity: {row[2]}, Price: {row[3]}, Restock Date: {row[4]}")
    except sqlite3.Error as e:
        print(f"Error: {e}")

# Stretch Challenge: Date Filtering (Filter by restock date)
def filter_by_date(conn, start_date, end_date):
    try:
        cursor = conn.cursor()
        sql = '''SELECT * FROM products WHERE restock_date BETWEEN ? AND ?;'''
        cursor.execute(sql, (start_date, end_date))
        rows = cursor.fetchall()
        print(f"\nProducts with restock dates between {start_date} and {end_date}:")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Quantity: {row[2]}, Price: {row[3]}, Restock Date: {row[4]}")
    except sqlite3.Error as e:
        print(f"Error: {e}")

# Main CLI loop
def main():
    conn = create_connection()
    if conn is not None:
        create_table(conn)

        while True:
            print("\nInventory Management System")
            print("1. Add a Product")
            print("2. Update a Product")
            print("3. Delete a Product")
            print("4. View Inventory")
            print("5. Filter by Restock Date")
            print("6. Exit")

            choice = input("Enter your choice (1-6): ")

            if choice == '1':
                name = input("Enter product name: ")
                quantity = int(input("Enter quantity: "))
                price = float(input("Enter price: "))
                restock_date = input("Enter restock date (YYYY-MM-DD): ")
                add_product(conn, name, quantity, price, restock_date)

            elif choice == '2':
                product_id = int(input("Enter product ID to update: "))
                name = input("Enter new product name: ")
                quantity = int(input("Enter new quantity: "))
                price = float(input("Enter new price: "))
                restock_date = input("Enter new restock date (YYYY-MM-DD): ")
                update_product(conn, product_id, name, quantity, price, restock_date)

            elif choice == '3':
                product_id = int(input("Enter product ID to delete: "))
                delete_product(conn, product_id)

            elif choice == '4':
                query_products(conn)

            elif choice == '5':
                start_date = input("Enter start date (YYYY-MM-DD): ")
                end_date = input("Enter end date (YYYY-MM-DD): ")
                filter_by_date(conn, start_date, end_date)

            elif choice == '6':
                print("Exiting the system...")
                break

            else:
                print("Invalid choice! Please try again.")

        conn.close()
    else:
        print("Error! Cannot connect to the database.")

if __name__ == "__main__":
    main()
