""" Clic per seconde"""
import pygame
import time
pygame.init()
longueur, largeur = 500,500
canya = pygame.display.set_mode((longueur,largeur))
pygame.display.set_caption("Clic per seconde By @Canihel:)")
clock = pygame.time.Clock()
#police
font = pygame.font.Font(None, 64)
#texte
text = font.render("Clic counter !", True, (250,250,250))
#nombre de clic
clic = 0
clic2 =0
#temps
start = time.time()
chrono_start = time.time()
H,M,S = str(0),str(0),str(0)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            clic = clic + 1
            clic2 = clic2 + 1

    instant_time = time.time()
    last = int((instant_time - start))
    if last == 1 :
        clic2 = clic2
    elif last > 1 :
        clic2 = 0
        start = time.time()

    #chronomètre
    chrono_instant = time.time()
    chrono_last =int(chrono_instant - chrono_start)
    #seconde, minute, heure
    S = str((chrono_last % 60))
    M = str((chrono_last % 3600)//60)
    H = str(chrono_last //3600)
    if (int(S)<10):
        S='0'+S
    if (int(M)<10):
        M='0'+M
    if (int(H)<10):
        H='0'+H


    CPS =font.render("CPS :"+str(clic2), True, (0, 250, 250))
    count = font.render("Count : "+str(clic), True, (0, 0, 250))
    chrono = font.render("Time = "+H+" : "+M+" : "+S , True, (250, 50, 0))
    canya.fill((0,0,0))
    canya.blit(text, (100, 0))
    canya.blit(count,(0,64))
    canya.blit(CPS, (0, 128))
    canya.blit(chrono , (0,192))

    pygame.display.flip()