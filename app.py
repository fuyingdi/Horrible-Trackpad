from tkinter import *

class Root(Tk):
    dots = [[]]
    slots = [[], [], [], [], []]

    class Rect:
        def __init__(self, x1,x2,y1,y2):
            self.x1 = x1
            self.x2 = x2
            self.y1 = y1
            self.y2 = y2
    class Circle:
        def __init__(self, x, y, r):
            self.x = x 
            self.y = y
            self.r = r

    def __init__(self):
        super().__init__()
        self.geometry("233x286")
        self.resizable(False,False)

        self.canvas = Canvas(self, width=233, height=286, bg='black')
        self.num_pad_image = PhotoImage(file="number_pad.png")
        self.canvas.create_image(0,0, image=self.num_pad_image, anchor=NW)
        self.canvas.pack()

    def init_number_pad(self):
        number_pad_slot = [[]]
        number_pad_slot[0].append(Label(self,textvariable="o"))
        for x in number_pad_slot:
            for y in x:
                y.pack()

def run():
    root = Root()
    root.init_number_pad()
    
    root.mainloop()



if __name__ == '__main__':
    run()
