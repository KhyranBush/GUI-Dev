import tkinter as tk
from tkinter import PhotoImage
from tkinter import ttk

def display_statistics():
    label_month_savings.config(text="")
    label_average_savings.config(text="")
    label_max_savings_month.config(text="")
    
    try:
        selected_index = months.index(selected_month.get())
        label_month_savings.config(text=f"Electric Savings for {selected_month.get()}: ${savings[selected_index]:.2f}")
        
        # Placeholder calculation
        total_savings = 0
        max_savings = float('-inf')
        max_month = ""
        for i, month in enumerate(months):
            total_savings += savings[i]
            if savings[i] > max_savings:
                max_savings = savings[i]
                max_month = month
        average_savings = total_savings / len(months)
        label_average_savings.config(text=f"Average Monthly Savings: ${average_savings:.2f}")
        label_max_savings_month.config(text=f"Month with Maximum Savings: {max_month}")
    except ValueError:
        label_average_savings.config(text="Invalid input. Please enter numeric values.")
        label_max_savings_month.config(text="")
        
# Read data from the text file
with open("C:\\Users\\12297\\OneDrive\\Documents\\Smart Home Savings\\savings.txt", "r") as file:
    data = file.readlines()

months = []
savings = []

for line in data:
    month, saving = line.strip().split(',')
    months.append(month)
    savings.append(float(saving))

# Create main window
root = tk.Tk()
root.title("Smart Home Electric Savings Calculator")

# Load and display image
image_path = "smarthome.png"  # Replace with the path to your image
smart_home_image = PhotoImage(file=image_path)
label_image = tk.Label(root, image=smart_home_image)
label_image.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

# Label for Smart Home text
label_smart_home = tk.Label(root, text="Smart Home\n" + "Electric Savings:", font=("Helvetica", 16, "bold"))
label_smart_home.grid(row=0, column=1, padx=10, pady=5, sticky="w")

# Combobox to select months
selected_month = tk.StringVar()
combobox_months = ttk.Combobox(root, textvariable=selected_month, values=months, state="readonly")
combobox_months.grid(row=1, column=1, padx=10, pady=5, sticky="w")

label_month_savings = tk.Label(root, text="", font=("Helvetica", 12))
label_month_savings.grid(row=2, column=1, padx=10, pady=5, sticky="w")

button_display_statistics = tk.Button(root, text="Display Statistics", command=display_statistics)
button_display_statistics.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Label to display electric savings
label_average_savings = tk.Label(root, text="", font=("Helvetica", 12))
label_average_savings.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

label_max_savings_month = tk.Label(root, text="", font=("Helvetica", 12))
label_max_savings_month.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

# Center the window
window_width = 600
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width / 2) - (window_width / 2)
y_coordinate = (screen_height / 2) - (window_height / 2)
root.geometry(f"{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}")

root.mainloop()
