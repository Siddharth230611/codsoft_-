
import tkinter as tk
from tkinter import messagebox
import pickle

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.load_c()

        tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=10)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(root, text="Phone no.").grid(row=1, column=0, padx=10, pady=10)
        self.phone_entry = tk.Entry(root)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Button(root, text="Add Contact", command=self.add_c).grid(row=2, column=0, padx=10, pady=10)
        tk.Button(root, text="Update Contact", command=self.update_c).grid(row=2, column=1, padx=10, pady=10)
        tk.Button(root, text="Delete Contact", command=self.delete_c).grid(row=2, column=2, padx=10, pady=10)
        tk.Button(root, text="View Contacts", command=self.refresh_c).grid(row=2, column=3, padx=10, pady=10)

        self.contacts_listbox = tk.Listbox(root, width=50, height=15)
        self.contacts_listbox.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

    def load_c(self):
        try:
            with open("contacts.pkl", "rb") as f:
                self.contacts = pickle.load(f)
        except FileNotFoundError:
            self.contacts = {}

    def save_c(self):
        with open("contacts.pkl", "wb") as f:
            pickle.dump(self.contacts, f)

    def add_c(self):
        name, phone = self.name_entry.get().strip(), self.phone_entry.get().strip()
        if name and phone:
            if name in self.contacts:
                messagebox.showwarning("Warning", "Contact already exists")
            else:
                self.contacts[name] = phone
                self.save_c()
                self.refresh_c()
                messagebox.showinfo("Success", "Contact added successfully!")
        else:
            messagebox.showwarning("Warning", "Please enter both name and phone number")

    def update_c(self):
        selected = self.contacts_listbox.curselection()
        if selected:
            name = self.contacts_listbox.get(selected).split(":")[0].strip()
            phone = self.phone_entry.get().strip()
            if phone:
                self.contacts[name] = phone
                self.save_c()
                self.refresh_c()
                messagebox.showinfo("Success", "Contact updated successfully")
            else:
                messagebox.showwarning("Warning", "Please enter a new phone number")
        else:
            messagebox.showwarning("Warning", "Please select a contact to update")

    def delete_c(self):
        selected = self.contacts_listbox.curselection()
        if selected:
            name = self.contacts_listbox.get(selected).split(":")[0].strip()
            del self.contacts[name]
            self.save_c()
            self.refresh_c()
            messagebox.showinfo("Success", "Contact deleted successfully")
        else:
            messagebox.showwarning("Warning", "Please select a contact to delete")

    def refresh_c(self):
        self.contacts_listbox.delete(0, tk.END)
        for name, phone in sorted(self.contacts.items()):
            self.contacts_listbox.insert(tk.END, f"{name}: {phone}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()

