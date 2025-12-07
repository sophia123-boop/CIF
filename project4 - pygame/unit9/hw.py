import pygame # import
pygame.init() # initiate game

# defining colors
green = (0, 168, 107)
pink = (255, 0, 127)
black = (0, 0, 0)

# setting up width and height of screen
width = 800
height = 600

# starting coordinates of box
box_size = 30

# box 1 coordinates
box_x = 0
box_y = 0

# box 2 coordinates
box_x2 = width - box_size
box_y2 = height - box_size

# initializing boxes
rect1 = pygame.Rect(box_x, box_y, 30, 30)
rect2 = pygame.Rect(box_x2, box_y2, 30, 30)

# create screen
screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()
while True:
    clock.tick(30) # 30 frames per second
    for event in pygame.event.get(): # if user clicked quit button
        if event.type == pygame.QUIT: # exit
            exit()

    # if pink box touches edge, stop
    if box_x + box_size > width:
        box_x = width - box_size

    # if green box touches edge, stop
    if box_x2 < 0:
        box_x2 = 0

    # make the boxes move to the right and left
    box_x += 5
    box_x2 -= 5

    # drawing the boxes
    rect1 = pygame.Rect(box_x, box_y, 30, 30)
    rect2 = pygame.Rect(box_x2, box_y2, 30, 30)
    pygame.draw.rect(screen, pink, rect1)
    pygame.draw.rect(screen, green, rect2)

    # update screen, erase prior instances
    pygame.display.update()
    screen.fill(black)
