import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())

    if length <= 0:
        password.set("Invalid length")
        return

    # Define character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Create a pool of characters based on user selection
    pool = ""
    if var_lower.get():
        pool += lower
    if var_upper.get():
        pool += upper
    if var_digits.get():
        pool += digits
    if var_symbols.get():
        pool += symbols

    if pool == "":
        password.set("Select at least one character type")
        return

    # Generate password
    password_str = ''.join(random.choice(pool) for i in range(length))
    password.set(password_str)

# Create main window
window = tk.Tk()
window.title("Random Password Generator")

# Password length label and entry
length_label = tk.Label(window, text="Enter password length:")
length_label.grid(row=0, column=0, padx=10, pady=10)

length_entry = tk.Entry(window, width=10)
length_entry.grid(row=0, column=1, padx=10, pady=10)

# Checkbuttons for character types
var_lower = tk.IntVar()
lower_check = tk.Checkbutton(window, text="Lowercase", variable=var_lower)
lower_check.grid(row=1, column=0, padx=10, pady=5, sticky='w')

var_upper = tk.IntVar()
upper_check = tk.Checkbutton(window, text="Uppercase", variable=var_upper)
upper_check.grid(row=1, column=1, padx=10, pady=5, sticky='w')

var_digits = tk.IntVar()
digits_check = tk.Checkbutton(window, text="Digits", variable=var_digits)
digits_check.grid(row=2, column=0, padx=10, pady=5, sticky='w')

var_symbols = tk.IntVar()
symbols_check = tk.Checkbutton(window, text="Symbols", variable=var_symbols)
symbols_check.grid(row=2, column=1, padx=10, pady=5, sticky='w')

# Button to generate password
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.grid(row=3, columnspan=2, padx=10, pady=10)

# Display the generated password
password_label = tk.Label(window, text="Generated Password:")
password_label.grid(row=4, column=0, padx=10, pady=5, sticky='w')

password = tk.StringVar()
password_entry = tk.Entry(window, textvariable=password, state='readonly')
password_entry.grid(row=4, column=1, padx=10, pady=5, sticky='w')

# Start the tkinter main loop
window.mainloop()