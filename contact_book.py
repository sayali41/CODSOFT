import tkinter as tk
from tkinter import messagebox
import json
import os

# Colors and Fonts
BG_COLOR = "#2C3E50"
BUTTON_COLOR = "#3498DB"
BUTTON_HOVER = "#2980B9"
FONT_STYLE = ("Arial", 14)
TEXT_COLOR = "white"

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("500x550")
        self.root.configure(bg=BG_COLOR)

        self.filename = "contacts.json"
        self.contacts = self.load_contacts()

        # Title
        self.label = tk.Label(root, text="📖 Contact Book", font=("Arial", 18, "bold"), fg=TEXT_COLOR, bg=BG_COLOR)
        self.label.pack(pady=10)

        # Input Fields
        self.create_input_fields()

        # Buttons
        self.create_buttons()

        # Contact Listbox
        self.contact_listbox = tk.Listbox(root, width=50, height=10, font=FONT_STYLE, bg="white", fg="black")
        self.contact_listbox.pack(pady=10)
        self.contact_listbox.bind("<<ListboxSelect>>", self.fill_entries_from_list)  # Select contact to update

        self.view_contacts()  # Show contacts when app starts

    def create_input_fields(self):
        """Create input fields."""
        labels = ["Name", "Phone", "Email", "Address"]
        self.entries = {}

        for label in labels:
            lbl = tk.Label(self.root, text=f"{label}:", font=FONT_STYLE, fg=TEXT_COLOR, bg=BG_COLOR)
            lbl.pack(pady=2)
            entry = tk.Entry(self.root, font=FONT_STYLE, width=30)
            entry.pack(pady=2)
            self.entries[label.lower()] = entry  # Store entries in a dictionary

    def create_buttons(self):
        """Create action buttons."""
        buttons = [
            ("➕ Add Contact", self.add_contact),
            ("📄 View Contacts", self.view_contacts),
            ("🔍 Search Contact", self.search_contact),
            ("✏ Update Contact", self.update_contact),
            ("❌ Delete Contact", self.delete_contact),
        ]

        for text, command in buttons:
            btn = tk.Button(self.root, text=text, font=FONT_STYLE, bg=BUTTON_COLOR, fg=TEXT_COLOR,
                            width=20, command=command)
            btn.pack(pady=5)
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg=BUTTON_HOVER))
            btn.bind("<Leave>", lambda e, b=btn: b.config(bg=BUTTON_COLOR))

    def load_contacts(self):
        """Load contacts from JSON file."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    return json.load(file)
            except json.JSONDecodeError:
                return []
        return []

    def save_contacts(self):
        """Save contacts to JSON file."""
        with open(self.filename, "w") as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self):
        """Add a new contact."""
        name = self.entries["name"].get()
        phone = self.entries["phone"].get()
        email = self.entries["email"].get()
        address = self.entries["address"].get()

        if name and phone:
            self.contacts.append({"name": name, "phone": phone, "email": email, "address": address})
            self.save_contacts()
            self.view_contacts()
            self.clear_entries()
            messagebox.showinfo("Success", "Contact added successfully!")
        else:
            messagebox.showwarning("Warning", "Name and Phone are required!")

    def view_contacts(self):
        """Display all contacts."""
        self.contact_listbox.delete(0, tk.END)
        if not self.contacts:
            self.contact_listbox.insert(tk.END, "No contacts found.")
        else:
            for contact in self.contacts:
                self.contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

    def search_contact(self):
        """Search for a contact by name or phone number."""
        search_query = self.entries["name"].get() or self.entries["phone"].get()
        if not search_query:
            messagebox.showwarning("Warning", "Enter a name or phone number to search!")
            return

        self.contact_listbox.delete(0, tk.END)
        found = False
        for contact in self.contacts:
            if search_query.lower() in contact['name'].lower() or search_query in contact['phone']:
                self.contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")
                found = True

        if not found:
            self.contact_listbox.insert(tk.END, "No results found.")

    def update_contact(self):
        """Update an existing contact."""
        selected = self.contact_listbox.curselection()
        if not selected:
            messagebox.showwarning("Warning", "Select a contact to update!")
            return

        old_contact_text = self.contact_listbox.get(selected[0])
        old_name, old_phone = old_contact_text.split(" - ")

        for contact in self.contacts:
            if contact['name'] == old_name and contact['phone'] == old_phone:
                contact['name'] = self.entries["name"].get() or contact['name']
                contact['phone'] = self.entries["phone"].get() or contact['phone']
                contact['email'] = self.entries["email"].get() or contact['email']
                contact['address'] = self.entries["address"].get() or contact['address']

                self.save_contacts()
                self.view_contacts()
                self.clear_entries()
                messagebox.showinfo("Success", "Contact updated successfully!")
                return

    def delete_contact(self):
        """Delete a selected contact."""
        selected = self.contact_listbox.curselection()
        if not selected:
            messagebox.showwarning("Warning", "Select a contact to delete!")
            return

        contact_text = self.contact_listbox.get(selected[0])
        name, phone = contact_text.split(" - ")

        self.contacts = [c for c in self.contacts if not (c["name"] == name and c["phone"] == phone)]
        self.save_contacts()
        self.view_contacts()
        messagebox.showinfo("Success", "Contact deleted successfully!")

    def fill_entries_from_list(self, event):
        """Auto-fill input fields when a contact is selected from the list."""
        selected = self.contact_listbox.curselection()
        if not selected:
            return

        contact_text = self.contact_listbox.get(selected[0])
        name, phone = contact_text.split(" - ")

        for contact in self.contacts:
            if contact["name"] == name and contact["phone"] == phone:
                self.entries["name"].delete(0, tk.END)
                self.entries["name"].insert(0, contact["name"])
                self.entries["phone"].delete(0, tk.END)
                self.entries["phone"].insert(0, contact["phone"])
                self.entries["email"].delete(0, tk.END)
                self.entries["email"].insert(0, contact["email"])
                self.entries["address"].delete(0, tk.END)
                self.entries["address"].insert(0, contact["address"])

    def clear_entries(self):
        """Clear all input fields."""
        for entry in self.entries.values():
            entry.delete(0, tk.END)

if __name__ == "__main__":
    print("Contact Book is running...")  # ✅ Added to verify execution
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
