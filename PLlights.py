from tkinter import *

class WhiteorRed:

    def __init__(self):
        window = Tk()
        window.title('White or Red Lights')

        frame = Frame(window)
        frame.pack()

        self.color = StringVar()

        radio_red = Radiobutton(frame, text="Red", bg="red", variable=self.color, value="R", command = self.changecolors)
        radio_red.grid(row=10, column=1)

        radio_white = Radiobutton(frame, text="White", bg="White", variable=self.color, value="W", command = self.changecolors)               
        radio_white.grid(row = 10, column = 2)

        self.canvas = Canvas(window, width = 450, height = 300, bg = "white")
        self.canvas.pack()

        self.oval_one = self.canvas.create_oval(10, 10, 110, 110, fill = "white"
        )
        self.oval_two = self.canvas.create_oval(120, 10, 220, 110, fill = "white"
        )
        self.oval_three = self.canvas.create_oval(230, 10, 330, 110, fill ="white")

        self.color.set('R')
        self.canvas.itemconfig(self.oval_one, fill ="red")

        window.mainloop()

    def changecolors(self):
        color = self.color.get()

        if color == 'R':
            self.canvas.itemconfig(self.oval_one, fill = "red")
            self.canvas.itemconfig(self.oval_two, fill = "red")
            self.canvas.itemconfig(self.oval_three, fill = "red")

        elif color == 'W':
            self.canvas.itemconfig(self.oval_one, fill = "white")
            self.canvas.itemconfig(self.oval_two, fill = "white")
            self.canvas.itemconfig(self.oval_three, fill = "white")


WhiteorRed()


