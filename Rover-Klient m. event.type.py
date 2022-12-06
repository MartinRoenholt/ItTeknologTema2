import socket, pygame                                   #Importering af moduler
import time as T

print("Kører klienten\n")                               #melding om at vi starter klient

skt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  #Definere socket i en variable så det gør den lettere at bruge

host = input("Skriv serverens ip adresse: ")            #Ber om input til serverens ip adresse
portInput = input("Skriv port som server lytter på: ")  #Ber om input til serverens port
port = int(portInput)                                   #Omdanner port inputtet fra string til integer, så det kan bruges

pygame.init()                                           #Starter pygame
screen = pygame.display.set_mode((100,50))              #Opsætter en lille skærm
runLoop = True                                          #Definere en kill variable

delay=0.05                                              #Definere et delay i en variable til senere brug

while runLoop:                                          #Programmet primære funktion
    #pygame.event.clear(pump=True)
    events = pygame.event.get()
    for event in events:
        
        
        if event.type == pygame.QUIT:
            runLoop = False
        
        elif event.type in [pygame.KEYDOWN]:
            if event.key == pygame.K_w:
                data = "frem"
                indkodet_data = data.encode("UTF-8")	# Indkoder data til UTF-8
                skt.sendto(indkodet_data, (host, port))

            elif event.key == pygame.K_s:
                data = "bag"
                indkodet_data = data.encode("UTF-8")	# Indkoder data til UTF-8
                skt.sendto(indkodet_data, (host, port))
                
            elif event.key == pygame.K_a:
                data = "venstre"
                indkodet_data = data.encode("UTF-8")	# Indkoder data til UTF-8
                skt.sendto(indkodet_data, (host, port))
                
            elif event.key == pygame.K_d:
                data = "hoejre"
                indkodet_data = data.encode("UTF-8")	# Indkoder data til UTF-8
                skt.sendto(indkodet_data, (host, port))
            
            elif event.key == pygame.K_x:
                data = "stop"
                indkodet_data = data.encode("UTF-8")	# Indkoder data til UTF-8
                skt.sendto(indkodet_data, (host, port))
            

data="kill"
indkodet_data = data.encode("UTF-8")
skt.sendto(indkodet_data, (host, port))
skt.close() # Lukker forbindelse
print("Socketen blev lukket")