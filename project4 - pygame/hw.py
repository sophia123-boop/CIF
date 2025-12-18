import pygame # import
from random import randint

pygame.init() # initiate game

color_change = pygame.USEREVENT + 1
pygame.time.set_timer(color_change, 2000)

# defining colors
black = (0, 0, 0)
color = (255, 0, 0)

# setting up width and height of screen
width = 800
height = 600

# starting box status
box_x = 0
box_y = 0
box_x_change = 0
box_y_change = 0
box_size = 30
rect1 = pygame.Rect(box_x, box_y, box_size, box_size)
speed = 5

# booleans
move_up = False
move_left = False
move_down = False
move_right = False

# create screen
screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()
while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                box_x_change -= speed
                move_left = True
            if event.key == pygame.K_RIGHT:
                box_x_change += speed
                move_right = True
            if event.key == pygame.K_UP:
                box_y_change -= speed
                move_up = True
            if event.key == pygame.K_DOWN:
                box_y_change += speed
                move_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                box_x_change = 0
                move_left = False
            if event.key == pygame.K_RIGHT:
                box_x_change = 0
                move_right = False
            if event.key == pygame.K_UP:
                box_y_change = 0
                move_up = False
            if event.key == pygame.K_DOWN:
                box_y_change = 0
                move_down = False

        if event.type == color_change:
            color = (randint(0, 255), randint(0, 255), randint(0, 255))
            

    box_x += box_x_change
    box_y += box_y_change

    if box_x + box_size > width:
        box_x = width - box_size
    if box_x < 0:
        box_x = 0
    if box_y + box_size > height:
        box_y = height - box_size
    if box_y < 0:
        box_y = 0

    rect1 = pygame.Rect(box_x, box_y, 30, 30) # drawing box
    pygame.draw.rect(screen, color, rect1)

    # update screen, erase prior instances
    screen.fill(black)
    pygame.draw.rect(screen, color, rect1)
    pygame.display.update()
