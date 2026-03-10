
"""@Canihel:)
Vas y rejoint mon discord on vas coder des jeux en 2D et faire d'autre truc cool
"""
import random
import time
from xml.etree.ElementTree import canonicalize

import  pygame


#initiation de pygame
pygame.init()
#pour faire apparaître la fenêtre  900 . 700
canya = pygame.display.set_mode ((900,700))
pygame.display.set_caption("@Canihel:) Game")

area = pygame.Rect(350,250,100,100)
area_color = ((250,0,0))


vitesse_y = 0
gravite = 1
est_en_saut = False

x = 0
y = 500
frame =[]
frame_f =[]
#image
cactus = pygame.image.load("image/captus.png").convert_alpha()
cactus_hitbox = cactus.get_rect()

"""animation dino"""
dino = pygame.image.load("image/dinoo.png").convert_alpha()
dino_hitbox = dino.get_rect()

"""Animation frame by frame"""
#initialtion des frames du coup de hache
frames_droit = ['frames/hache0.png','frames/hache1.png','frames/hache2.png','frames/hache3.png']
for _ in frames_droit:
    frame.append(pygame.image.load(_).convert_alpha())

#initialtion des frames de la foudre
frame_light =['frame_f/file_1.png','frame_f/file_2.png','frame_f/file_3.png','frame_f/file_4.png','frame_f/file_5.png','frame_f/file_6.png']
for i in frame_light:
    frame_f.append(pygame.image.load(i).convert_alpha())

clock = pygame.time.Clock()

#son
son_saut = pygame.mixer.Sound("son/saut.wav")
son_universo =  pygame.mixer.Sound("son/universo.wav")
coup_de_haches = pygame.mixer.Sound('son/equip_generic1.wav')
coup_de_foudre = pygame.mixer.Sound('son/thundersfx1sec.wav')

#le décors
dirt_color=((0,250,0))
dirt = pygame.Rect(0, 579, 900, 150)

#couleur
couleur = ['red','blue','yellow','green','pink']

#score
score = 0
font = pygame.font.Font(None, 40)
#texte
text = font.render(str(score), True, (250,250,250))

cactus_x = 900 #obstacle position
t = 0  #variable pour incrémenter les framme de haches
light = 0 #variable pour incrémenter les framme de foudre
animation = False
lighting_release = False
son_intro = False
son_foudre = False
running = True
while running:
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_SPACE] and not est_en_saut:
        vitesse_y  = -10
        est_en_saut = True
        print("'Saut' : détecté")
        #clock.tick(150)

    """saut"""
    if  est_en_saut == True :
        vitesse_y += gravite
        y += vitesse_y
        #print("la touche d'espace est appuyé")
        #clock.tick(150)
        if y >= 442 :
            y= 442
            est_en_saut = False
            vitesse_y = 0
            son_saut.play()
    if pressed[pygame.K_LEFT]:
        x -= 1
        print("x :",x)
       # print("la touche droite est appuyé")

    if pressed[pygame.K_RIGHT]:
        animation = True
        print("'coups de hache':détecté")

    if pressed[pygame.K_UP]:
        y -= 1
        print("y :", y)
       # print("la touche haute est appuyé")


    if pressed[pygame.K_DOWN]:
        y += 1
        print("y :", y)
       # print("la touche bas est appuyé")

    if son_intro == True :
        pass
    else:
        #son_universo.play()
        son_intro = True
    canya.fill((0, 250, 250))
    pygame.draw.rect(canya, dirt_color, dirt)
    cactus_x = cactus_x - 5
    if cactus_x == -50:
        cactus_x =900
    #redéfinition de la position du cube
    obstacle = pygame.Rect(cactus_x, 529, 50, 50)

    choix = random.choice(couleur)

    # pygame.draw.rect(canya, 'black', obstacle)
    dino_hitbox.topleft=(113, y)
    r = cactus_x +10
    h = 529+50-100+10
    cactus_hitbox.topleft=(cactus_x,h)
    canya.blit(cactus, cactus_hitbox.topleft)

    canya.blit(dino, dino_hitbox.topleft)

    # Score
    text = font.render("Score: "+str(score), True, (250, 250, 250))
    score += 1

    #animation de coup de hache et son
    if t == 0 and animation ==True :
        coup_de_haches.stop()
        coup_de_haches.play()
    if animation == True:
        canya.blit(frame[t],(208 , y+15))#-240))
        t +=1
    else:
        canya.blit(frame[0], (208, y +15))#-240))

    if t >=4:
        t = 0
        animation = False

    #animation foudre et son
    """
    mettre ici la partie pour gérer le son 
    
    """



    if lighting_release == True :
        canya.blit(frame_f[light], (-200, 0))  # -240))
        light +=  1

    if light >= 6:
        light = 0
        lighting_release = False


    #affichage des textes
    canya.blit(text, (100, 0))
    canya.blit(cactus,(0,0))
    # en cas de collision
    if dino_hitbox.colliderect(cactus_hitbox):
        print("'collision' : détectée")
        lighting_release = True
        if son_foudre == True:
            pass
        else:
            coup_de_foudre.play()
            son_foudre = True


            #time.sleep(0.5)
        #cactus_x=900
        cactus_x = cactus_x + 5
        score = 0
        #continue

    else :
        lighting_release = False
        son_foudre = False



    pygame.display.flip()
    #if not pressed[pygame.K_SPACE]:
    clock.tick(250)
    #clock.tick()

print("'Jeu' : Fermé")




















