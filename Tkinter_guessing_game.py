import tkinter as tk
from tkinter import ttk, messagebox
import time

def show_loading_screen():
    def show_next_label():
        nonlocal current_label_index
        
        if current_label_index < len(loading_labels):
            loading_labels[current_label_index].pack()
            root.update()
            current_label_index += 1
            root.after(3000, show_next_label)  # Showing each label for 3 seconds
        else:
            loading_screen.destroy()  # Closing the loading screen
            input_value = entry.get()
            messagebox.showinfo("Result", f"You thought of: {input_value}")
    
    loading_screen = tk.Toplevel(root)
    loading_screen.title("Calculating...")

    loading_labels = [
        tk.Label(loading_screen, text="AI is calculating your value..."),
        tk.Label(loading_screen, text="Analyzing your past use-case scenarios with number..."),
        tk.Label(loading_screen, text="Looking for your previous activities in the dark web..."),
        tk.Label(loading_screen, text="Hacking into your mobile phone..."),
        tk.Label(loading_screen, text="AI Found the Answer...")  
    ]
    
    current_label_index = 0
    show_next_label()

    # Centering the loading screen
    loading_width = 300
    loading_height = 150
    x_loading = (root.winfo_screenwidth() - loading_width) // 2
    y_loading = (root.winfo_screenheight() - loading_height) // 2
    loading_screen.geometry(f"{loading_width}x{loading_height}+{x_loading}+{y_loading}")

# Creating the main window
root = tk.Tk()
root.title("AI Number Guesser")

# Calculating the center position of the main window
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 400  # Set the desired width
window_height = 200  # Set the desired height
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# Setting the dimensions and position of the main window
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Creating an entry field for input
entry_label = tk.Label(root, text="Enter a value for the AI to guess:")
entry_label.pack()
entry = tk.Entry(root)
entry.pack()

# Creating a button to trigger the loading screen
load_button = tk.Button(root, text="Enter", command=show_loading_screen)
load_button.pack()

# Starting the Tkinter main loop
root.mainloop()
