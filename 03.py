import turtle as t

class Hanoi(object):
    def __init__(self, n=3, start="A", workspace="B", destination="C"):
        self.startp = Pole(start, 0, 0)
        self.workspacep = Pole(workspace, 150, 0)
        self.destinationp = Pole(destination, 300, 0)
        self.startp.showpole()
        self.workspacep.showpole()
        self.destinationp.showpole()
        for i in range(n):
            self.startp.pushdisk(Disk("d"+str(i), 0, i*150, 20, (n-i)*30))

    def move_disk(self, start, destination):
        disk = start.popdisk()
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

class Disk(object):
    def __init__(self, name="", xpos=0, ypos=0, height=20, width=40):
        self.dname = name
        self.dxpos = xpos
        self.dypos = ypos
        self.dheight = height
        self.dwidth = width

    def showdisk(self):
        t.pensize(2)
        t.speed(0)
        t.pendown()
        t.fillcolor("grey")
        t.begin_fill()

        for _ in range(2):
            t.fd(200)
            t.left(90)
            t.fd(30)
            t.left(90)
        t.fd(100)

        t.end_fill()

    def newpos(self, x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()
        self.dxpos, self.dypos = x, y

    def cleardisk(self):
        # Precondition: Turtle must face east
        t.clear()
        t.setheading(0)

        # Move to the current position of the disk
        t.penup()
        t.goto(self.dxpos, self.dypos)
        t.pendown()

        # Clear the disk
        t.fillcolor("grey")
        t.begin_fill()
        for _ in range(2):
            t.fd(200)
            t.left(90)
            t.fd(30)
            t.left(90)
        t.fd(100)

        t.end_fill()

h = Hanoi()
h.solve()