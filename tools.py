import tkinter as tk
window = tk.Tk()

'''

exec(open('/home/quantum/Desktop/git_repo/kicad/tools.py').read())

'''

def align():
    print("Align")

def align90():
    print("Align 90")

button01 = tk.Button(
    text    = "Align",
    width   = 25,
    height  = 5,
    bg      = "yellow",
    fg      = "black",
    command = align
)

button02 = tk.Button(
    text    = "Align90",
    width   = 25,
    height  = 5,
    bg      = "black",
    fg      = "yellow",
    command = align90
)

button01.pack()
button02.pack()
window.mainloop()
