import socket, time

print("Kører klienten\n")

skt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

host = input("Skriv serverens ip adresse: ")
portInput = input("Skriv port som server lytter på: ")
port = int(portInput)

print("Serverens ip adresse er:", host)
print("Serveren lytter på port:", str(port))

# Definerer data:
dataListe = ["Mørs", "Jupiter", "Italien", "TCP", "Stol"]

# Sender data
kommando=""
while True:
	kommando = input("skriv et kommando")
	if kommando == "s":
		for data in dataListe:
			print("Sender data:", str(data))
		
			# Indkoder data til UTF-8
			indkodet_data = data.encode("UTF-8")	
			skt.sendto(indkodet_data, (host, port))
   
			time.sleep(0.001)
	if kommando == "q":
		data="q"
		indkodet_data = data.encode("UTF-8")
		skt.sendto(indkodet_data, (host, port))	
		skt.close() # Lukker forbindelse
		print("Socketen blev lukket")
		break
