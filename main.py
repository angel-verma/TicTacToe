import tkinter.messagebox
from tkinter import*

root = Tk()
root.geometry("1350x700+0+0")
root.title("Tic Tac Toe")
root.configure(background='Cadet Blue')

tops = Frame(root, bg='Cadet Blue', pady=2,
             width=1200, height=100, relief=RIDGE)
tops.grid(row=0, column=0)
lblTitle = Label(tops, font="arial 50 bold", text="Tic Tac Toe Game",
                 bd=20, bg='Cadet Blue', fg='Cornsilk', justify=CENTER,)
lblTitle.grid(row=0, column=0)


mainFrame = Frame(root, bg='Cadet Blue', pady=2,
                  width=1200, height=600, relief=RIDGE)
mainFrame.grid(row=1, column=0)

leftFrame = Frame(mainFrame, bd=10, bg='Cadet Blue', pady=2, padx=10,
                  width=750, height=500, relief=RIDGE)
leftFrame.pack(side=LEFT)

rightFrame = Frame(mainFrame, bg='Cadet Blue', pady=2,
                   width=600, height=500, relief=RIDGE, bd=10)
rightFrame.pack(side=RIGHT)

rightFrame1 = Frame(rightFrame, bg='Cadet Blue', pady=2,
                    width=600, height=250, relief=RIDGE, bd=10)
rightFrame1.grid(row=0, column=0)

rightFrame2 = Frame(rightFrame, bg='Cadet Blue', pady=2,
                    width=600, height=250, relief=RIDGE, bd=10)
rightFrame2.grid(row=1, column=0)


# variables
playerX = IntVar()
player0 = IntVar()

playerX.set(0)
player0.set(0)

buttons = StringVar()
click = TRUE


def checker(buttons):
    global click
    if buttons["text"] == "" and click == TRUE:
        buttons["text"] = "X"
        click = FALSE
        score()
    elif buttons["text"] == "" and click == FALSE:
        buttons["text"] = "0"
        click = TRUE
        score()


def score():
    if (btn1["text"] == "X" and btn2["text"] == "X" and btn3["text"] == "X"):
        btn1.configure(background="powder blue")
        btn2.configure(background="powder blue")
        btn3.configure(background="powder blue")
        n = float(playerX.get())
        score = (n+1)
        playerX.set(score)
        tkinter.messagebox.showerror("Winner X", "You Won")

    if (btn4["text"] == "X" and btn5["text"] == "X" and btn6["text"] == "X"):
        btn4.configure(background="powder blue")
        btn5.configure(background="powder blue")
        btn6.configure(background="powder blue")
        n = float(playerX.get())
        score = (n+1)
        playerX.set(score)
        tkinter.messagebox.showerror("Winner X", "You Won")

    if (btn7["text"] == "X" and btn8["text"] == "X" and btn9["text"] == "X"):
        btn7.configure(background="powder blue")
        btn8.configure(background="powder blue")
        btn9.configure(background="powder blue")
        n = float(playerX.get())
        score = (n+1)
        playerX.set(score)
        tkinter.messagebox.showerror("Winner X", "You Won")

    if (btn1["text"] == "X" and btn5["text"] == "X" and btn9["text"] == "X"):
        btn1.configure(background="powder blue")
        btn5.configure(background="powder blue")
        btn9.configure(background="powder blue")
        n = float(playerX.get())
        score = (n+1)
        playerX.set(score)
        tkinter.messagebox.showerror("Winner X", "You Won")

    if (btn3["text"] == "X" and btn5["text"] == "X" and btn7["text"] == "X"):
        btn3.configure(background="powder blue")
        btn5.configure(background="powder blue")
        btn7.configure(background="powder blue")
        n = float(playerX.get())
        score = (n+1)
        playerX.set(score)
        tkinter.messagebox.showerror("Winner X", "You Won")

    if (btn1["text"] == "X" and btn4["text"] == "X" and btn7["text"] == "X"):
        btn1.configure(background="powder blue")
        btn4.configure(background="powder blue")
        btn7.configure(background="powder blue")
        n = float(playerX.get())
        score = (n+1)
        playerX.set(score)
        tkinter.messagebox.showerror("Winner X", "You Won")

    if (btn2["text"] == "X" and btn5["text"] == "X" and btn8["text"] == "X"):
        btn2.configure(background="powder blue")
        btn5.configure(background="powder blue")
        btn8.configure(background="powder blue")
        n = float(playerX.get())
        score = (n+1)
        playerX.set(score)
        tkinter.messagebox.showerror("Winner X", "You Won")

    if (btn3["text"] == "X" and btn6["text"] == "X" and btn9["text"] == "X"):
        btn3.configure(background="powder blue")
        btn6.configure(background="powder blue")
        btn9.configure(background="powder blue")
        n = float(playerX.get())
        score = (n+1)
        playerX.set(score)
        tkinter.messagebox.showerror("Winner X", "You Won")


# ---------------------------------------------------------------------------------------------
    if (btn1["text"] == "0" and btn2["text"] == "0" and btn3["text"] == "0"):
        btn1.configure(background="powder blue")
        btn2.configure(background="powder blue")
        btn3.configure(background="powder blue")
        n = float(player0.get())
        score = (n+1)
        player0.set(score)
        tkinter.messagebox.showerror("Winner 0", "You Won")

    if (btn4["text"] == "0" and btn5["text"]=="0" and btn6["text"]=="0"):
        btn4.configure(background="powder blue")
        btn5.configure(background="powder blue")
        btn6.configure(background="powder blue")
        n = float(player0.get())
        score = (n+1)
        player0.set(score)
        tkinter.messagebox.showerror("Winner 0", "You Won")

    if (btn7["text"] == "0" and btn8["text"]=="0" and btn9["text"]=="0"):
        btn7.configure(background="powder blue")
        btn8.configure(background="powder blue")
        btn9.configure(background="powder blue")
        n = float(player0.get())
        score = (n+1)
        player0.set(score)
        tkinter.messagebox.showerror("Winner 0", "You Won")

    if (btn1["text"] == "0" and btn5["text"]=="0" and btn9["text"]=="0"):
        btn1.configure(background="powder blue")
        btn5.configure(background="powder blue")
        btn9.configure(background="powder blue")
        n = float(player0.get())
        score = (n+1)
        player0.set(score)
        tkinter.messagebox.showerror("Winner 0", "You Won")

    if (btn3["text"] == "0" and btn5["text"]=="0" and btn7["text"]=="0"):
        btn3.configure(background="powder blue")
        btn5.configure(background="powder blue")
        btn7.configure(background="powder blue")
        n = float(player0.get())
        score = (n+1)
        player0.set(score)
        tkinter.messagebox.showerror("Winner 0", "You Won")

    if (btn1["text"] == "0" and btn4["text"]=="0" and btn7["text"]=="0"):
        btn1.configure(background="powder blue")
        btn4.configure(background="powder blue")
        btn7.configure(background="powder blue")
        n = float(player0.get())
        score = (n+1)
        player0.set(score)
        tkinter.messagebox.showerror("Winner 0", "You Won")

    if (btn2["text"] == "0" and btn5["text"]=="0" and btn8["text"]=="0"):
        btn2.configure(background="powder blue")
        btn5.configure(background="powder blue")
        btn8.configure(background="powder blue")
        n = float(player0.get())
        score = (n+1)
        player0.set(score)
        tkinter.messagebox.showerror("Winner 0", "You Won")

    if (btn3["text"] == "0" and btn6["text"]=="0" and btn9["text"]=="0"):
        btn3.configure(background="powder blue")
        btn6.configure(background="powder blue")
        btn9.configure(background="powder blue")
        n = float(player0.get())
        score = (n+1)
        player0.set(score)
        tkinter.messagebox.showerror("Winner 0", "You Won")
# ---------------------------------------------------------------------------------------------


def reset():
    btn1["text"] = ""
    btn2["text"] = ""
    btn3["text"] = ""
    btn4["text"] = ""
    btn5["text"] = ""
    btn6["text"] = ""
    btn7["text"] = ""
    btn8["text"] = ""
    btn9["text"] = ""

    btn1.configure(bg="gainsboro")
    btn2.configure(bg="gainsboro")
    btn3.configure(bg="gainsboro")
    btn4.configure(bg="gainsboro")
    btn5.configure(bg="gainsboro")
    btn6.configure(bg="gainsboro")
    btn7.configure(bg="gainsboro")
    btn8.configure(bg="gainsboro")
    btn9.configure(bg="gainsboro")


def newGame():
    reset()
    playerX.set(0)
    player0.set(0)


lblPlayerX = Label(rightFrame1, font="arial 30 bold", text="PlayerX :",
                   bd=20, bg='Cadet Blue')
lblPlayerX.grid(row=0, column=0, sticky=W)
txtPlayerX = Entry(rightFrame1, font="arial 30 bold", bd=2,
                   fg="black", textvariable=playerX, width=14, justify=LEFT)
txtPlayerX.grid(row=0, column=1)

lblPlayer0 = Label(rightFrame1, font="arial 30 bold", text="Player0 :",
                   bd=20, bg='Cadet Blue')
lblPlayer0.grid(row=1, column=0, sticky=W)
txtPlayer0 = Entry(rightFrame1, font="arial 30 bold", bd=2,
                   fg="black", textvariable=player0, width=14, justify=LEFT)
txtPlayer0.grid(row=1, column=1)

# button
btn1 = Button(leftFrame, text="", font="times 26 bold",
              height=3, width=8, bg='gainsboro', command=lambda: checker(btn1))
btn1.grid(row=1, column=0, sticky=S+N+E+W)

btn2 = Button(leftFrame, text="", font="times 26 bold",
              height=3, width=8, bg='gainsboro', command=lambda: checker(btn2))
btn2.grid(row=1, column=1, sticky=S+N+E+W)

btn3 = Button(leftFrame, text="", font="times 26 bold",
              height=3, width=8, bg='gainsboro', command=lambda: checker(btn3))
btn3.grid(row=1, column=2, sticky=S+N+E+W)

btn4 = Button(leftFrame, text="", font="times 26 bold",
              height=3, width=8, bg='gainsboro', command=lambda: checker(btn4))
btn4.grid(row=2, column=0, sticky=S+N+E+W)

btn5 = Button(leftFrame, text="", font="times 26 bold",
              height=3, width=8, bg='gainsboro', command=lambda: checker(btn5))
btn5.grid(row=2, column=1, sticky=S+N+E+W)

btn6 = Button(leftFrame, text="", font="times 26 bold",
              height=3, width=8, bg='gainsboro', command=lambda: checker(btn6))
btn6.grid(row=2, column=2, sticky=S+N+E+W)

btn7 = Button(leftFrame, text="", font="times 26 bold",
              height=3, width=8, bg='gainsboro', command=lambda: checker(btn7))
btn7.grid(row=3, column=0, sticky=S+N+E+W)

btn8 = Button(leftFrame, text="", font="times 26 bold",
              height=3, width=8, bg='gainsboro', command=lambda: checker(btn8))
btn8.grid(row=3, column=1, sticky=S+N+E+W)

btn9 = Button(leftFrame, text="", font="times 26 bold",
              height=3, width=8, bg='gainsboro', command=lambda: checker(btn9))
btn9.grid(row=3, column=2, sticky=S+N+E+W)

# button right
btnReset = Button(rightFrame2, text="Reset", font="times 16 bold",
                  height=2, width=20, bg='gainsboro', command=reset)
btnReset.grid(row=1, column=0, sticky=S+N+E+W)

btnNewGame = Button(rightFrame2, text="New Game", font="times 16 bold",
                    height=2, width=20, bg='gainsboro', command=newGame)
btnNewGame.grid(row=2, column=0, sticky=S+N+E+W)

root.mainloop()
