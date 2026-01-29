import pygame
import random

pygame.init()

# --- setting up --- 

#colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
orange = (232, 145, 78)
blue = (140, 195, 255)
gray = (200, 200, 200)

#screen
width = 600
height = 950
screen = pygame.display.set_mode((width, height))

#game state
start_screen = True
show_instructions = False

#capybara
cb = pygame.image.load("cif/cif/zpictures/ogcapybara.png").convert_alpha()
orig_width, orig_height = cb.get_size()
new_cb = (int(orig_width * 0.35), int(orig_height * 0.35))
cb = pygame.transform.smoothscale(cb, new_cb)
cb_width, cb_height = cb.get_size()

#capybara starting location
cb_x = 200
cb_y = 800
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
jump_count = 0

#carrot
carrot = pygame.image.load("cif/cif/zpictures/carrot.png").convert_alpha()
orig_width, orig_height = cb.get_size()
new_carrot = (int(orig_width * 0.6), int(orig_height * 0.7))
carrot = pygame.transform.smoothscale(carrot, new_carrot)
carrot_width, carrot_height = carrot.get_size()

#carrot center
carrot_pos = (275, 25)   
carrot_center = pygame.Rect(0, 0, 20, 20)
carrot_center.center = (carrot_pos[0] + carrot_width // 2, carrot_pos[1] + carrot_height // 2)

#fonts
timesNewRoman = pygame.font.SysFont('Times New Roman', 23)
instructions = timesNewRoman.render("Help feed Mr Capybara his carrots!", True, black)
instructions2 = timesNewRoman.render("Climb by jumping on the clouds using", True, black)
instructions3 = timesNewRoman.render("arrow keys and press up twice for double jump!", True, black)
instructions4 = timesNewRoman.render("Don't get shot by the red dot!", True, black)
ready_text = timesNewRoman.render("READY", True, black)
win = timesNewRoman.render("Victory! Carrot snatched!", True, black)
lose = timesNewRoman.render("Oh no! Mr Capybara was shot!", True, black)
retry = timesNewRoman.render("Press space to play again", True, black)
start_text = timesNewRoman.render("START GAME", True, black)

#booleans
game_won = False
game_lost = False

#ready button
ready_button = pygame.Rect(width//2 - 100, height//2 + 100, 200, 50)

#start button
start_button = pygame.Rect(width//2 - 100, height//2 + 100, 200, 50)

#ledges
ledge_width = cb_width+10

ledge_speed = 5

ledge1 = pygame.Rect(100, 800, ledge_width, 10)
ledge2 = pygame.Rect(400, 650, ledge_width, 10)
ledge3 = pygame.Rect(200, 500, ledge_width, 10)
ledge4 = pygame.Rect(500, 375, ledge_width, 10)
ledge5 = pygame.Rect(250, 200, ledge_width, 10)

ledge_list = [ledge1, ledge2, ledge3, ledge4, ledge5,]

#clouds
cloud = pygame.image.load("cif/cif/zpictures/cloud.png").convert_alpha()
orig_width, orig_height = cloud.get_size()
new_cloud = (int(orig_width * 0.55), int(orig_height * 0.55))
cloud = pygame.transform.smoothscale(cloud, new_cloud)
cloud_width, cloud_height = cloud.get_size()

#bullets
bullet_y = ledge3.top - 50

bullet_speed = -5

bullet1 = pygame.Rect(600, bullet_y, 15, 15)
bullet2 = pygame.Rect(120, bullet_y, 15, 15)
bullet3 = pygame.Rect(240, bullet_y, 15, 15)
bullet4 = pygame.Rect(360, bullet_y, 15, 15)
bullet5 = pygame.Rect(480, bullet_y, 15, 15)

bullet_list = [bullet1, bullet2, bullet3, bullet4, bullet5]

clock = pygame.time.Clock()

# --- main game loop ---

while True:
    #setting 
    mouse_pos = pygame.mouse.get_pos()
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        #activate start button and ready button
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_screen:
                if start_button.collidepoint(mouse_pos):
                    start_screen = False
                    show_instructions = True

            elif show_instructions:
                if ready_button.collidepoint(mouse_pos):
                    show_instructions = False

        if not start_screen and not show_instructions:

            #restart controls
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:                                
                    if game_won:
                            ledge_speed += random.randint(1,3)
                            bullet_speed += random.randint(-3,-1)
                            
                    if game_won or game_lost:
                        game_won = False
                        game_lost = False
                                    
                        cb_x = 200
                        cb_y = 800
                        cb_y_change = 0

                #capybara controls
                if event.key == pygame.K_RIGHT:
                    cb_x_change -= speed
                    move_left = True
                if event.key == pygame.K_LEFT:
                    cb_x_change += speed
                    move_right = True
                if event.key == pygame.K_UP:
                    if jump_count < 2:
                        cb_y_change = jump
                        jump_count += 1
                        is_jumping = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT and cb_x_change < 0:
                    cb_x_change = 0
                    move_left = False
                if event.key == pygame.K_LEFT and cb_x_change > 0:
                    cb_x_change = 0
                    move_right = False
        
    #playing
    if not start_screen and not show_instructions and not game_won and not game_lost:
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
            jump_count = 0

        #ledge movement
        for ledge in ledge_list:
            ledge.x += ledge_speed

            if ledge.left > width:
                ledge.right = 0

        #capybara ledge detection
        cb_rect = pygame.Rect(cb_x, cb_y, cb_width, cb_height)

        for ledge in ledge_list:
            if cb_rect.colliderect(ledge):
                if cb_y_change > 0 and cb_rect.bottom < ledge.top + 10:
                    cb_y = ledge.top - cb_height
                    cb_y_change = 0
                    is_jumping = False
                    jump_count = 0
                    cb_x += ledge_speed

        #bullet movement
        for bullet in bullet_list:
            bullet.x += bullet_speed

            if bullet.left < 0:
                bullet.right = width
                
        #capybara bullet detection
        for bullet in bullet_list:
            if cb_rect.colliderect(bullet):
                if bullet == bullet3:
                    game_lost = True
                else:
                    cb_shot = bullet_speed * 2

        #capybara carrot detection
        carrot_rect = pygame.Rect(275, 15, carrot_width, carrot_height)

        if cb_rect.colliderect(carrot_center):
            game_won = True    

    # --- drawing ---

    screen.fill(blue)
    
    if start_screen:
        screen.blit(cb, (width//2 - cb_width//2, height//2 - cb_height//2))
        start_button_color = gray if start_button.collidepoint(mouse_pos) else white
        pygame.draw.rect(screen, start_button_color, start_button, border_radius = 10)
        pygame.draw.rect(screen, black, start_button, 2, border_radius = 10)
        screen.blit(start_text, (start_button.centerx - start_text.get_width()//2, start_button.centery - start_text.get_height()//2))
    
    else:
        if show_instructions:
            pygame.draw.rect(screen, white, (50, height//2 - 200, 500, 400), border_radius = 15)
            screen.blit(instructions, (width//2 - instructions.get_width()//2, height//2 - 125))
            screen.blit(instructions2, (width//2 - instructions2.get_width()//2, height//2 - 75))
            screen.blit(instructions3, (width//2 - instructions3.get_width()//2, height//2 - 25))
            screen.blit(instructions4, (width//2 - instructions4.get_width()//2, height//2 + 25))

            ready_button_color = gray if ready_button.collidepoint(mouse_pos) else white
            pygame.draw.rect(screen, ready_button_color, ready_button, border_radius = 10)
            pygame.draw.rect(screen, black, ready_button, 2, border_radius = 10)
            screen.blit(ready_text, (ready_button.centerx - ready_text.get_width()//2, ready_button.centery - ready_text.get_height()//2))
            
        else:
            #carrot and center     
            screen.blit(carrot, carrot_pos)

            #capybara
            screen.blit(cb, (cb_x, cb_y))

            #ledges
            for ledge in ledge_list:
                screen.blit(cloud, (ledge.x, ledge.y - 15))

            #bullets
            for bullet in bullet_list:
                if bullet == bullet3:
                    pygame.draw.circle(screen, red, bullet.center, 10)
                else:
                    pygame.draw.circle(screen, black, bullet.center, 8)

            #game ending scenes
            if game_won:
                screen.fill(white)
                win_rect = win.get_rect(center=(width//2, height//2))
                screen.blit(win, win_rect)
                screen.blit(retry, (width//2 - retry.get_width()//2, height//2 + 50))
                screen.blit(cb, (width//2 - 50, height//2 + 150))
                cb_x = 0
                cb_y = 0

            if game_lost:
                screen.fill(white)
                lose_rect = lose.get_rect(center=(width//2, height//2))
                screen.blit(lose, lose_rect)  
                screen.blit(retry, (width//2 - retry.get_width()//2, height//2 + 50))
                screen.blit(cb, (width//2 - 50, height//2 + 150))
                cb_rect.x, cb_rect.y = width//2 - 50, height//2 + 150
                pygame.draw.circle(screen, red, cb_rect.center, 10)

    pygame.display.update()

    #cloud variation
    #inifite climber