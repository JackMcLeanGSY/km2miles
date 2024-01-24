import tkinter as tk

def convert_km_to_miles():
    km = float(km_input.get())
    miles = km * 0.621371
    miles_label.config(text=f"{miles:.2f} miles")


#Code breaks when I put random letters so I adjusted the code to allow numbers only. 
def validate_input(new_value):
    # Allow empty input
    if new_value == '':
        return True
    try:
        # input to a float
        float(new_value)
        return True
    except ValueError:
        # Input contains non-numbers characters
        return False

# Create the main window
window = tk.Tk()
window.title("Kilometers to Miles Converter")
window.geometry("300x150")
window.resizable(False, False)
window.configure(bg='light blue')

# The grid layout
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)

# The widgets
km_label = tk.Label(window, text="Enter kilometers:", font=("Arial", 10))
km_input = tk.Entry(window, validate='key', validatecommand=(window.register(validate_input), '%S'))
convert_button = tk.Button(
