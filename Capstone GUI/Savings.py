import tkinter as tk
import random
from datetime import datetime, timedelta

class ShoppingCartApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Store Management System")
        
        # Set background color of the root window
        self.root.configure(bg="tan")

        # Load shopping cart image
        self.shopping_cart_image = tk.PhotoImage(file="shopping_cart.png")

        # Create shopping cart frame
        self.shopping_cart_frame = tk.Frame(root, bd=2, relief=tk.SUNKEN, bg="tan")
        self.shopping_cart_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsw")

        # Shopping cart label with image
        self.shopping_cart_label = tk.Label(self.shopping_cart_frame, image=self.shopping_cart_image, bd=0, bg="tan")
        self.shopping_cart_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        # Shopping cart title
        self.shopping_cart_title = tk.Label(self.shopping_cart_frame, text="Shopping Cart", font=("Helvetica", 16), bg="tan")
        self.shopping_cart_title.grid(row=0, column=1, columnspan=2, padx=5, pady=5, sticky="w")

        # Create main frame
        self.main_frame = tk.Frame(root, bd=2, relief=tk.SUNKEN, bg="tan")
        self.main_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        
        # Load inventory and create buttons
        self.load_inventory()

        # Create cart items listbox
        self.cart_items_listbox = tk.Listbox(self.main_frame, width=40, height=10)
        self.cart_items_listbox.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        # Checkout button
        self.checkout_button = tk.Button(self.main_frame, text="Checkout", command=self.open_checkout_window, bg="red", fg="white")
        self.checkout_button.grid(row=4, column=0, padx=10, pady=5, sticky="ew")

        # Delete selected button in home screen
        self.delete_selected_button_home = tk.Button(self.main_frame, text="Delete Selected", command=self.delete_selected_item_home, bg="blue", fg="white")
        self.delete_selected_button_home.grid(row=5, column=0, padx=10, pady=5, sticky="ew")

    def load_inventory(self):
        # Load inventory from file
        self.inventory = {}
        try:
            with open("inventory.txt", "r") as file:
                for line in file:
                    name, price = line.strip().split(',')
                    self.inventory[name] = float(price)
        except FileNotFoundError:
            tk.messagebox.showerror("Error", "Inventory file not found.")

        # Calculate number of rows and columns for grid
        num_items = len(self.inventory)
        num_columns = min(num_items, 3)
        num_rows = (num_items + num_columns - 1) // num_columns

        # Create buttons for each item in the inventory
        for i, (name, price) in enumerate(self.inventory.items()):
            row = i // num_columns
            col = i % num_columns
            button = tk.Button(self.main_frame, text=name, width=15, height=3, command=lambda name=name, price=price: self.add_item_from_button(name, price), bg="black", fg="white")
            button.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

    def add_item_from_button(self, name, price):
        # Add item to cart listbox
        self.cart_items_listbox.insert(tk.END, f"{name} - ${price:.2f}")

    def open_checkout_window(self):
        # Create a new window for checkout
        self.checkout_window = tk.Toplevel(self.root)
        self.checkout_window.title("Checkout")

        # Entry fields for user information
        tk.Label(self.checkout_window, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.name_entry = tk.Entry(self.checkout_window)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        tk.Label(self.checkout_window, text="Number:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.number_entry = tk.Entry(self.checkout_window)
        self.number_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        tk.Label(self.checkout_window, text="Address:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.address_entry = tk.Entry(self.checkout_window)
        self.address_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # Cart items listbox in checkout window
        self.cart_items_listbox_checkout = tk.Listbox(self.checkout_window, width=40, height=10)
        self.cart_items_listbox_checkout.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Populate cart items listbox in checkout window
        for item in self.cart_items_listbox.get(0, tk.END):
            self.cart_items_listbox_checkout.insert(tk.END, item)

        # Delete selected button
        self.delete_selected_button_checkout = tk.Button(self.checkout_window, text="Delete Selected", command=self.delete_selected_item_checkout, bg="red", fg="white")
        self.delete_selected_button_checkout.grid(row=4, columnspan=2, padx=10, pady=5, sticky="ew")

        # Finalize button
        self.finalize_button = tk.Button(self.checkout_window, text="Finalize", command=self.finalize_order, bg="blue", fg="white")
        self.finalize_button.grid(row=5, columnspan=2, padx=10, pady=10)

    def delete_selected_item_home(self):
        selected_index = self.cart_items_listbox.curselection()
        if selected_index:
            self.cart_items_listbox.delete(selected_index)

    def delete_selected_item_checkout(self):
        selected_index = self.cart_items_listbox_checkout.curselection()
        if selected_index:
            self.cart_items_listbox_checkout.delete(selected_index)

    def finalize_order(self):
        # Get user information
        name = self.name_entry.get()
        number = self.number_entry.get()
        address = self.address_entry.get()

        # Get items from the cart listbox
        cart_items = self.cart_items_listbox.get(0, tk.END)

        # Display transaction details in the new window
        self.checkout_window.destroy()
        self.checkout_window = tk.Toplevel(self.root)
        self.checkout_window.title("Transaction Details")

        # Display user information and order details
        tk.Label(self.checkout_window, text="User Information", font=("Helvetica", 12, "bold")).grid(row=0, columnspan=2, padx=10, pady=5)
        tk.Label(self.checkout_window, text=f"Name: {name}").grid(row=1, columnspan=2, padx=10, pady=5)
        tk.Label(self.checkout_window, text=f"Number: {number}").grid(row=2, columnspan=2, padx=10, pady=5)
        tk.Label(self.checkout_window, text=f"Address: {address}").grid(row=3, columnspan=2, padx=10, pady=5)

        tk.Label(self.checkout_window, text="Order Details", font=("Helvetica", 12, "bold")).grid(row=4, columnspan=2, padx=10, pady=5)
        for i, item in enumerate(cart_items, start=5):
            tk.Label(self.checkout_window, text=item).grid(row=i, columnspan=2, padx=10, pady=5)
        total_price = sum(float(item.split('$')[-1]) for item in cart_items)
        tk.Label(self.checkout_window, text=f"Total Price: ${total_price:.2f}").grid(row=i+1, columnspan=2, padx=10, pady=5)

        # Generate random delivery time
        delivery_time = datetime.now() + timedelta(days=random.randint(1, 7))
        tk.Label(self.checkout_window, text=f"Estimated Delivery Time: {delivery_time.strftime('%Y-%m-%d %H:%M:%S')}").grid(row=i+2, columnspan=2, padx=10, pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = ShoppingCartApp(root)
    root.mainloop()
