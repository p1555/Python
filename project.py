import tkinter as tk
from tkinter import messagebox

# Function to save contact to a file
def save_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    
    if name and phone:
        with open("contacts.txt", "a") as file:
            file.write(f"{name} - {phone}\n")
        messagebox.showinfo("Success", "Contact saved successfully!")
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please fill in both fields.")

# Function to view all saved contacts
def view_contacts():
    try:
        with open("contacts.txt", "r") as file:
            contacts = file.readlines()
            if contacts:
                contacts_list.delete(0, tk.END)
                for contact in contacts:
                    contacts_list.insert(tk.END, contact.strip())
            else:
                messagebox.showinfo("No Contacts", "No contacts saved yet.")
    except FileNotFoundError:
        messagebox.showwarning("No File", "Contacts file not found. No contacts saved yet.")

# Setting up the main window
root = tk.Tk()
root.title("Contact Book")
root.geometry("400x400")

# Adding Labels and Entry widgets for name and phone number
tk.Label(root, text="Name:").pack(pady=5)
name_entry = tk.Entry(root, width=40)
name_entry.pack(pady=5)

tk.Label(root, text="Phone Number:").pack(pady=5)
phone_entry = tk.Entry(root, width=40)
phone_entry.pack(pady=5)

# Adding buttons for Save and View
save_button = tk.Button(root, text="Save Contact", command=save_contact)
save_button.pack(pady=10)

view_button = tk.Button(root, text="View Contacts", command=view_contacts)
view_button.pack(pady=10)

# Listbox to display saved contacts
contacts_list = tk.Listbox(root, width=50, height=10)
contacts_list.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
