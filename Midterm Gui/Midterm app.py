import tkinter as tk
from tkinter import PhotoImage

def convert_to_meters(inches):
    # Conversion factor: 1 inch = 0.0254 meters
    meters = inches * 0.0254
    return meters


def convert_to_inches(meters):
    # Conversion factor: 1 meter = 39.3701 inches
    inches = meters * 39.3701
    return inches

def on_convert():
    try:
        value = float(entry_value.get())
        if sentence1_var.get():  # Inches to Meters
            result = convert_to_meters(value)
            result_label.config(text=f"{value} inches is {result:.2f} meters", fg="gold")
        elif sentence2_var.get():  # Meters to Inches
            result = convert_to_inches(value)
            result_label.config(text=f"{value} meters is {result:.2f} inches", fg="gold")
        else:
            result_label.config(text="Please select a conversion type", fg="gold")
    except ValueError:
        result_label.config(text="Please enter a valid number", fg="gold")

def clear_entries():
    entry_value.delete(0, tk.END)
    result_label.config(text="", fg="gold")

def exit_application():
    app.destroy()

# Create the main window
app = tk.Tk()
app.title("Building Plans Conversion")

# Set window size and position it in the center
app.geometry("500x400")
app.eval('tk::PlaceWindow . center')
app.configure(bg="black")  # Set window background color to black

# Load image and resize
image_path = "C:\\Users\\12297\\OneDrive\\Documents\\Midterm Gui\\building.png"
image = PhotoImage(file=image_path).subsample(2, 2)

# Create and place widgets
converter_label = tk.Label(app, text="Converter App", font=("Helvetica", 14, "bold"), fg="gold", bg="black")
converter_label.grid(row=0, column=0, columnspan=2, pady=10, sticky=tk.N)

image_label = tk.Label(app, image=image, padx=10, pady=10, relief="solid", bg="black")
image_label.grid(row=1, column=0, rowspan=2, sticky=tk.NSEW)

instruction_label = tk.Label(app, text="Enter a value and\n choose conversion:", fg="gold", bg="black")
instruction_label.grid(row=1, column=1, pady=10, padx=5, sticky=tk.W)

# Gold box for convert_measurement
convert_measurement_frame = tk.Frame(app, bg="gold", padx=10, pady=10)
convert_measurement_frame.grid(row=2, column=1, pady=10, padx=5, sticky=tk.W)

convert_measurement_label = tk.Label(convert_measurement_frame, text="Convert Measurement", font=("Helvetica", 12, "bold"), bg="gold")
convert_measurement_label.grid(row=0, column=0, pady=5)

# Two sentences with checkboxes
sentence1_var = tk.BooleanVar()
sentence2_var = tk.BooleanVar()

sentence1_checkbox = tk.Checkbutton(convert_measurement_frame, text="Inches to Meters", variable=sentence1_var, bg="gold")
sentence1_checkbox.grid(row=1, column=0, sticky=tk.W)

sentence2_checkbox = tk.Checkbutton(convert_measurement_frame, text="Meters to Inches", variable=sentence2_var, bg="gold")
sentence2_checkbox.grid(row=2, column=0, sticky=tk.W)

entry_value = tk.Entry(app)
entry_value.grid(row=1, column=2, pady=5, padx=5, sticky=tk.W)


result_label = tk.Label(app, text="", fg="gold", bg="black")
result_label.grid(row=4, column=1, columnspan=2, pady=8)

# Three buttons at the bottom
convert_button = tk.Button(app, text="Convert", command=on_convert, bg="gold")
convert_button.grid(row=5, column=0, pady=10, padx=5, sticky=tk.W)

clear_button = tk.Button(app, text="Clear", command=clear_entries, bg="gold")
clear_button.grid(row=5, column=1, pady=10, padx=5, sticky=tk.W)

exit_button = tk.Button(app, text="Exit", command=exit_application, bg="gold")
exit_button.grid(row=5, column=2, pady=10, padx=5, sticky=tk.W)

# Configure row and column weights to make the layout expandable
app.grid_rowconfigure(3, weight=1)
app.grid_columnconfigure(1, weight=1)

# Start the Tkinter event loop
app.mainloop()
