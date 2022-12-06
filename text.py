import pygame 
pygame.font.init()
Retning=""
screen=pygame.display.set_mode((500,500))
screen.fill((0,0,0))

x=100
y=100
color=(255,255,255)
textfont=pygame.font.SysFont('freesansbold.ttf', 32)
a=True
while a:
    screen.fill((0,0,0))
    pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            a=False
        
        if pressed[pygame.K_w]:
            print("Fremad")
            Retning="Der køres fremad"
     
        if pressed[pygame.K_s]:
            print("Bagud")
            Retning="Der køres bagud"
            
    textTBD=textfont.render(Retning,1,color)
    screen.blit(textTBD,(x,y))
    pygame.display.update() 
    pygame.display.flip()
