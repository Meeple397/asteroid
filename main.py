import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get(): #must be begining of loop
            if event.type == pygame.QUIT:
                return
        screen.fill(000)
        pygame.display.flip() #must be end of loop
    
if __name__ == "__main__":
    main()
