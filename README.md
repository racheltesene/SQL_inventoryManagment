# Overview

I developed an Inventory Management System using Python and SQLite, which integrates seamlessly with a SQL relational database to store and manage inventory data. This software allows users to perform CRUD (Create, Read, Update, Delete) operations on products within the inventory, where each product contains fields such as product name, quantity, price, and restock date. Additionally, the system implements a feature to filter products based on restock dates, giving users the ability to track when products are scheduled to be replenished over specific time periods.

To use the program, users interact with a command-line interface (CLI), where they can:

1. Add a product: Input product details to store in the database.

2. Update a product: Modify an existing product's information by its ID.
3. Delete a product: Remove a product from the database using its ID.
4. View inventory: Display all products currently stored in the database.
5. Filter by restock date: Search for products scheduled to be restocked within a given date range.

# Purpose of Writing the Software

The goal behind developing this software was to further my learning as a software engineer by deepening my understanding of database interactions and SQL commands within Python applications. This project allowed me to gain hands-on experience in implementing SQL queries for creating, reading, updating, and deleting records, and it also provided an opportunity to explore how date-based queries can be used for advanced data filtering. Additionally, I aimed to optimize my ability to write clean, efficient Python code that can interact with relational databases, a crucial skill for building scalable, data-driven software systems.

{Provide a link to your YouTube demonstration. It should be a 4-5 minute demo of the software running, a walkthrough of the code, and a view of how created the Relational Database.}

[Software Demo Video](https://youtu.be/UA-ExRQ3-eU)

# Relational Database

I am using **SQLite**, a lightweight relational database that is embedded directly within the software. SQLite allows for local data storage without the need for complex server configuration, making it ideal for smaller-scale applications like this Inventory Management System. SQLite is also widely supported in Python, making it a practical choice for learning and experimenting with database interactions.

The database I created consists of one main table called `products`. The `products` table is used to store all the necessary information for managing inventory. Each row in the table represents a product, and the table uses a unique identifier (`id`) for each product to enable efficient queries and updates.

#### **Database Structure (Tables)**:
The `products` table contains the following fields:
- `id` (INTEGER, PRIMARY KEY, AUTOINCREMENT): A unique identifier for each product.
- `name` (TEXT, NOT NULL): The name of the product.
- `quantity` (INTEGER, NOT NULL): The available quantity of the product in stock.
- `price` (REAL, NOT NULL): The price of the product.
- `restock_date` (TEXT, NOT NULL): The date when the product is scheduled for restocking, stored in `YYYY-MM-DD` format.

This structure allows for the storage, management, and querying of inventory-related data, including filtering products by restock date.

---

# Development Environment

For developing this software, I used the following tools:

- **Visual Studio Code (VS Code)**: A powerful code editor that supports Python development with features like syntax highlighting, debugging, and version control integration (GitHub). It also provides useful extensions that improve productivity while coding in Python.
  
- **SQLite**: A serverless relational database management system, embedded within the software to handle local data storage and queries.

#### **Programming Language and Libraries**:

- **Python**: I used Python as the primary programming language for this project. Python is widely used in both web and software development, offering powerful libraries and built-in support for interacting with SQLite databases.

- **sqlite3**: The `sqlite3` library, which is part of Python’s standard library, was used to interface with the SQLite database. It enabled me to execute SQL queries for CRUD operations (Create, Read, Update, Delete) and handle the database within the Python code seamlessly.

These tools and libraries worked together to build a fully functioning Inventory Management System that performs the necessary database operations efficiently.
# Useful Websites



- [Relational Databases - Wikipedia](https://en.wikipedia.org/wiki/Relational_database)
- [Relational Databases - Oracle](https://www.oracle.com/database/what-is-a-relational-database/)
- [SQL - W3Schools](https://www.w3schools.com/sql/)

# Future Work


- **Item 1: Improve Error Handling**
  - Implement more robust error handling to gracefully manage issues like invalid user input, database connection errors, and unexpected crashes.
  
- **Item 2: Add User Authentication**
  - Introduce user authentication to limit access to the inventory system, ensuring that only authorized personnel can modify the inventory.

- **Item 3: Implement a Graphical User Interface (GUI)**
  - Upgrade the command-line interface to a more user-friendly GUI using a Python library such as Tkinter or PyQt to enhance user experience.