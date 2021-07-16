import sys
sys.path.append('/usr/local/lib/python3.9/site-packages')
import getch

from easytello import tello

drone=tello.Tello()

distance=int(input("how many cenitimeters would you like your drone to move each time a key is pressed?"))

angledegree=int(input("how many degrees do you want your drone to turn?"))

flying=True

drone.takeoff()

while flying==True:
    key=getch.getch()
    if key=="w":
        drone.forward(distance)
    elif key=="s":
        drone.back(distance)
    elif key=="a":
        drone.left(distance)
    elif key=="d":
        drone.right(distance)
    elif key==" ":
        drone.up(distance)
    elif key=="c":
        drone.down(distance)
    elif key=="q":
        drone.ccw(angledegree)
    elif key=="e":
        drone.cw(angledegree)
    elif key==".":
        drone.land()
    elif key ==",":
        drone.takeoff()
    elif key=="p":
        drone.land()
        flying=False
    elif key=="y":
        newdistance=int(input("what would you like to change your new distance to?"))
        distance=newdistance
    elif key=="u":
        newangledegree=int(input("what would you like to have for your new angle degree?"))
        angledegree=newangledegree
