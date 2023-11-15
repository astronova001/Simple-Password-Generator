import string
import random
import tkinter as tk
from tkinter import messagebox

def generate_password(length, upper, lower, numerals, special):
    all_chars = [
        (string.ascii_uppercase, upper),
        (string.ascii_lowercase, lower),
        (string.digits, numerals),
        (string.punctuation, special),
    ]

    password = []
    for chars, num in all_chars:
        password.extend(random.choices(chars, k=num))

    if len(password) < length:
        password.extend(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length-len(password)))

    random.shuffle(password)
    return ''.join(password)

def main():
    length = int(length_entry.get())
    upper = int(upper_entry.get())
    lower = int(lower_entry.get())
    numerals = int(numerals_entry.get())
    special = int(special_entry.get())

    password = generate_password(length, upper, lower, numerals, special)
    messagebox.showinfo("Generated Password", f"Your generated password is: {password}")

root = tk.Tk()

length_label = tk.Label(root, text="Enter the total length of the password: ")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

upper_label = tk.Label(root, text="Enter the number of uppercase letters: ")
upper_label.pack()
upper_entry = tk.Entry(root)
upper_entry.pack()

lower_label = tk.Label(root, text="Enter the number of lowercase letters: ")
lower_label.pack()
lower_entry = tk.Entry(root)
lower_entry.pack()

numerals_label = tk.Label(root, text="Enter the number of numerals: ")
numerals_label.pack()
numerals_entry = tk.Entry(root)
numerals_entry.pack()

special_label = tk.Label(root, text="Enter the number of special characters: ")
special_label.pack()
special_entry = tk.Entry(root)
special_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=main)
generate_button.pack()

root.mainloop()
