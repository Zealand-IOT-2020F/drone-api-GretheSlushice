import socket

class Drone(object):
    """description of class"""
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.Host = ""
        self.HostPort = 9000
        self.locaddr = (self.Host, self.HostPort)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #self.tello_address = ("192.168.10.1", 8889)
        self.tello_address = (ip, port)
        self.sock.bind(self.locaddr)

    def sendBesked(self,TelloMessage):
        try:   
            print("send message "+ TelloMessage +" end")
            msg = TelloMessage.encode(encoding="utf-8")
            sent = self.sock.sendto(msg, self.tello_address)
            data, server = self.sock.recvfrom(1518)
            #print(data.decode(encoding="utf-8"))

            return "Succes"
        except:
            return "Did not work"

        

    def connect(self):
        print("Forbinder")
        resultat = self.sendBesked("command")
        print(resultat)

    def takeOff(self):
        print("takeOff")
        resultat = self.sendBesked("takeoff")
        print(resultat)

    def forward(self, value):
        print("frem "+value)
        resultat = self.sendBesked("forward "+value)
        print(resultat)

    def back(self, value):
        print("tilbage "+value)
        resultat = self.sendBesked("back "+value)
        print(resultat)
    
    def left(self, value):
        print("venstre "+value)
        resultat = self.sendBesked("left "+value)
        print(resultat)

    def right(self, value):
        print("hojre "+value)
        resultat = self.sendBesked("right "+value)
        print(resultat)

    def land(self):
        print("lander")
        resultat = self.sendBesked("land")
        print(resultat)
    
    def turn_cw(self, value):
        print("drejer med uret "+value)
        resultat = self.sendBesked("cw "+value)
        print(resultat)

    def turn_ccw(self, value):
        print("drejer mod uret "+value)
        resultat = self.sendBesked("ccw"+value)
        print(resultat)

#tello_address = ('192.168.10.1', 8889)
#print ('Tello: command takeoff land flip forward back left right \r\n       up down cw ccw speed speed?\r\n')








