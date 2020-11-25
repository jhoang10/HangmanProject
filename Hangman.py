#import random
#from WordList import wordList

import pygame

#game setup
pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman")


#buttons 
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x,y, chr(A + i)])

#fonts
LETTER_FONT = pygame.font.SysFont('arial', 40)

#hangman pictures used
images = []
#loop cycles through the images for each point in hangman based on pic name
for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)

#stage in where the hangman is
hangmanLife = 0
words = []
words = random.choice(wordlist)
guessed = []

#colors
WHITE = (255,255,255)
BLACK = (0,0,0)

#draw buttons
def draw():
    win.fill(WHITE)
    
    for letter in letters:
        x,y, ltr = letter
        pygame.draw.circle(win, BLACK, (x,y), RADIUS, 3)
        text = LETTER_FONT.render(ltr, 1, BLACK)
        win.blit(text, (x - text.get_width()/2,y - text.get_height()/2))


FPS = 60
clock = pygame.time.Clock()
run = True
    

while run:
    clock.tick(FPS)

    #background color
    win.fill((153, 179, 255))
    win.blit(images[hangmanLife], (100, 100))
    pygame.display.update()
    
    #this event is used to close the application
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
    #taking in position of the mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)

pygame.quit
