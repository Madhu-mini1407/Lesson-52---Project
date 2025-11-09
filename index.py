from tkinter import *

window = Tk()
window.title('Random Password Generator')
window.geometry('300x150')

entry = Entry(fg="yellow", bg="blue", width=50, justify='center') 
entry.pack(pady=10)

button = Button(
    text="Click me to create a new secret keeper!", 
    fg='white', 
    bg='black'
)
button.pack(pady=5)

greeting = Label(text="Password is below \n 244466666", fg='black', bg='white')
greeting.pack()

window.mainloop()