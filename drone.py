# from easytello import tello

# my_drone = tello.Tello()

# my_drone.takeoff()

# my_drone.curve(50,50,0,50,-50,0,30)
# my_drone.curve(-50,-50,0,-50,50,0,30)




from easytello import tello

mydrone=tello.Tello()

mydrone.takeoff()

for i in range(4):

    while True:
        tof=int(int(mydrone.get_tof())/10)
        
        if tof>32:
            if tof-30 >= 20:
                mydrone.down(tof-30)
            else:
                mydrone.forward(80)
                break
        elif tof<28:
            mydrone.up(tof)

        else:
            mydrone.forward(80)
            break

mydrone.land()