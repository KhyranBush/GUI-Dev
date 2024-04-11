import tkinter as tk
from tkinter import messagebox

def calculate_cost():
    # Declare and initialize cost levels
    cost_convention_superhero = 100
    cost_convention_autographs = 150
    cost_convention = 50

    # Check if group size is numeric
    group_size = entry_group_size.get()
    if not group_size:
        messagebox.showerror("Error", "Please enter group size.")
        return
    try:
        group_size = int(group_size)
    except ValueError:
        messagebox.showerror("Error", "Group size must be a number.")
        return

    # Check if group size is between 1 and 20
    if not 1 <= group_size <= 20:
        messagebox.showerror("Error", "Group size must be between 1 and 20.")
        return

    # Determine which cost level is selected
    if badge_var1.get():
        total_cost = group_size * cost_convention_superhero
    elif badge_var2.get():
        total_cost = group_size * cost_convention_autographs
    elif badge_var3.get():
        total_cost = group_size * cost_convention
    else:
        messagebox.showerror("Error", "Please select a badge type.")
        return

    # Step 3: Calculate total cost amount and display results
    cost_textbox.delete(1.0, tk.END)  # Clear previous content
    cost_textbox.insert(tk.END, f"${total_cost}")


def clear_fields():
    entry_group_size.delete(0, tk.END)
    badge_var1.set(False)
    badge_var2.set(False)
    badge_var3.set(False)
    cost_textbox.delete(1.0, tk.END)

# Create main window
root = tk.Tk()
root.title("Comic Convention Registration")
root.geometry("550x550")  # Set initial window size

# Load banner image and resize
banner_img = tk.PhotoImage(file="C:\\Users\\12297\\OneDrive\\Documents\\COmic\\comic.png")
banner_img = banner_img.subsample(6, 6)  # Resize by specifying the subsample factor

# Image panel
image_panel = tk.Label(root, image=banner_img)
image_panel.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

# Comic Convention Registration label
registration_label = tk.Label(root, text="Comic Convention Registration", fg="red", font=("Helvetica", 16, "bold"))
registration_label.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

# Group Size label and entry
label_group_size = tk.Label(root, text="Group Size:")
label_group_size.grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_group_size = tk.Entry(root)
entry_group_size.grid(row=2, column=1, padx=10, pady=5)

# Badge type checkboxes
badge_var1 = tk.BooleanVar()
badge_var2 = tk.BooleanVar()
badge_var3 = tk.BooleanVar()

# Checkbox labels
check_convention_superhero = tk.Checkbutton(root, text="Convention + Superhero Experience", variable=badge_var1)
check_convention_superhero.grid(row=3, column=0, padx=10, sticky="w")
check_convention_autographs = tk.Checkbutton(root, text="Convention Plus Autographs", variable=badge_var2)
check_convention_autographs.grid(row=4, column=0, padx=10, sticky="w")
check_convention = tk.Checkbutton(root, text="Convention", variable=badge_var3)
check_convention.grid(row=5, column=0, padx=10, sticky="w")

# Registration Cost label and result
cost_label = tk.Label(root, text="Registration Cost: ", font=("Helvetica", 12))
cost_label.grid(row=6, column=0, padx=10, pady=5, sticky="w")

cost_textbox = tk.Text(root, height=1, width=10)
cost_textbox.grid(row=6, column=1, padx=10, pady=5)

calculate_cost_button = tk.Button(root, text="Calculate", command=calculate_cost)
calculate_cost_button.grid(row=7, column=0, padx=10, pady=5)

# Clear button
clear_button = tk.Button(root, text="Clear", command=clear_fields)
clear_button.grid(row=7, column=1, padx=10, pady=5)

# Register button
btn_register = tk.Button(root, text="Register", command=register)
btn_register.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

# Adjust font sizes
root.option_add("*Font", "Helvetica 12")

# Start the application
root.mainloop()
