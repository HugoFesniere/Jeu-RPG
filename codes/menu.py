# on importe les modules dont on a besoin pour coder le menu
import pygame, sys
from histoire import window_storie
from game import Game
mainClock = pygame.time.Clock()
from pygame.locals import *
#on initialise pygame
pygame.init()
# on creer une fenêtre ou le menu sera afficher et on lui donne le nom de notre jeu
pygame.display.set_caption('Projet RPG')
#on creer une variable "screen " ou l'on peut choisir la taille chosisit la taille de notre fenêtre 
screen = pygame.display.set_mode((500, 500), 0, 32)
font = pygame.font.SysFont(None, 20)

''' on créer une fonction "draw text" qui nous permettra d'afficher du texte sur notre fenêtre
 on impose des paramètres qui correspondent : au choix du texte,  l'emplacement , la taille, la couleur du texte  '''
 
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

click = False

# on crée notre fonction principale menu
def main_menu():
    while True :

        screen.fill((0,0,0))                                            # on se sert de la fontion draw_text pour vouloir afficher tout ce qui est textuel dans la fenêtre du menu
        draw_text('main menu', font, (255,255,255), screen, 20, 20)   
        draw_text('new game', font, (255,255,255), screen, 20, 80)      # on chosis la même couleur pour le soin d'esthétisme et on ne modifie que le y pour l'emplacement du texte (pour eviter la superposition)
        draw_text('credits', font, (255,255,255), screen, 20, 180)
        draw_text('quit', font, (255,255,255), screen, 20, 280)
        

        mx, my = pygame.mouse.get_pos()

        # nos bouttons etant de forme rectangle, on choisit la hauteur, largeur, longeur et l'opacité du boutton

        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)
        button_3 = pygame.Rect(50 ,300, 200, 50)
        
        # à chaque fois qu'on appuie sur un boutton cela va faire appel à une fonction qui lui est propre 
        if button_1.collidepoint((mx, my)):
            if click :
                launch = Game()
                launch.run()
                
        if button_2.collidepoint((mx, my)):
            if click :
                credits()
               
        if button_3.collidepoint((mx, my)):
            if click :
                quit_the_game()


        # nos bouttons ont étés crées au-dessus mais maintenant il faut pouvoir les afficher et choisir leur couleur 
        # on veut les afficher sur notre fenêtre, on se sert de la variable screen créee au début
        # pour la couleur, on se sert du spectre rgb
        pygame.draw.rect(screen, (150, 0, 205), button_1)
        pygame.draw.rect(screen, (164, 66, 220), button_2)
        pygame.draw.rect(screen, (181, 100, 227), button_3)

        ''' concernant notre fenêtre, si l'utlisateur clique sur un boutton, l'action qui lui est associé va se lancer,
        toutefois il va pouvoir revenir en arrière (c'est à dire à l'affichage du menu ) avec la touche echap'''
        click = False
        for event in pygame.event.get():
            if event.type == QUIT :
                pygame.quit()
                sys.exit
            if event.type == KEYDOWN :
                if event.key == K_ESCAPE:
                    pygame.quit ()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN :
                if event.button == 1 :
                    click = True

        pygame.display.update()
        mainClock.tick(60)

# dans cette partie on creer une fonction pour chaque boutton qu'on a crée


''' la fonction credit nous permet de voir toutes les personnes qui ont participer à la création du jeu;
lorque l'on clique dessus cela ouvre une nouvelle fenetre credits et on ne voit plus la fenetre du menu principale'''
def credits():
    running = True
    while running :
        screen.fill((0, 0, 0))
        draw_text('Raphaël LOUISON', font, (255, 255, 255), screen, 20, 20)
        draw_text('Hugo FESNIERE', font, (255, 255, 255), screen, 20, 50)
        draw_text('Gustave CONSTANS', font, (255, 255, 255), screen, 20, 80)
        draw_text('Phara MILLAURIAUX', font, (255, 255, 255), screen, 20, 110)
        draw_text('Maxime AIT ADDA', font, (255, 255, 255), screen, 20, 140)
        for event in pygame.event.get():
            if event.type == QUIT :
                pygame.quit()
                sys.exit
            if event.type == KEYDOWN :
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)
        
# la fonction quit_the_game doit permettre de quitter notre jeu lorqu'on clique dessus
def quit_the_game():
    pygame.quit()
    sys.exit