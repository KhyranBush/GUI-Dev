import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage

def submit_order():
    # Get meal choice
    meal_choice = meal_var.get()

    # Check if meal choice is selected
    if meal_choice == "":
        messagebox.showwarning("Error", "Please select a meal choice.")
        return

    # Display order summary
    summary = f"Meal Choice: {meal_choice}"
    messagebox.showinfo("Order Summary", summary)

def calculate_points():
    global meal_var, selections  # Access meal_var and selections globally

    meal_price = 0.0

    # Calculate meal price based on selected items
    for var, item in zip(selections, ["Gourmet Cheese", "Pinwheel Wraps", "Veggie", "Sausage and Cheese", "Fruit"]):
        if var.get():
            # Define meal prices based on items
            if item == "Gourmet Cheese":
                meal_price += 49.99
            elif item == "Pinwheel Wraps":
                meal_price += 39.99
            elif item == "Veggie":
                meal_price += 29.99
            elif item == "Sausage and Cheese":
                meal_price += 59.99
            elif item == "Fruit":
                meal_price += 19.99

    if meal_price == 0:
        messagebox.showwarning("Error", "Please select at least one meal item.")
        return

    try:
        loyalty_points = int(entry_loyalty_points.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for Loyalty Points.")
        entry_loyalty_points.delete(0, tk.END)
        entry_loyalty_points.focus()
        return

    if loyalty_points < 0:
        messagebox.showerror("Error", "Loyalty Points cannot be negative.")
        entry_loyalty_points.delete(0, tk.END)
        entry_loyalty_points.focus()
        return

    # Calculate discount based on loyalty points
    if 1 <= loyalty_points <= 10:
        discount_percentage = loyalty_points * 0.01  # 1 loyalty point = 1% discount
        total_discount = discount_percentage * meal_price
        final_price = meal_price - total_discount
        payment_info = f"Your order costs ${final_price:.2f} using {loyalty_points} loyalty points after a discount of {total_discount:.2f}."
    else:
        payment_info = f"Your order costs ${meal_price:.2f}. Loyalty points discount is not applicable for the entered amount."

    label_payment_info.config(text=payment_info)

def clear_entries():
    # Clear all entry fields
    meal_var.set("")  # Reset meal_var
    entry_loyalty_points.delete(0, tk.END)
    entry_loyalty_points.focus()
    label_payment_info.config(text="")

# Create main window
root = tk.Tk()
root.title("Catering")

# Title label
title_label = tk.Label(root, text="Catering", font=("Helvetica", 16))
title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Star Market label
label_star_market = tk.Label(root, text="Star Market", font=("Helvetica", 12))
label_star_market.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

# Textbox
textbox = tk.Text(root, bg="white", bd=0, highlightthickness=0, width=30, height=5)
textbox.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")

# Checkbuttons
selections = []
for i, item in enumerate(["Gourmet Cheese", "Pinwheel Wraps", "Veggie", "Sausage and Cheese", "Fruit"]):
    var = tk.BooleanVar()
    checkbutton = tk.Checkbutton(root, variable=var, text=item)
    textbox.window_create(tk.END, window=checkbutton)
    selections.append(var)
    textbox.insert(tk.END, f" - $49.99\n")

# Disable editing of the text box
textbox.config(state=tk.DISABLED)

# Payment options
label_payment = tk.Label(root, text="Payment Option:")
label_payment.grid(row=10, column=0, padx=10, pady=5, sticky="e")

payment_var = tk.StringVar()
payment_var.set("Pre-pay")

radio_prepay = tk.Radiobutton(root, text="Pre-pay", variable=payment_var, value="Pre-pay")
radio_prepay.grid(row=10, column=1, padx=10, pady=5, sticky="w")

radio_pay_upon_pickup = tk.Radiobutton(root, text="Pay upon Pickup", variable=payment_var, value="Pay upon Pickup")
radio_pay_upon_pickup.grid(row=11, column=1, padx=10, pady=5, sticky="w")

# Picture label
catering_image = PhotoImage(file="C:\\Users\\12297\\OneDrive\\Documents\\Catering\\platter.png")  # Replace "catering_image.png" with the path to your image
catering_image = catering_image.subsample(2, 2)  # Resize the image to half of its original size
label_picture = tk.Label(root, image=catering_image)
label_picture.grid(row=0, column=3, rowspan=13, padx=10, pady=10, sticky="ne")

# Loyalty points label
label_loyalty_points = tk.Label(root, text="Loyalty Points:")
label_loyalty_points.grid(row=13, column=3, padx=10, pady=5, sticky="nw")

# Loyalty points textbox
entry_loyalty_points = tk.Entry(root)
entry_loyalty_points.grid(row=13, column=3, padx=10, pady=5, sticky="ne")

# Calculate and Clear buttons
button_calculate = tk.Button(root, text="Calculate", command=calculate_points)
button_calculate.grid(row=14, column=3, padx=5, pady=5, sticky="w")

button_clear = tk.Button(root, text="Clear", command=clear_entries)
button_clear.grid(row=14, column=3, padx=5, pady=5, sticky="e")

# Payment information label
label_payment_info = tk.Label(root, text="")
label_payment_info.grid(row=15, column=0, columnspan=2, padx=10, pady=10)

# Center the window
window_width = 800
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width / 2) - (window_width / 2)
y_coordinate = (screen_height / 2) - (window_height / 2)
root.geometry(f"{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}")

# Define meal_var globally after creating the main window
meal_var = tk.StringVar()

# Run btnClear code on form load
clear_entries()

root.mainloop()
