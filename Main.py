import Drone
import socket
import time

voresDrone = Drone.Drone("127.0.0.1", 8889)

voresDrone.connect()
time.sleep(2)

voresDrone.takeOff()
time.sleep(2)
print("\n")

for i in range(5):
    print("Lap "+str(i+1))
    voresDrone.forward("20")
    time.sleep(2)

    voresDrone.turn_cw("180")
    time.sleep(2)

    voresDrone.forward("20")
    time.sleep(2)

    voresDrone.turn_cw("180")
    time.sleep(2)
    print("\n")

voresDrone.land()