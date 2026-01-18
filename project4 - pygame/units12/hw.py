import pygame
import math

pygame.init()

#colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
orange = (232, 145, 78)
blue = (140, 195, 255)

#setting up screen
width = 600
height = 950

screen = pygame.display.set_mode((width, height))

#setting up capybara
cb = pygame.image.load("cif/cif/zpictures/capybara.png").convert_alpha()
orig_width, orig_height = cb.get_size()
new_cb = (int(orig_width * 0.35), int(orig_height * 0.35))
cb = pygame.transform.smoothscale(cb, new_cb)
cb_width, cb_height = cb.get_size()

#setting up carrot
carrot = pygame.image.load("cif/cif/zpictures/carrot.png").convert_alpha()
orig_width, orig_height = cb.get_size()
new_carrot = (int(orig_width * 0.7), int(orig_height * 0.8))
carrot = pygame.transform.smoothscale(carrot, new_carrot)
carrot_width, carrot_height = carrot.get_size()

#myfonts
timesNewRoman = pygame.font.SysFont('Times New Roman', 30)
title = timesNewRoman.render("Help Mr Capybara get his carrot!", True, black)
win = timesNewRoman.render("Victory! Mr Capybara is now very happy!", True, black)
lose = timesNewRoman.render("Oh no! Mr Capybara was shot!", True, black)
retry = timesNewRoman.render("Press space to play again", True, black)

game_won = False
game_lost = False

#starting location
cb_x = 200
cb_y = 1000
cb_rect = pygame.Rect(cb_x, cb_y, cb_width, cb_height)
cb_x_change = 0
speed = 10
cb_shot = 0

move_left = False
move_right = False

#gravity
gravity = 1
jump = -20
cb_y_change = 0
is_jumping = False

#ledges
ledge_width = cb_width+10

try:
    ledge_speed = int(input("Enter difficulty of clouds (1-8, recommend 5): "))
except ValueError:
    ledge_speed = 8

ledge1 = pygame.Rect(100, 800, ledge_width, 10)
ledge2 = pygame.Rect(400, 650, ledge_width, 10)
ledge3 = pygame.Rect(200, 500, ledge_width, 10)
ledge4 = pygame.Rect(500, 350, ledge_width, 10)
ledge5 = pygame.Rect(250, 200, ledge_width, 10)

ledge_list = [ledge1, ledge2, ledge3, ledge4, ledge5,]

#setting up clouds
cloud = pygame.image.load("cif/cif/zpictures/cloud.png").convert_alpha()
orig_width, orig_height = cloud.get_size()
new_cloud = (int(orig_width * 0.55), int(orig_height * 0.55))
cloud = pygame.transform.smoothscale(cloud, new_cloud)
cloud_width, cloud_height = cloud.get_size()

#bullets
bullet_y = ledge3.top - 50

try:
    difficulty = int(input("Enter difficulty of bullets (1-5, recommend 3): "))
except ValueError:
    difficulty = 5

bullet_speed = -difficulty
bullet1 = pygame.Rect(0, bullet_y, 15, 15)
bullet2 = pygame.Rect(200, bullet_y, 15, 15)
bullet3 = pygame.Rect(400, bullet_y, 15, 15)

bullet_list = [bullet1, bullet2, bullet3]

clock = pygame.time.Clock()
while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if game_won or game_lost:
                    game_won = False
                    game_lost = False
                    
                    cb_x = 200
                    cb_y = 800
                    cb_y_change = 0

            if event.key == pygame.K_LEFT:
                cb_x_change -= speed
                move_left = True
            if event.key == pygame.K_RIGHT:
                cb_x_change += speed
                move_right = True
            if event.key == pygame.K_UP and not is_jumping:
                cb_y_change = jump
                is_jumping = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                cb_x_change = 0
                move_left = False
            if event.key == pygame.K_RIGHT:
                cb_x_change = 0
                move_right = False

    #capybara movement
    cb_x += cb_x_change + cb_shot
    cb_y_change += gravity
    if cb_y_change > 15:
        cb_y_change = 15
    cb_y += cb_y_change

    if cb_shot > 0:
        cb_shot -= 1
    elif cb_shot < 0:
        cb_shot += 1

    #capybara border detection
    if cb_x < 0:
        cb_x = 0
    elif cb_x + cb_width > width:
        cb_x = width - cb_width

    if cb_y < 0:
        cb_y = 0
        cb_y_change = 0
        
    if cb_y + cb_height > height:
        cb_y = height - cb_height
        cb_y_change = 0
        is_jumping = False

    #capybara ledge detection
    cb_rect = pygame.Rect(cb_x, cb_y, cb_width, cb_height)

    for ledge in ledge_list:
        if cb_rect.colliderect(ledge):
            if cb_y_change > 0 and cb_rect.bottom < ledge.top + 10:
                cb_y = ledge.top - cb_height
                cb_y_change = 0
                is_jumping = False
                cb_x += ledge_speed
    
    #ledge movement
    for ledge in ledge_list:
        ledge.x += ledge_speed

        if ledge.left > width:
            ledge.right = 0

    #bullet movement
    for bullet in bullet_list:
        bullet.x += bullet_speed

        if bullet.left < 0:
            bullet.right = width
        
    #capybara bullet detection
    for bullet in bullet_list:
        if cb_rect.colliderect(bullet):
            if bullet == bullet3:
                dist_x = cb_rect.centerx - bullet.centerx
                dist_y = cb_rect.centery - bullet.centery
                distance = math.sqrt(dist_x**2 + dist_y**2)
                
                if distance < 30:
                    game_lost = True
            else:
                cb_x += bullet_speed
                if abs(cb_rect.centery - bullet.centery) < 20:
                    cb_shot = 15

    #capybara carrot detection
    carrot_rect = pygame.Rect(250, 100, carrot_width, carrot_height)
    carrot_center = pygame.Rect(257, 150, 10, 10)

    if cb_rect.colliderect(carrot_center):
        game_won = True

    screen.fill(blue)

    #draw carrot and center
    screen.blit(carrot, (250, 100))
    pygame.draw.rect(screen, orange, carrot_center)

    #draw capybara
    screen.blit(cb, (cb_x, cb_y))

    #drawing ledges
    for ledge in ledge_list:
        screen.blit(cloud, (ledge.x, ledge.y - 15))

    #drawing bullets
    for bullet in bullet_list:
        if bullet == bullet3:
            pygame.draw.circle(screen, red, bullet.center, 10)
        else:
            pygame.draw.circle(screen, black, bullet.center, 8)
    
    #draw titles
    screen.blit(title, (100, 50))   

    if game_won:
        screen.fill(white)
        win_rect = win.get_rect(center=(width//2, height//2))
        screen.blit(win, win_rect)
        screen.blit(retry, (width//2 - 150, height//2 + 50))
        screen.blit(cb, (width//2 - 50, height//2 + 150))

    if game_lost:
        screen.fill(white)
        lose_rect = lose.get_rect(center=(width//2, height//2))
        screen.blit(lose, lose_rect)  
        screen.blit(retry, (width//2 - 150, height//2 + 50))
        screen.blit(cb, (width//2 - 50, height//2 + 150))
        cb_rect.x, cb_rect.y = width//2 - 50, height//2 + 150
        pygame.draw.circle(screen, red, cb_rect.center, 10)

    pygame.display.update()
