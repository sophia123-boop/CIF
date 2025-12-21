import pygame

pygame.init() # initialize game

# text
timesNewRoman = pygame.font.SysFont('Times New Roman', 30) # font
overlapping = timesNewRoman.render('OVERLAPPING', False, (255,255,255)) # display

# colors
black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
pink = (255, 0, 127)

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

# stationary box
box2_x = 400
box2_y = 300
rect2 = pygame.Rect(box2_x, box2_y, box_size, box_size)

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

        box2color = green # stationary box original color
        is_overlapping = False

        if rect1.colliderect(rect2):
            box2color = blue # change to blue
            is_overlapping = True

    box_x += box_x_change
    box_y += box_y_change

    rect1 = pygame.Rect(box_x, box_y, box_size, box_size)

    # drawing stuff

    screen.fill(black)

    if is_overlapping:
        screen.blit(overlapping,(width // 2 - 100, 50))

    pygame.draw.rect(screen, pink, rect1)
    pygame.draw.rect(screen, box2color, rect2)

    pygame.display.update()
