import tkinter as tk
from tkinter import messagebox, PhotoImage, filedialog

# Global variable to store conversion history
conversion_history = []

def convert_to_meters(inches):
    # Conversion formula: 1 inch = 0.0254 meters
    meters = inches * 0.0254
    return meters

def convert_to_inches(meters):
    # Conversion formula: 1 meter = 39.3701 inches
    inches = meters * 39.3701
    return inches

def on_clear_results():
    entry_value.delete(0, tk.END)
    result_label.config(text="")
    sentence1_var.set(False)
    sentence2_var.set(False)

def on_checkbox_click():
    # Only deselect if already selected
    if sentence1_var.get() and sentence2_var.get():
        sentence1_var.set(False)
        sentence2_var.set(False)

def on_convert():
    try:
        value = float(entry_value.get())
        if value < 0:
            raise ValueError("Negative value entered")

        if sentence1_var.get():  # Inches to Meters
            result = convert_to_meters(value)
            result_label.config(text=f"{value} inches is {result:.3f} meters")
            conversion_history.append(f"{value} inches is {result:.3f} meters")
        elif sentence2_var.get():  # Meters to Inches
            result = convert_to_inches(value)
            result_label.config(text=f"{value} meters is {result:.3f} inches")
            conversion_history.append(f"{value} meters is {result:.3f} inches")
        else:
            messagebox.showerror("Error", "Please select a conversion type")
    except ValueError as e:
        messagebox.showerror("Error", str(e))
    except Exception as e:
        messagebox.showerror("Error", "An unexpected error occurred")

    # Update the listbox with conversion history
    update_history_listbox()

def update_history_listbox():
    history_listbox.delete(0, tk.END)
    for item in conversion_history:
        history_listbox.insert(tk.END, item)

def clear_history():
    global conversion_history
    conversion_history = []
    update_history_listbox()

def save_result():
    if not history_listbox.curselection():
        messagebox.showinfo("Error", "Please select an item from the list to save its result.")
        return
    selected_item_index = history_listbox.curselection()[0]
    selected_item = history_listbox.get(selected_item_index)
    file_name = f"{selected_item}.txt"
    result = result_label.cget("text")
    with open(file_name, "w") as file:
        file.write(result)

def save_session_results():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        items_saved = len(history_listbox.get(0, tk.END))
        with open(file_path, "w") as file:
            for result in conversion_history:
                file.write(result + "\n")
        messagebox.showinfo("Success", f"{items_saved} item(s) from the conversion history were saved to {file_path}.")

# Create the main window
app = tk.Tk()
app.title("Building Plans Conversion 2")

# Set window size and position it in the center
app.geometry("850x650")
app.eval('tk::PlaceWindow . center')
app.configure(bg="black")  # Set window background color to black

# Load image and resize
image_path = "building.png"
image = PhotoImage(file=image_path).subsample(2, 2)

# Create and place widgets
converter_label = tk.Label(app, text="Converter App 2", font=("Helvetica", 14, "bold"), fg="gold", bg="black")
converter_label.grid(row=0, column=0, columnspan=2, pady=10, sticky=tk.N)

image_label = tk.Label(app, image=image, padx=10, pady=10, relief="solid", bg="black")
image_label.grid(row=1, column=0, rowspan=2, sticky=tk.NSEW)

instruction_label = tk.Label(app, text="Enter a value and choose conversion:", fg="gold", bg="black")
instruction_label.grid(row=1, column=1, pady=10, padx=5, sticky=tk.W)

# Gold box for convert_measurement
convert_measurement_frame = tk.Frame(app, bg="gold", padx=10, pady=10)
convert_measurement_frame.grid(row=2, column=1, pady=10, padx=5, sticky=tk.W)

convert_measurement_label = tk.Label(convert_measurement_frame, text="Convert Measurement", font=("Helvetica", 12, "bold"), bg="gold")
convert_measurement_label.grid(row=0, column=0, pady=5)

# Two radio buttons for unit choices
sentence1_var = tk.BooleanVar()
sentence2_var = tk.BooleanVar()

sentence1_checkbox = tk.Radiobutton(convert_measurement_frame, text="Inches to Meters", variable=sentence1_var, value=True, bg="gold", command=on_checkbox_click)
sentence1_checkbox.grid(row=1, column=0, sticky=tk.W)

sentence2_checkbox = tk.Radiobutton(convert_measurement_frame, text="Meters to Inches", variable=sentence2_var, value=True, bg="gold", command=on_checkbox_click)
sentence2_checkbox.grid(row=2, column=0, sticky=tk.W)

entry_value = tk.Entry(app)
entry_value.grid(row=1, column=2, pady=5, padx=5, sticky=tk.W)

result_label = tk.Label(app, text="", fg="gold", bg="black")
result_label.grid(row=4, column=1, columnspan=2, pady=8)

# Listbox to display conversion history
history_label = tk.Label(app, text="Conversion History", fg="gold", bg="black")
history_label.grid(row=3, column=0, columnspan=2, pady=5, sticky=tk.W)

history_listbox = tk.Listbox(app, width=50)
history_listbox.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

# Button to clear conversion history
clear_history_button = tk.Button(app, text="Clear History", command=clear_history, bg="gold")
clear_history_button.grid(row=5, column=0, pady=10, padx=5, sticky=tk.W)

# Button to save result to file
save_result_button = tk.Button(app, text="Save Result", command=save_result, bg="gold")
save_result_button.grid(row=5, column=1, pady=10, padx=5, sticky=tk.W)

# Button to save session results to file
save_session_button = tk.Button(app, text="Save Session", command=save_session_results, bg="gold")
save_session_button.grid(row=5, column=2, pady=10, padx=5, sticky=tk.W)

# Three buttons at the bottom
convert_button = tk.Button(app, text="Convert", command=on_convert, bg="gold")
convert_button.grid(row=5, column=3, pady=10, padx=5, sticky=tk.W)

clear_button = tk.Button(app, text="Clear Results", command=on_clear_results, bg="gold")
clear_button.grid(row=5, column=4, pady=10, padx=5, sticky=tk.W)

exit_button = tk.Button(app, text="Exit", command=app.destroy, bg="gold")
exit_button.grid(row=5, column=5, pady=10, padx=5, sticky=tk.W)

# Configure row and column weights to make the layout expandable
app.grid_rowconfigure(3, weight=1)
app.grid_columnconfigure(1, weight=1)

# Start the Tkinter event loop
app.mainloop()
