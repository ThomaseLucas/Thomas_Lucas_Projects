import tkinter as tk
from tkinter import messagebox
import json
import os
import time


current_turn = "X"
x_o_labels = []
game_board = [['', '', ''], ['', '', ''], ['', '', '']]
game_over = False

def Reset_Game():
    global buttons, current_turn, x_o_labels, game_board, game_over
    #print(f"Reset_Game function = Current turn: {current_turn}")
    #print(f"Reset_Game function = Game board after move: {game_board}")
    current_turn = "X"  # Reset the turn to "X"
    game_over = False

    # Clear all buttons
    for row in buttons:
        for button in row:
            button.config(text='', state=tk.NORMAL)
    
    for label in x_o_labels:
        label.destroy()

    x_o_labels.clear()
    game_board = [['', '', ''], ['', '', ''], ['', '', '']]
    return
def Check_Win(board):
    global game_over, current_turn
    winning_combos = [
        [(0, 0),(0, 1),(0, 2)],
        [(1, 0),(1, 1),(1, 2)],
        [(2, 0),(2, 1),(2, 2)],
        [(0, 0),(1, 0),(2, 0)],
        [(0, 1),(1, 1),(2, 1)],
        [(0, 2),(1, 2),(2, 2)],
        [(0, 0),(1, 1),(2, 2)],
        [(0, 2),(1, 1),(2, 0)]
    ]

    for combo in winning_combos:
        if (game_board[combo[0][0]][combo[0][1]] ==
            game_board[combo[1][0]][combo[1][1]] ==
            game_board[combo[2][0]][combo[2][1]] != ''):
            winner = game_board[combo[0][0]][combo[0][1]]
            game_over = True
            messagebox.showinfo("Winner!", f"{winner} is the winner!")
            time.sleep(.5)
            Reset_Game()
            #print(f"After Win = Current turn: {current_turn}")
            #print(f"Afer Win = Game board after move: {game_board}")
            return
        
    if all(cell != '' for row in game_board for cell in row):
        game_over = True
        messagebox.showinfo("Draw!", "It's a draw!")
        time.sleep(.5)
        Reset_Game()
        #print(f"After Draw = Current turn: {current_turn}")
        #print(f"Game board after move: {game_board}")
        return

    return
def Handle_Click(r, c):
    global current_turn, x_o_labels
    global buttons
    global game_root
    global game_board, game_over

    #print(f" After Click = Current turn: {current_turn}")
    #print(f"Game board after move: {game_board}")

    # Stop handling clicks if the game is over.
    if game_over:
        return

    # Check if the button is already clicked
    if buttons[r][c]["text"] == '':
        global xolabel
        # Place a giant X or O on the button depending on the current turn
        xolabel = tk.Label(game_root, text = current_turn, font = ("arial", 200), bg = "white",
                           fg = "red" if current_turn == "X" else "blue")
        xolabel.place(x = buttons[r][c].winfo_x(), y = buttons[r][c].winfo_y(),
                      width = buttons[r][c].winfo_width(), height = buttons[r][c].winfo_height())
        
        x_o_labels.append(xolabel)
        game_board[r][c] = current_turn

        # Check if there's a winner or if the game is over
        Check_Win(game_board)

        # If game is not over, switch turns
        if not game_over:
            current_turn = "O" if current_turn == "X" else "X"
        
    else:
        messagebox.showwarning("Warning", "This spot is already taken!")
def Start_Game(username):
    global game_root, canvas
    game_root = tk.Tk()
    game_root.title(f"Tic Tac Toe --{username}")
    game_root.geometry("680x755")
    game_root.configure(bg = "black")

    global buttons
    buttons = []
    for i in range(3):
        row_buttons = []
        for j in range(3):
            button = tk.Button(game_root, text = '', width = 10, height = 5,
                               bg = "white", font = ('Arial', 24),
                               anchor = 'center',
                               padx = 10, pady = 10,
                               command = lambda r = i, c = j: Handle_Click(r, c))   
            button.grid(row = i, column = j, padx = 5, pady = 5)
            row_buttons.append(button)
        buttons.append(row_buttons)

    tk.Button(game_root, text = "Restart", command = lambda: Reset_Game()).grid(row = 3, column = 1, pady = 10)
    
    game_root.mainloop()

    return
def Load_Profile(username):
    global root

    if not username:
        messagebox.showerror("Error", "Please enter your username")
        return

    tictactoe_users = []

    if os.path.exists('profiles.json'):
        with open('profiles.json', 'r') as fin:
            try:
                tictactoe_users = json.load(fin)
            except json.JSONDecodeError:
                messagebox.showerror("Error", "Failed to load existing file")
                return

    if username in tictactoe_users:
        root.destroy()
        Start_Game(username)
        
    else: 
        messagebox.showerror("Error", "No such username exists.")
        return
    return
def Create_Profile(username):
    if not username:
        messagebox.showerror("Error", "Username cannot be empty")
        return
    
    tictactoe_users = []

    if os.path.exists('profiles.json'):
        with open('profiles.json', 'r') as fin:
            try:
                tictactoe_users = json.load(fin)
            except json.JSONDecodeError:
                messagebox.showerror("Error", "Failed to load existing files")
                return
            
    if username in tictactoe_users:
        messagebox.showerror("Error", "Username already exists")
    else:
        tictactoe_users.append(username)
        with open('profiles.json', 'w') as fout:
            json.dump(tictactoe_users, fout)
        messagebox.showinfo("Profile Created", f"Profile '{username}' created successfully")

            

    return
def Clear_Profiles():
    with open('profiles.json', 'w') as fout:
        fout.write("[]")
    messagebox.showinfo("Profiles Cleared", "All profiles have been cleared")
def Start_Main_Window():
    global root
    root = tk.Tk()
    root.title("Main Menu")
    root.geometry("600x600")


    tk.Label(root, text = "Enter Profile Name: ").pack(pady = 10)
    name_entry = tk.Entry(root)
    name_entry.pack(pady = 10)

    #tk.Label(root, text = "Enter password:").pack(pady = 10)
    #name_entry = tk.Entry(root)
    #name_entry.pack(pady = 10)

    tk.Button(root, text = "Play Game", command = lambda: Load_Profile(name_entry.get())).pack(pady =  5)
    tk.Button(root, text = "Create Profile", command = lambda: Create_Profile(name_entry.get())).pack(pady = 5)
    tk.Button(root, text = "Clear Profiles", command = lambda: Clear_Profiles()).pack(pady = 5)

    root.mainloop()
def main():
    Start_Main_Window()
if __name__ == "__main__":
    main()