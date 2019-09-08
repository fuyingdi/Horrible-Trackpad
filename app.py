from tkinter import *


if __name__ == '__main__':
    root = Tk()
    root.geometry("233x286")
    root.resizable(False,False)
    canvas = Canvas( width=300, height=200, bg='black')
    canvas.pack(expand=YES, fill=BOTH)
    image = PhotoImage(file="number_pad.png")
    canvas.create_image(0, 0, image=image, anchor=NW)
    root.mainloop()
