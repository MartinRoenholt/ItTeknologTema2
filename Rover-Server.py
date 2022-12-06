import socket
import RPi.GPIO as G
import RoverFunktioner as RoverFunk
host="192.168.4.1" #Brug raspberryens ip
portInput=input("Skriv den port som server skal lytte på: ") # den port man vil lytte på
port = int(portInput)

print("Host ip adresse er", host) #printer host ip adressen på terminalen
print("server lytter på port", str(port)) #printer porten man lytter på

skt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #definere socket som en variable
skt.bind((host,port)) #binder host ip adressen og porten til socket.
"""
16 = Venstre bagud
20 = Venstre fremad
21 = Højre bagud
26 = Højre fremad

"""
pins = (16, 20, 21, 26)
G.setmode(G.BCM)
G.setup(pins, G.OUT)
v1 = G.PWM(pins[0],100)
v2 = G.PWM(pins[1],100)
v3 = G.PWM(pins[2],100)
v4 = G.PWM(pins[3],100)
while True:
    data, adresse = skt.recvfrom(64)
        
    dekodet_data = str(data.decode("UTF-8"))
        
    if dekodet_data == "frem":
        RoverFunk.frem()

    if dekodet_data == "bag":
        RoverFunk.bag()

    if dekodet_data == "venstre":
        RoverFunk.venstre()

    if dekodet_data == "højre":
        RoverFunk.højre()

    if dekodet_data == "fremVenstre":
        RoverFunk.fremV()

    if dekodet_data == "fremHøjre":
        RoverFunk.fremH()

    if dekodet_data == "bagVenstre":
        RoverFunk.bagV()

    if dekodet_data == "bagHøjre":
        RoverFunk.bagH()

    if dekodet_data == "kill":
        print("Slut")
        break

    elif dekodet_data == "stop":
        v1.ChangeDutyCycle(0)
        v2.ChangeDutyCycle(0)
        v3.ChangeDutyCycle(0)
        v4.ChangeDutyCycle(0)