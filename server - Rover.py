import socket

host="192.168.4.1" #Brug raspberryens ip
portInput=input("Skriv den port som server skal lytte på: ") # den port man vil lytte på
port = int(portInput)


print("Host ip adresse er", host)
print("server lytter på port", str(port))

skt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
skt.bind((host,port))


while True:
    data, adresse = skt.recvfrom(64)
        
    dekodet_data = str(data.decode("UTF-8"))
        
    if dekodet_data != "q":
        print("Fra klienten: ", str(dekodet_data))
    elif dekodet_data == "q":
        print("Slut")
        break


    
    


    
    

    




