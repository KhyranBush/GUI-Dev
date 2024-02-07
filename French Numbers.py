"""
French Numbers: GUI:
-------------------
Description:
-------------
This script creates an app that lets users press a button and view its name in french.

Author:
-------
[Khyran Bush]

Date: 02/05/2024
-----
[02/05/2024]

"""

import tkinter as tk
from tkinter import ttk
#these two functions make the frame draggable
def on_title_bar_press(event):
    global offset_x, offset_y
    offset_x = event.x
    offset_y = event.y

def on_title_bar_drag(event):
    x = root.winfo_x() + event.x - offset_x
    y = root.winfo_y() + event.y - offset_y
    root.geometry(f"+{x}+{y}")

def disable_event():
    pass  # Do nothing to disable the minimize/maximize actions

def update_french_word(number): # Dictionary function that lists the words in french
    french_words = {
        1: "Un",
        2: "Deux",
        3: "Trois",
        4: "Quatre",
        5: "Cinq",
    }

    word = french_words.get(number, "Unknown")
    french_textbox.delete(1.0, tk.END)  # Clear the text box
    french_textbox.insert(tk.END, f"{word}")
    french_textbox.tag_add("center", "1.0", "end")  # Center align the text
    french_textbox.tag_configure("center", justify='center')

def create_main_window():
    global root, french_textbox
    root = tk.Tk()
    root.title("French Numbers")

    # Set window attributes to make it non-resizable and without minimize/maximize buttons
    root.overrideredirect(False)  # Set to True if you want to remove the window decorations (title bar)
    root.resizable(False, False)
    root.attributes("-toolwindow", 1)  # Remove minimize/maximize buttons on Windows
    root.protocol("WM_DELETE_WINDOW", disable_event)  # Disable the close button

    style = ttk.Style()
    style.theme_use('clam')

    # Create a title bar as a draggable area
    title_bar = ttk.Frame(root, relief='flat', borderwidth=0)
    title_bar.pack(fill='x')

    label = tk.Label(title_bar, text="Do you know the French words for the numbers\n 1 through 5?\nClick the buttons below to see them.", fg="white", bg="#2e2e2e")
    label.pack(side="left", fill="x")

    # Bind events for dragging the window
    title_bar.bind("<ButtonPress-1>", on_title_bar_press)
    title_bar.bind("<B1-Motion>", on_title_bar_drag)

    button_frame = tk.Frame(root)
    button_frame.pack()

    french_textbox = tk.Text(root, wrap=tk.WORD, height=1, width=6, font=("Arial", 8), fg="green")
    french_textbox.pack(pady=10)

    button_font = ("Arial", 16)  # Change the font and size as needed

    # Create number buttons and associate them with the update_french_word function
    for i in range(1, 6):
        button = tk.Button(button_frame, text=str(i), command=lambda num=i: update_french_word(num), font=button_font)
        button.pack(side=tk.LEFT, padx=10, pady=5)

    exit_button = tk.Button(root, text="Exit", command=root.destroy)
    exit_button.pack(pady=10)

    return root

if __name__ == "__main__":
    main_window = create_main_window()
    main_window.mainloop()
