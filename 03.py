import turtle as t

class Disk:
    def __init__(self, name, xpos, ypos, height, width):
        self.dname = name
        self.dxpos = xpos
        self.dypos = ypos
        self.dheight = height
        self.dwidth = width
        self.t = t.Turtle()
        self.t.hideturtle()
        self.t.speed('fastest')

    def draw_disk(self):
        self.t.penup()  # Lift the pen before moving
        self.t.goto(self.dxpos, self.dypos - self.dheight / 2)  # Adjust for the disk's height
        self.t.pendown()
        self.t.begin_fill()
        for _ in range(2):
            self.t.forward(self.dwidth / 2)
            self.t.left(90)
            self.t.forward(self.dheight)
            self.t.left(90)
            self.t.forward(self.dwidth)
            self.t.left(90)
            self.t.forward(self.dheight)
            self.t.left(90)
            self.t.forward(self.dwidth / 2)
        self.t.end_fill()
        self.t.penup()

    def newpos(self, xpos, ypos):
        self.dxpos = xpos
        self.dypos = ypos
        self.draw_disk()

    def cleardisk(self):
        self.t.reset()
        self.t.hideturtle()

class Pole:
    def __init__(self, name, xpos, ypos, thick, length):
        self.pname = name
        self.stack = []
        self.pxpos = xpos
        self.pypos = ypos
        self.pthick = thick
        self.plength = length
        self.t = t.Turtle()
        self.t.hideturtle()
        self.t.speed('fastest')

    def showpole(self):
        self.t.penup()
        self.t.goto(self.pxpos, self.pypos)
        self.t.pendown()
        self.t.forward(self.pthick / 2)
        self.t.left(90)
        self.t.forward(self.plength)
        self.t.left(90)
        self.t.forward(self.pthick)
        self.t.left(90)
        self.t.forward(self.plength)
        self.t.left(90)
        self.t.forward(self.pthick / 2)
        self.t.penup()

    def pushdisk(self, disk):
        disk.cleardisk()  # Clear the disk before moving it
        ypos = self.pypos + len(self.stack) * disk.dheight
        disk.newpos(self.pxpos, ypos)
        self.stack.append(disk)

    def popdisk(self):
        if self.stack:
            disk = self.stack.pop()
            disk.cleardisk()  # Clear the disk before moving it
            return disk
        return None

class Hanoi:
    def __init__(self, n=3, start="A", workspace="B", destination="C"):
        self.startp = Pole(start, -150, -100, 10, 100)
        self.workspacep = Pole(workspace, 0, -100, 10, 100)
        self.destinationp = Pole(destination, 150, -100, 10, 100)
        self.startp.showpole()
        self.workspacep.showpole()
        self.destinationp.showpole()
        for i in range(n):
            disk = Disk("d"+str(i+1), self.startp.pxpos, self.startp.pypos + i*20, 20, (n-i)*30 + 10)
            self.startp.pushdisk(disk)
            disk.draw_disk()

    def move_disk(self, start, destination):
        disk = start.popdisk()
        if disk:
            destination.pushdisk(disk)

    def move_tower(self, n, s, d, w):
        if n == 1:
            self.move_disk(s, d)
        else:
            self.move_tower(n-1, s, w, d)
            self.move_disk(s, d)
            self.move_tower(n-1, w, d, s)

    def solve(self):
        self.move_tower(3, self.startp, self.destinationp, self.workspacep)

# Set up the screen
t.setup(600, 600)
t.title("Tower of Hanoi")
t.bgcolor("white")

# Create and solve the puzzle
h = Hanoi()
h.solve()

# Finish the program
t.done()
