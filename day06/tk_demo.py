#!/usr/bin/python3
# Filename: tk_demo.py


import tkinter as tk


def callback():
    """
    callback function for buttom click
    """
    listbox.insert(tk.END, "Hello World!")


if __name__ == "__main__":
    master = tk.Tk()


    button = tk.Button(master, text="OK", command=callback)
    button.pack()


    listbox = tk.Listbox(master)
    listbox.pack()


    tk.mainloop()

