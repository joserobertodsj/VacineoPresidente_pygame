#import os, sys

#dirpath = os.getcwd()
#sys.path.append(dirpath)

#if getattr(sys, "frozen", False):
    #os.chdir(sys._MEIPASS)



import pygame
import random

from pygame import image


from nurse import Nurse
from virus import Virus
from vaccine import Vaccine
from bolsonaro import Bolsonaro


#inicializando o pygame e criando a janela
pygame.init()
display = pygame.display.set_mode([840, 480])
pygame.display.set_caption("Virus Combat")

#Groups
ObjectsGroup = pygame.sprite.Group()
VirusGroup = pygame.sprite.Group()
BolsonaroGroup = pygame.sprite.Group()
VaccineGroup = pygame.sprite.Group()




#Backgroud
bg = pygame.sprite.Sprite(ObjectsGroup)
bg.image = pygame.image.load("data/bg.jpeg")
bg.image = pygame.transform.scale(bg.image, [840, 480])
bg.rect = bg.image.get_rect()



nurse = Nurse(ObjectsGroup)
virus= Virus(ObjectsGroup)
vaccine = Vaccine(ObjectsGroup)
bolsonaro = Bolsonaro(ObjectsGroup)



#music
pygame.mixer.music.load("data/musicafundo.mpeg")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)


#sound
seringa = pygame.mixer.Sound("data/Vacina.wav")
cloroquina = pygame.mixer.Sound("data/cloroquina.wav")
fimdejogo = pygame.mixer.Sound("data/GameOver.wav")

gameloop = True
gameover = False

timer = 10
clock = pygame.time.Clock()

if __name__ == "__main__":
    while gameloop:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameloop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not gameover:
                    seringa.play()
                    newVaccine = Vaccine(ObjectsGroup, VaccineGroup)
                    newVaccine.rect.center = nurse.rect.center 

            

        #Update Logic
        if not gameover:

            ObjectsGroup.update()

            timer +=1
            if timer > 20:
                timer = 0
                if random.random() < 0.3:
                    newVirus = Virus(ObjectsGroup, VirusGroup)
                elif random.random() < 0.05:
                    newBolsonaro = Bolsonaro(ObjectsGroup, BolsonaroGroup) and cloroquina.play()
                    
            collisions = pygame.sprite.spritecollide(nurse, VirusGroup, False)
            collisions2 = pygame.sprite.spritecollide(nurse, BolsonaroGroup, False)

            if collisions or collisions2: 
                GO = pygame.sprite.Sprite(ObjectsGroup)
                GO.image = pygame.image.load("data/fimdejogo.png")
                GO.image = pygame.transform.scale(GO.image, [840,480])
                GO.rect = bg.image.get_rect()
                pygame.mixer.music.stop()
                fimdejogo.play()
                gameover = True
        
            hits = pygame.sprite.groupcollide (VaccineGroup, VirusGroup, True, True)
            hits2 = pygame.sprite.groupcollide (VaccineGroup, BolsonaroGroup, True, True)

        # Draw:
        display.fill([46, 46, 46])
        ObjectsGroup.draw(display)
        pygame.display.update()


