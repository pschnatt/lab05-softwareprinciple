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

class Pole(object):
  def __init__(self,name="",xpos=0,ypos=0,thick=10,length=100):
    self.pname = name
    self.stack = []
    self.toppos = 0
    self.pxpos = xpos
    self.pypos = ypos
    self.pthick = thick
    self.plength = length

  def showpole(self):
    t.penup()
    t.goto(self.pxpos,self.pypos)
    t.pendown()
    t.fd(self.pthick / 2)
    t.lt(90)
    t.fd(self.plength)
    t.lt(90)
    t.fd(self.pthick)
    t.lt(90)
    t.fd(self.plength)
    t.lt(90)
    t.fd(self.pthick / 2)
    
  def pushdisk(self, disk):
    if (disk.dheight * self.toppos >= self.plength):
      return
    disk.cleardisk()
    disk.newpos(self.pxpos,self.pypos + disk.dheight * self.toppos)
    disk.showdisk()

  def popdisk(self):
    if (self.toppos > 0):
      disk = self.stack.pop()
      position = disk.dheight * (len(self.toppos) - 1)
      self.toppos -= 1
      disk.cleardisk()
      disk.newpos(self.pxpos,self.pypos + self.plength + 20)
      disk.showdisk()


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
            t.fd(self.dwidth)
            t.left(90)
            t.fd(self.dheight)
            t.left(90)
        t.fd(100)

        t.end_fill()

    def newpos(self, x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()
        self.dxpos, self.dypos = x, y

    def cleardisk(self):
        t.clear()
        t.setheading(0)

        t.penup()
        t.goto(self.dxpos, self.dypos)
        t.pendown()

        t.fillcolor("grey")
        t.begin_fill()
        for _ in range(2):
            t.fd(self.dwidth)
            t.left(90)
            t.fd(self.dheight)
            t.left(90)
        t.fd(100)

        t.end_fill()

h = Hanoi()
h.solve()