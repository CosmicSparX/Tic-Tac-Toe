# Name -  Pranay Sinha
# Class - XI 'A'
# Roll no. - 40

import tkinter as tk
import tkinter.messagebox
import time


def gui():
    window = tk.Tk()
    window.title("Tic Tac Toe")
    window.resizable(False, False)

    turnG = "X"
    movesG = 0
    lastMove = ""
    win_con = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 4, 8), (2, 4, 6), (0, 3, 6), (1, 4, 7), (2, 5, 8)]

    def next_turn():
        nonlocal turnG, movesG
        
        if turnG == "X":
            turnG = "O"
        elif turnG == "O":
            turnG = "X"
        
        info["text"] = f"Current turn: {turnG}\n Moves: {str(movesG)}"

    def btnClick(i):
        nonlocal turnG, movesG, lastMove

        if buttons[i]["text"] == " ":
            buttons[i]["text"] = turnG
            movesG += 1
            lastMove = buttons[i]
            checkForWin()
            next_turn()
        else:
            tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")

    def disableButton():
        for button in buttons:
            button.configure(state='disabled')
        
        undobtn.configure(state="disabled")

    def checkForWin():
        winner = ""
        for con in win_con:
            i, j, k = con
            if buttons[i]['text'] == buttons[j]['text'] == buttons[k]['text'] != " ":
                winner = buttons[i]['text'] 
                break

        if (winner == "X"):
            disableButton()
            tkinter.messagebox.showinfo("Tic-Tac-Toe", "X wins!")
        elif (winner == "O"):
            disableButton()
            tkinter.messagebox.showinfo("Tic-Tac-Toe", "O wins!")
        elif movesG == 9:
            tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie!")
            disableButton()

    def undo():
        nonlocal turnG, movesG
        if movesG == 0:
            tkinter.messagebox.showinfo("Tic-Tac-Toe", "Game not started!")
        else:
            if lastMove["text"] != " ":
                lastMove["text"] = " "
                movesG -= 1
                next_turn()
            else:
                tkinter.messagebox.showinfo("Tic-Tac-Toe", "No new moves registered yet!")

    def reset():
        nonlocal movesG, turnG, btnClick
        for button in buttons:
            button.configure(state='normal')
            button['text'] = ' '

        undobtn.configure(state='normal')
        movesG = 0
        turnG = "X"
        info["text"] = "Current turn: X\n Moves: 0"

    buttons = []
    for i in range(9):
        buttons.append(tk.Button(text=' ', font='forte 20 bold', bg='white', fg='black', height=4, width=8,
                        command=lambda i=i: btnClick(i)))
    k = 0
    for i in range(3, 6):
        for j in range(3):
            buttons[k].grid(row=i, column=j)
            k += 1

    info = tk.Label(text="Current turn: X\n Moves: 0")
    info.grid(row=6, column=2)

    undobtn = tk.Button(text='Undo', font='arial 8', command=undo)

    undobtn.place(x=100, y=434)

    resetbtn = tk.Button(text='Reset', font='arial 8', command=reset)

    resetbtn.place(x=20, y=434)

    tk.mainloop()


def cui():
    running = True
    turnC = "X"
    movesC = 0
    cells = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    win_con = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 4, 8), (2, 4, 6), (0, 3, 6), (1, 4, 7), (2, 5, 8)]
    print("\n\n\n\t\t\t \N{SUPERSCRIPT ONE}|\N{SUPERSCRIPT TWO}|\N{SUPERSCRIPT THREE}\n\t\t\t--+-+--\n\t\t\t \N{SUPERSCRIPT FOUR}|\N{SUPERSCRIPT FIVE}|\N{SUPERSCRIPT SIX}\n\t\t\t--+-+--\n\t\t\t \N{SUPERSCRIPT SEVEN}|\N{SUPERSCRIPT EIGHT}|\N{SUPERSCRIPT NINE}")

    def ask_pos():
        nonlocal turnC, cells, movesC

        try:
            cellID = int(input(f"\nPlease select a position to place a '{turnC}' (1-9): ")) - 1
        except ValueError:
            print("Invalid Input.")
            time.sleep(0.5)
            return

        if cellID > 8 or cellID < 0:
            print("Invalid Input.")
            time.sleep(0.5)
            return
        elif 0 <= cellID <= 8:
            if cells[cellID] == ' ':
                cells[cellID] = turnC
                print(
                    f"\n\n\n\t\t\t {cells[0]}|{cells[1]}|{cells[2]}\n\t\t\t--+-+--\n\t\t\t {cells[3]}|{cells[4]}|{cells[5]}\n\t\t\t--+-+--\n\t\t\t {cells[6]}|{cells[7]}|{cells[8]}")
                if turnC == "X":
                    turnC = "O"
                elif turnC == "O":
                    turnC = "X"
                scan()
                movesC += 1
            else:
                print("That cell is already filled.\n")
                time.sleep(0.5)
                return

    def scan():
        nonlocal cells, running, movesC, win_con
        
        winner = ""
        for con in win_con:
            i, j, k = con
            if(cells[i] == cells[j] == cells[k] != " "):
                winner = cells[i] 
                break

        if (winner == "X"):
            print('''
   _  __             _               __
  | |/ /   _      __(_)___  _____   / /
  |   /   | | /| / / / __ \/ ___/  / / 
 /   |    | |/ |/ / / / / (__  )  /_/  
/_/|_|    |__/|__/_/_/ /_/____/  (_)   
                                       
                            
            ''')
            running = False
        elif (winner == "O"):
            print('''
   ____              _               __
  / __ \   _      __(_)___  _____   / /
 / / / /  | | /| / / / __ \/ ___/  / / 
/ /_/ /   | |/ |/ / / / / (__  )  /_/  
\____/    |__/|__/_/_/ /_/____/  (_)   
                                       
           
            ''')
            running = False
        elif movesC == 8:
            print("\nIt's a Tie!")
            running = False

    while running:
        ask_pos()


def main():
    print('''
 _____ _                _____                    _____          
|_   _(_) ___          |_   _|_ _  ___          |_   _|__   ___ 
  | | | |/ __|  _____    | |/ _` |/ __|  _____    | |/ _ \ / _ |
  | | | | (__  |_____|   | | (_| | (__  |_____|   | | (_) |  __/
  |_| |_|\___|           |_|\__,_|\___|           |_|\___/ \___|
                                                                

    ''')
    print(
        "Hello! Welcome to Tic - Tac - Toe (This program is created by Pranay Sinha)\n\n"
        "Tic-tac-toe, noughts and crosses, or Xs and Os is a paper-and-pencil game for two players, X and O, \n"
        "who take turns marking the spaces in a 3×3 grid. The player who succeeds in placing three of their marks in \n"
        "a horizontal, vertical, or diagonal row wins the game.\n\nWhich version would you like to play?\n\t1. "
        "Character user interface ("
        "CUI)- This version is played in the IDLE itself.\n\t2. Graphical user interface (GUI) - This version will "
        "be played on a new window containing buttons.")
    
    while True:
        try:
            ver = int(input("\n\nEnter '1' for CUI, '2' for GUI or '0' to close the program: "))
        except ValueError:
            print("Invalid Input.")
            time.sleep(2)
            
        if ver == 1:
                cui()
                time.sleep(1.5)
        elif ver == 2:
            gui()
            exit()
        elif ver == 0:
            exit()
        else:
            print("Invalid Input.")
            time.sleep(2)



if __name__ == "__main__":
    main()
