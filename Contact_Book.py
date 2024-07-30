import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("Contact Book")
root.geometry("600x400")
contacts = {}
name_var = tk.StringVar()
phone_var = tk.StringVar()
email_var = tk.StringVar()
address_var = tk.StringVar()
def add_contact():
    name = name_var.get()
    phone = phone_var.get()
    email = email_var.get()
    address = address_var.get()
    if name and phone:
        contacts[name] = {'phone': phone, 'email': email, 'address': address}
        messagebox.showinfo("Success", "Contact added successfully")
        view_contacts()
        clear_fields()
    else:
        messagebox.showwarning("Input Error", "Name and Phone are required")
def view_contacts():
    contact_list.delete(0, tk.END)
    for name, details in contacts.items():
        contact_list.insert(tk.END, f"{name}: {details['phone']}")
def search_contact():
    search_term = name_var.get()
    contact_list.delete(0, tk.END)
    for name, details in contacts.items():
        if search_term.lower() in name.lower() or search_term in details['phone']:
            contact_list.insert(tk.END, f"{name}: {details['phone']}")
def update_contact():
    name = name_var.get()
    if name in contacts:
        contacts[name] = {'phone': phone_var.get(), 'email': email_var.get(), 'address': address_var.get()}
        messagebox.showinfo("Success", "Contact updated successfully")
        view_contacts()
        clear_fields()
    else:
        messagebox.showwarning("Error", "Contact not found")
def delete_contact():
    name = name_var.get()
    if name in contacts:
        del contacts[name]
        messagebox.showinfo("Success", "Contact deleted successfully")
        view_contacts()
        clear_fields()
    else:
        messagebox.showwarning("Error", "Contact not found")
def clear_fields():
    name_var.set("")
    phone_var.set("")
    email_var.set("")
    address_var.set("")
tk.Label(root, text="Name").pack()
tk.Entry(root, textvariable=name_var).pack()
tk.Label(root, text="Phone").pack()
tk.Entry(root, textvariable=phone_var).pack()
tk.Label(root, text="Email").pack()
tk.Entry(root, textvariable=email_var).pack()
tk.Label(root, text="Address").pack()
tk.Entry(root, textvariable=address_var).pack()
tk.Button(root, text="Add Contact", command=add_contact).pack(pady=5)
tk.Button(root, text="View Contacts", command=view_contacts).pack(pady=5)
tk.Button(root, text="Search Contact", command=search_contact).pack(pady=5)
tk.Button(root, text="Update Contact", command=update_contact).pack(pady=5)
tk.Button(root, text="Delete Contact", command=delete_contact).pack(pady=5)
contact_list = tk.Listbox(root)
contact_list.pack(fill=tk.BOTH, expand=1)
root.mainloop()