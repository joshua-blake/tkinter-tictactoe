import tkinter as tk
import random
root = tk.Tk()
root.title("Tic Tac Toe")
def clicked(button):
  options = [b1,b2,b3,b4,b5,b6,b7,b8,b9]
  if button['text'] != "":
    return
  else:
    button.configure(text="O")
    if all([buttons['text'] != "" for buttons in options]):
      next
    else:
      button_chosen = random.choice(options)
      while button_chosen['text'] != "":
        button_chosen = random.choice(options)
      button_chosen.configure(text="X")
  
  if options[0]['text'] == "O" and options[1]['text'] == "O" and options[2]['text'] == "O":
    print("YOU WIN")
    for b in options:
      b.configure(text="")
  elif options[3]['text'] == "O" and options[4]['text'] == "O" and options[5]['text'] == "O":
    print("YOU WIN")
    for b in options:
      b.configure(text="")
  elif options[6]['text'] == "O" and options[7]['text'] == "O" and options[8]['text'] == "O":
    print("YOU WIN")
    for b in options:
      b.configure(text="")
  elif options[0]['text'] == "O" and options[3]['text'] == "O" and options[6]['text'] == "O":
    print("YOU WIN")
    for b in options:
      b.configure(text="")
  elif options[1]['text'] == "O" and options[4]['text'] == "O" and options[7]['text'] == "O":
    print("YOU WIN")
    for b in options:
      b.configure(text="")
  elif options[2]['text'] == "O" and options[5]['text'] == "O" and options[8]['text'] == "O":
    print("YOU WIN")
    for b in options:
      b.configure(text="")
  elif options[1]['text'] == "O" and options[4]['text'] == "O" and options[7]['text'] == "O":
    print("YOU WIN")
    for b in options:
      b.configure(text="")
  elif options[0]['text'] == "O" and options[4]['text'] == "O" and options[8]['text'] == "O":
    print("YOU WIN")
    for b in options:
      b.configure(text="")
  elif options[2]['text'] == "O" and options[4]['text'] == "O" and options[6]['text'] == "O":
    print("YOU WIN")
    for b in options:
      b.configure(text="")

  elif options[0]['text'] == "X" and options[1]['text'] == "X" and options[2]['text'] == "X":
    print("I WIN")
    for b in options:
      b.configure(text="")
  elif options[3]['text'] == "X" and options[4]['text'] == "X" and options[5]['text'] == "X":
    print("I WIN")
    for b in options:
      b.configure(text="")
  elif options[6]['text'] == "X" and options[7]['text'] == "X" and options[8]['text'] == "X":
    print("I WIN")
    for b in options:
      b.configure(text="")
  elif options[0]['text'] == "X" and options[3]['text'] == "X" and options[6]['text'] == "X":
    print("I WIN")
    for b in options:
      b.configure(text="")
  elif options[1]['text'] == "X" and options[4]['text'] == "X" and options[7]['text'] == "X":
    print("I WIN")
    for b in options:
      b.configure(text="")
  elif options[2]['text'] == "X" and options[5]['text'] == "X" and options[8]['text'] == "X":
    print("I WIN")
    for b in options:
      b.configure(text="")
  elif options[1]['text'] == "X" and options[4]['text'] == "X" and options[7]['text'] == "X":
    print("I WIN")
    for b in options:
      b.configure(text="")
  elif options[0]['text'] == "X" and options[4]['text'] == "X" and options[8]['text'] == "X":
    print("I WIN")
    for b in options:
      b.configure(text="")
  elif options[2]['text'] == "X" and options[4]['text'] == "X" and options[6]['text'] == "X":
    print("I WIN")
    for b in options:
      b.configure(text="")
  elif all([buttons['text'] != "" for buttons in options]):
    print("IT'S A TIE")
    for b in options:
      b.configure(text="")

b1 = tk.Button(root, text="", font=("Helvetica", 20), height=3, width=6, command= lambda: clicked(b1))
b2 = tk.Button(root, text="", font=("Helvetica", 20), height=3, width=6, command= lambda: clicked(b2))
b3 = tk.Button(root, text="", font=("Helvetica", 20), height=3, width=6, command= lambda: clicked(b3))
b4 = tk.Button(root, text="", font=("Helvetica", 20), height=3, width=6, command= lambda: clicked(b4))
b5 = tk.Button(root, text="", font=("Helvetica", 20), height=3, width=6, command= lambda: clicked(b5))
b6 = tk.Button(root, text="", font=("Helvetica", 20), height=3, width=6, command= lambda: clicked(b6))
b7 = tk.Button(root, text="", font=("Helvetica", 20), height=3, width=6, command= lambda: clicked(b7))
b8 = tk.Button(root, text="", font=("Helvetica", 20), height=3, width=6, command= lambda: clicked(b8))
b9 = tk.Button(root, text="", font=("Helvetica", 20), height=3, width=6, command= lambda: clicked(b9))

b1.grid(column=0, row=0)
b2.grid(column=1, row=0)
b3.grid(column=2, row=0)
b4.grid(column=0, row=1)
b5.grid(column=1, row=1)
b6.grid(column=2, row=1)
b7.grid(column=0, row=2)
b8.grid(column=1, row=2)
b9.grid(column=2, row=2)
root.mainloop()