import tkinter as tk
import random

def generate_password():
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' + '0123456789' + '!@#$%^&*()_+-=[]{}|;:,.<>/?'
    password_length = 12
    password = ''.join(random.choice(characters) for i in range(password_length))
    entry.delete(0, tk.END) 
    entry.insert(0, password)

window = tk.Tk()
window.title('Random Password Generator')
window.geometry('400x120') 
window.resizable(False, False)

entry = tk.Entry(
    window, 
    fg="yellow", 
    bg="blue", 
    width=50, 
    justify='center',
    font=('Arial', 10, 'bold')
) 
entry.pack(pady=20, padx=10)
entry.insert(0, "Click 'GENERATE' to create your secret keeper.")

button = tk.Button(
    window, 
    text="GENERATE", 
    fg='white', 
    bg='black',
    command=generate_password 
)
button.pack(pady=5)

window.mainloop()