import tkinter as tk
from tkinter import messagebox

class BurgerSpecialsApp:
    def __init__(self, root):
        root.title("Burger Specials")

        # Farm Burger Specials
        farm_burger_label = tk.Label(root, text="Farm Burger Specials", font=("Tahoma", 16, "bold"))
        farm_burger_label.grid(row=0, column=0, columnspan=3, pady=5)

        # Two image boxes centered
        left_image_box = tk.Frame(root, width=120, height=120, bg="lightgray")
        left_image_box.grid(row=2, column=0, padx=10, pady=5)

        right_image_box = tk.Frame(root, width=120, height=120, bg="lightgray")
        right_image_box.grid(row=2, column=2, padx=10, pady=5)

        # Three labeled boxes below
        prime_beef_box = tk.Frame(root, width=120, height=120, bg="lightgray")
        prime_beef_box.grid(row=3, column=0, pady=5)

        select_meal_box = tk.Frame(root, width=120, height=120, bg="lightgray")
        select_meal_box.grid(row=3, column=1, pady=5)

        veggie_box = tk.Frame(root, width=120, height=120, bg="lightgray")
        veggie_box.grid(row=3, column=2, pady=5)

        # Words in the boxes
        prime_beef_label = tk.Label(prime_beef_box, text="Prime Beef", font=("Tahoma", 9))
        prime_beef_label.pack(pady=5)

        select_meal_label = tk.Label(select_meal_box, text="Select Meal", font=("Tahoma", 9))
        select_meal_label.pack(pady=5)

        veggie_label = tk.Label(veggie_box, text="Veggie", font=("Tahoma", 9))
        veggie_label.pack(pady=5)

        # Message: "Choose a burger and then click the Select Meal button"
        message_label = tk.Label(root, text="Choose a burger and then click the Select Meal button", font=("Tahoma", 9))
        message_label.grid(row=4, column=0, columnspan=3, pady=5)

        # Enjoy your burger special message
        enjoy_message_label = tk.Label(root, text="Enjoy your burger special", font=("Tahoma", 9))
        enjoy_message_label.grid(row=5, column=0, columnspan=3, pady=5)

        # Exit button
        exit_button = tk.Button(root, text="Exit", command=root.destroy, font=("Tahoma", 9))
        exit_button.grid(row=6, column=0, columnspan=3, pady=5)

        # Images for each burger type with direct paths (resized)
        prime_beef_image = tk.PhotoImage(file="C:\\Users\\12297\\OneDrive\\Documents\\Burger proj\\prime.png").subsample(2, 2)
        veggie_image = tk.PhotoImage(file="C:\\Users\\12297\\OneDrive\\Documents\\Burger proj\\veggie.png").subsample(2, 2)

        # Left and right image labels
        self.left_image_label = tk.Label(left_image_box, image=None, bg="lightgray")
        self.left_image_label.pack(pady=5)

        self.right_image_label = tk.Label(right_image_box, image=None, bg="lightgray")
        self.right_image_label.pack(pady=5)

        # Variables to track selected special and confirmation status
        self.selected_special = None
        self.order_confirmed = False

        # Buttons with direct paths for images and commands
        prime_beef_button = tk.Button(root, text="Prime Beef", command=lambda: self.select_special("Prime Beef", prime_beef_image), font=("Tahoma", 9))
        prime_beef_button.grid(row=3, column=0, pady=5)

        select_meal_button = tk.Button(root, text="Select Meal", command=self.confirm_order, font=("Tahoma", 9))
        select_meal_button.grid(row=3, column=1, pady=5)

        veggie_button = tk.Button(root, text="Veggie", command=lambda: self.select_special("Veggie", veggie_image), font=("Tahoma", 9))
        veggie_button.grid(row=3, column=2, pady=5)

    def select_special(self, special_name, image):
        if not self.order_confirmed:
            if special_name == "Prime Beef":
                self.left_image_label.config(image=image)
                self.left_image_label.image = image
                self.right_image_label.config(image=None)
                self.right_image_label.image = None
            elif special_name == "Veggie":
                self.right_image_label.config(image=image)
                self.right_image_label.image = image
                self.left_image_label.config(image=None)
                self.left_image_label.image = None

            self.selected_special = special_name
            messagebox.showinfo("Selected Special", f"You selected {special_name}!")
        else:
            messagebox.showinfo("Order Confirmed", "Order already confirmed. Cannot change selection.")

    def confirm_order(self):
        if self.selected_special:
            self.order_confirmed = True
            messagebox.showinfo("Order Confirmed", f"You confirmed the order for {self.selected_special}!")
        else:
            messagebox.showinfo("Error", "Please select a special before confirming the order.")

if __name__ == "__main__":
    root = tk.Tk()
    app = BurgerSpecialsApp(root)
    root.mainloop()
