import tkinter as tk
from tkinter import PhotoImage, Entry, messagebox

class PayrollApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Payroll Every Two Weeks")

        # Constants
        self.cdecFica = 0.0765
        self.cdecFed = 0.22
        self.cdecState = 0.04

        # Create and place the labels for "FICA," "Federal Tax," and "State Tax"
        self.label_fica = tk.Label(root, text="FICA", font=("Helvetica", 12))
        self.label_federal_tax = tk.Label(root, text="Federal Tax", font=("Helvetica", 12))
        self.label_state_tax = tk.Label(root, text="State Tax", font=("Helvetica", 12))
        self.label_net_pay = tk.Label(root, text="Net Paycheck Income:", font=("Helvetica", 12))

        self.label_fica.grid(row=1, column=0, pady=5, padx=5, sticky='e')
        self.label_federal_tax.grid(row=1, column=1, pady=5, padx=5)
        self.label_state_tax.grid(row=1, column=2, pady=5, padx=5, sticky='w')
        self.label_net_pay.grid(row=2, column=0, pady=5, padx=5, sticky='e')

        # Create and place the entry box for "Gross Pay"
        self.entry_gross_pay = tk.Entry(root, font=("Helvetica", 12), width=10)
        self.entry_gross_pay.grid(row=2, column=1, pady=5, padx=5, sticky='w')
        self.entry_gross_pay.focus()

        # Create and place the buttons for "Compute Taxes," "Clear," and "Exit"
        self.button_compute_taxes = tk.Button(root, text="Compute Taxes", command=self.compute_taxes, bg="blue", fg="white")
        self.button_clear = tk.Button(root, text="Clear", command=self.clear_entry, bg="blue", fg="white")
        self.button_exit = tk.Button(root, text="Exit", command=root.destroy, bg="blue", fg="white")

        self.button_compute_taxes.grid(row=3, column=0, pady=5, padx=5, sticky='e')
        self.button_clear.grid(row=3, column=1, pady=5, padx=5)
        self.button_exit.grid(row=3, column=2, pady=5, padx=5, sticky='w')

        # Create and place the label for "Payroll Calculator"
        label_payroll = tk.Label(root, text="Payroll Calculator", font=("Helvetica", 16))
        label_payroll.grid(row=0, column=1, pady=5)

        # Load the image
        image_path = "C:\\Users\\12297\\OneDrive\\Documents\\Payroll\\payroll.png"  # Replace with the actual path to your image
        image = PhotoImage(file=image_path)
        # Resize the image (adjust width and height as needed)
        resized_image = image.subsample(4, 4)  # Change the values according to your preference

        # Create and place the frame for the picture
        frame_picture = tk.Frame(root, width=100, height=100, bg="lightblue")
        frame_picture.grid(row=0, column=0, padx=10, pady=10)

        # Create and place the label for the resized image
        label_image = tk.Label(frame_picture, image=resized_image)
        label_image.image = resized_image  # To prevent image from being garbage collected
        label_image.pack()

    def compute_taxes(self):
        # Clear labels
        self.label_fica.config(text="FICA")
        self.label_federal_tax.config(text="Federal Tax")
        self.label_state_tax.config(text="State Tax")
        self.label_net_pay.config(text="Net Paycheck Income:")

        # Get input and validate
        str_income = self.entry_gross_pay.get()
        if not self.is_valid_input(str_income):
            messagebox.showerror("Invalid Input", "Please enter a valid numeric value.")
            self.clear_entry()
            return

        # Convert str_income to float
        dec_income = float(str_income)

        # Calculate taxes and net income
        dec_fica = self.cdecFica * dec_income
        dec_federal_tax = self.cdecFed * dec_income
        dec_state_tax = self.cdecState * dec_income
        dec_net = dec_income - (dec_fica + dec_federal_tax + dec_state_tax)

        # Display the results
        self.label_fica.config(text=f"FICA: ${dec_fica:.2f}")
        self.label_federal_tax.config(text=f"Federal Tax: ${dec_federal_tax:.2f}")
        self.label_state_tax.config(text=f"State Tax: ${dec_state_tax:.2f}")
        self.label_net_pay.config(text=f"Net Paycheck Income: ${dec_net:.2f}")

    def clear_entry(self):
        # Clear entry box and set focus
        self.entry_gross_pay.delete(0, tk.END)
        self.entry_gross_pay.focus()

    def is_valid_input(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

if __name__ == "__main__":
    root = tk.Tk()
    app = PayrollApp(root)
    root.mainloop()
