from tkinter import ttk
import tkinter

root = tkinter.Tk()

style = ttk.Style()
style.theme_use("default")

ttk.Combobox().pack()
tkinter.Button(root, text="press me", height=10).pack()
ttk.Button(root, text="not me", padding=50).pack(pady=10, padx=10)

root.mainloop()