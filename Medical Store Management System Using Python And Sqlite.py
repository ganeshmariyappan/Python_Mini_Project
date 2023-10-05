#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sqlite3
import tkinter as tk
from tkinter import messagebox

conn = sqlite3.connect("medical_store.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    price REAL,
                    stock INTEGER
                )''')
conn.commit()

def add_product():
    name = name_entry.get()
    price = price_entry.get()
    stock = stock_entry.get()
    
    try:
        price = float(price)
        stock = int(stock)
    except ValueError:
        messagebox.showerror("Error", "Invalid price or stock value. Please enter valid numbers.")
        return

    cursor.execute("INSERT INTO products (name, price, stock) VALUES (?, ?, ?)", (name, price, stock))
    conn.commit()
    messagebox.showinfo("Success", "Product added successfully.")
    clear_entries()
    update_product_list()
    
def update_product():
    selected_item = product_listbox.curselection()
    if not selected_item:
        messagebox.showerror("Error", "Please select a product to edit.")
        return

    selected_item_index = selected_item[0]  # Get the selected item's index
    selected_item_data = product_listbox.get(selected_item_index)  # Get the text representation of the selected item
    selected_item_id = int(selected_item_data.split(' - ')[0])  # Extract the product's ID from the selected item

    name = name_entry.get()
    price = price_entry.get()
    stock = stock_entry.get()

    try:
        price = float(price)
        stock = int(stock)
    except ValueError:
        messagebox.showerror("Error", "Invalid price or stock value. Please enter valid numbers.")
        return

    cursor.execute("UPDATE products SET name=?, price=?, stock=? WHERE id=?", (name, price, stock, selected_item_id))
    conn.commit()
    messagebox.showinfo("Success", "Product updated successfully.")
    clear_entries()
    update_product_list()

# ... (Previous code remains the same)

def delete_product():
    selected_item = product_listbox.curselection()
    if not selected_item:
        messagebox.showerror("Error", "Please select a product to delete.")
        return

    selected_item = product_listbox.get(selected_item[0])  # Get the text representation of the selected item
    name = selected_item.split(' - ')[0]
    cursor.execute("DELETE FROM products WHERE name=?", (name,))
    conn.commit()
    messagebox.showinfo("Success", "Product deleted successfully.")
    clear_entries()
    update_product_list()



def search_product():
    search_term = search_entry.get()
    cursor.execute("SELECT * FROM products WHERE name LIKE ?", ('%' + search_term + '%',))
    products = cursor.fetchall()
    
    product_listbox.delete(0, tk.END)
    for product in products:
        product_listbox.insert(tk.END, f"{product[1]} - Price: {product[2]} - Stock: {product[3]}")

def clear_entries():
    name_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)
    stock_entry.delete(0, tk.END)

# ... (Previous code remains the same)

def update_product():
    selected_item = product_listbox.curselection()
    if not selected_item:
        messagebox.showerror("Error", "Please select a product to edit.")
        return

    selected_item = product_listbox.get(selected_item[0])  # Get the text representation of the selected item
    name = selected_item.split(' - ')[0]
    new_name = name_entry.get()
    price = price_entry.get()
    stock = stock_entry.get()
    
    try:
        price = float(price)
        stock = int(stock)
    except ValueError:
        messagebox.showerror("Error", "Invalid price or stock value. Please enter valid numbers.")
        return

    cursor.execute("UPDATE products SET name=?, price=?, stock=? WHERE name=?", (new_name, price, stock, name))
    conn.commit()
    messagebox.showinfo("Success", "Product updated successfully.")
    clear_entries()
    update_product_list()

root = tk.Tk()
root.title("Medical Store Management System")


tk.Label(root, text="Product Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Product Price:").pack()
price_entry = tk.Entry(root)
price_entry.pack()

tk.Label(root, text="Stock Quantity:").pack()
stock_entry = tk.Entry(root)
stock_entry.pack()


add_button = tk.Button(root, text="Add Product", command=add_product)
update_button = tk.Button(root, text="Update Product", command=update_product)
delete_button = tk.Button(root, text="Delete Product", command=delete_product)
search_button = tk.Button(root, text="Search Product", command=search_product)

add_button.pack()
update_button.pack()
delete_button.pack()
search_button.pack()


tk.Label(root, text="Search Product:").pack()
search_entry = tk.Entry(root)
search_entry.pack()


product_listbox = tk.Listbox(root, width=50)
product_listbox.pack()


update_product_list()


root.mainloop()


conn.close()


# In[ ]:



