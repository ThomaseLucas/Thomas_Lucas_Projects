import tkinter as tk
from tkinter import messagebox

def Load_Profile():
    return
def Create_Profile():
    return
def Start_Main_Window():
    root = tk.Tk()
    root.title("Main Menu")


    tk.Label(root, text = "Enter Profile Name: ").pack(pady = 10)
    name_entry = tk.Entry(root)
    name_entry.pack(pady = 10)

    tk.Button(root, text = "Load Profile", command = lambda: Load_Profile(name_entry.get())).pack(pady =  5)
    tk.Button(root, text = "Create Profile", command = lambda: Create_Profile(name_entry.get())).pack(pady = 5)

    root.mainloop()









def main():
    Start_Main_Window()

if __name__ == "__main__":
    main()