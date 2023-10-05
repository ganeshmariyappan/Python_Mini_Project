#!/usr/bin/env python
# coding: utf-8

# In[6]:


import sqlite3
import tkinter as tk
from tkinter import messagebox

# Create a SQLite database and a table for products
conn = sqlite3.connect('medical_store.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        quantity INTEGER NOT NULL
    )
''')
conn.commit()

# ... (rest of the code remains the same)
# Create the main application window
app = tk.Tk()
app.title("Medical Store Management System")

# Functions to perform CRUD operations
def add_product():
    name = name_entry.get()
    price = float(price_entry.get())
    quantity = int(quantity_entry.get())

    cursor.execute('INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)', (name, price, quantity))
    conn.commit()
    clear_entries()
    messagebox.showinfo("Success", "Product added successfully.")

def update_product():
    id = int(id_entry.get())
    name = name_entry.get()
    price = float(price_entry.get())
    quantity = int(quantity_entry.get())

    cursor.execute('UPDATE products SET name=?, price=?, quantity=? WHERE id=?', (name, price, quantity, id))
    conn.commit()
    clear_entries()
    messagebox.showinfo("Success", "Product updated successfully.")

def delete_product():
    id = int(id_entry.get())
    cursor.execute('DELETE FROM products WHERE id=?', (id,))
    conn.commit()
    clear_entries()
    messagebox.showinfo("Success", "Product deleted successfully.")

def search_product():
    id = int(id_entry.get())
    cursor.execute('SELECT * FROM products WHERE id=?', (id,))
    product = cursor.fetchone()
    if product:
        clear_entries()
        id_entry.insert(0, product[0])
        name_entry.insert(0, product[1])
        price_entry.insert(0, product[2])
        quantity_entry.insert(0, product[3])
    else:
        clear_entries()
        messagebox.showinfo("Not Found", "Product not found.")

def view_all_products():
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    if products:
        clear_entries()
        result_text.delete(1.0, tk.END)
        for product in products:
            result_text.insert(tk.END, f"ID: {product[0]}\nName: {product[1]}\nPrice: {product[2]}\nQuantity: {product[3]}\n\n")
    else:
        clear_entries()
        messagebox.showinfo("Empty", "No products found.")

def clear_entries():
    id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)

# Create and arrange widgets
tk.Label(app, text="ID:").grid(row=0, column=0)
id_entry = tk.Entry(app)
id_entry.grid(row=0, column=1)

tk.Label(app, text="Name:").grid(row=1, column=0)
name_entry = tk.Entry(app)
name_entry.grid(row=1, column=1)

tk.Label(app, text="Price:").grid(row=2, column=0)
price_entry = tk.Entry(app)
price_entry.grid(row=2, column=1)

tk.Label(app, text="Quantity:").grid(row=3, column=0)
quantity_entry = tk.Entry(app)
quantity_entry.grid(row=3, column=1)

add_button = tk.Button(app, text="Add Product", command=add_product)
add_button.grid(row=4, column=0)

update_button = tk.Button(app, text="Update Product", command=update_product)
update_button.grid(row=4, column=1)

delete_button = tk.Button(app, text="Delete Product", command=delete_product)
delete_button.grid(row=5, column=0)

search_button = tk.Button(app, text="Search Product", command=search_product)
search_button.grid(row=5, column=1)

view_all_button = tk.Button(app, text="View All Products", command=view_all_products)
view_all_button.grid(row=6, column=0, columnspan=2)

result_text = tk.Text(app, height=10, width=40)
result_text.grid(row=7, column=0, columnspan=2)

app.mainloop()

# Close the database connection when the application is closed
conn.close()


# In[ ]:




