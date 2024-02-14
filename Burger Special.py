import tkinter as tk
from tkinter import messagebox

class BurgerSpecialsApp:
    def __init__(self, root):
        root.title("Burger Specials")

        # Farm Burger Specials
        farm_burger_label = tk.Label(root, text="Farm Burger Specials", font=("Tahoma", 16, "bold"))
        farm_burger_label.grid(row=0, column=0, columnspan=3, pady=5)

        # Two image boxes centered
        left_image_box = tk.Frame(root, width=150, height=150, bg="lightgray")
        left_image_box.grid(row=2, column=0, padx=14, pady=5)

        right_image_box = tk.Frame(root, width=150, height=150, bg="lightgray")
        right_image_box.grid(row=2, column=2, padx=18, pady=5)

        # Three labeled boxes below
        prime_beef_box = tk.Frame(root, width=80, height=40, bg="lightgray")
        prime_beef_box.grid(row=3, column=0, pady=5)

        select_meal_box = tk.Frame(root, width=80, height=40, bg="lightgray")
        select_meal_box.grid(row=3, column=1, pady=5)

        veggie_box = tk.Frame(root, width=80, height=40, bg="lightgray")
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

        # Select Meal button
        select_meal_button = tk.Button(root, text="Select Meal", command=self.show_selected_meal, font=("Tahoma", 9))
        select_meal_button.grid(row=7, column=0, columnspan=3, pady=5)

        # Configure row and column weights to center the content
        root.grid_rowconfigure(2, weight=1)
        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=1)
        root.grid_columnconfigure(2, weight=1)

    def show_selected_meal(self):
        messagebox.showinfo("Selected Meal", "You selected a meal!")

if __name__ == "__main__":
    root = tk.Tk()
    app = BurgerSpecialsApp(root)
    root.mainloop()
