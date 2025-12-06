import pygame
pygame.init()
clock = pygame.time.Clock()
while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # initiate screen
    # create box
    # change x by 5 each frame however many times
    # stop

    pygame.display.update()