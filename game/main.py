import pygame
import random

# starts pygame
pygame.init()

# creates game window and title
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Road Rush")

# controls frame rate
clock = pygame.time.Clock()

# fonts for text on screen
title_font = pygame.font.Font("assets/HighSpeed.otf", 50)
small_font = pygame.font.SysFont(None, 36)

#images
#car picture
car_img = pygame.image.load("assets/whitecar.png").convert_alpha()
car_img = pygame.transform.scale(car_img, (90, 60))
menu_car_x = -100
menu_car_img = pygame.transform.scale(car_img, (60, 40))


#coin picture
coin_img = pygame.image.load("assets/goldcoin.png").convert_alpha()
coin_img = pygame.transform.scale(coin_img, (40, 40))
#tree picture
tree_img = pygame.image.load("assets/tree.png").convert_alpha()
tree_img = pygame.transform.scale(tree_img, (60, 60))

#music
#coin sound
coin_sound = pygame.mixer.Sound("assets/coinsound.mp3")
#driving sound
pygame.mixer.music.load("assets/drivingsound.mp3")
pygame.mixer.music.set_volume(0.4)

# starting x position of car
car_x = 150

# y positions for each lane
lanes = [120, 220, 320, 420]

# starting lane and y position
current_lane = 1
car_y = lanes[current_lane]

# coin starting settings
coin_x = 800
score = 0
coin_lane = random.randint(0, 3)
coin_y = lanes[coin_lane]

# timer settings
time_limit = 60
start_time = 0
time_left = time_limit

# controls what screen is shown
game_state = "start"


# resets game variables when restarting
def reset_game():
    global car_x, current_lane, car_y
    global coin_x, coin_lane, coin_y
    global score, start_time, time_left
    
    # reset car position
    car_x = 150
    current_lane = 1
    car_y = lanes[current_lane]

    # reset coin position
    coin_x = 800
    coin_lane = random.randint(0, 3)
    coin_y = lanes[coin_lane]

    # reset score and timer
    score = 0
    start_time = pygame.time.get_ticks()
    time_left = time_limit


# draws the start screen
def draw_start_screen():
    # background color
    screen.fill((192, 192, 192))
    

    # game title
    title = title_font.render("ROAD RUSH", True, (255, 255, 255))
    pygame.draw.rect(screen, (180, 0, 0), (150, 75, 500, 90))

    pygame.draw.polygon(screen, (180, 0, 0),
                    [(150, 75), (110, 120), (150, 165)])

    pygame.draw.polygon(screen, (180, 0, 0),
                    [(650, 75), (690, 120), (650, 165)])

    screen.blit(title, title.get_rect(center=(400, 120)))

    # instructions to start game
    text1 = small_font.render("Use ARROW KEYS or WASD to move", True, (0, 0, 0))
    text2 = small_font.render("Collect 20 coins before time runs out", True, (0, 0, 0))
    text3 = small_font.render("Avoid tires and oil spills", True, (0, 0, 0))
    #making the "enter" text white
    p1 = small_font.render("Press ", True, (0, 0, 0))
    p2 = small_font.render("ENTER", True, (255, 255, 255))
    p3 = small_font.render(" to Start", True, (0, 0, 0))

    total_width = p1.get_width() + p2.get_width() + p3.get_width()
    x = 400 - total_width // 2

    screen.blit(p1, (x, 370))
    screen.blit(p2, (x + p1.get_width(), 370))
    screen.blit(p3, (x + p1.get_width() + p2.get_width(), 370))

    screen.blit(text1, text1.get_rect(center=(400, 250)))
    screen.blit(text2, text2.get_rect(center=(400, 290)))
    screen.blit(text3, text3.get_rect(center=(400, 330)))
    
    #road for little car on the home screen
    pygame.draw.rect(screen, (60, 60, 60), (0, 500, 800, 40))
    for x in range(0, 800, 50):
        pygame.draw.rect(screen, (255, 255, 255), (x, 518, 25, 4))
    screen.blit(menu_car_img, (menu_car_x, 485))

    #coins design on the homescreen
    menu_coin = pygame.transform.scale(coin_img, (100, 60))
    screen.blit(menu_coin, (60, 250))
    screen.blit(menu_coin, (640, 250))




# draws the main gameplay screen
def draw_game():
    # background color
    screen.fill((157, 193, 183))

    # race track
    pygame.draw.rect(screen, (60, 60, 60), (0, 100, 800, 400))

    # lane divider lines
    pygame.draw.line(screen, (255, 255, 255), (0, 200), (800, 200), 3)
    pygame.draw.line(screen, (255, 255, 255), (0, 300), (800, 300), 3)
    pygame.draw.line(screen, (255, 255, 255), (0, 400), (800, 400), 3)

    # player car
    screen.blit(car_img, (car_x, car_y))

    # collectible coin
    screen.blit(coin_img, (coin_x, coin_y + 10))

    #tree
    for x in range(50, 751, 150):
        screen.blit(tree_img, (x, 20))
        screen.blit(tree_img, (x, 520))

    # displays score
    #score box
    pygame.draw.rect(screen, (30, 30, 30), (60, 50, 140, 40))
    #timer box
    pygame.draw.rect(screen, (30, 30, 30), (590, 50, 140, 40))

    score_text = small_font.render(
        f"Score: {score}",
        True,
        (255, 255, 255)
    )
    screen.blit(score_text, (70, 60))

    # displays timer
    timer_text = small_font.render(
        f"Time: {time_left}",
        True,
        (255, 255, 255)
    )
    screen.blit(timer_text, (620, 60))


# draws the game over screen
def draw_game_over():
    # background color
    screen.fill((200, 100, 100))

    # game over title
    game_over = title_font.render("GAME OVER", True, (0, 0, 0))
    screen.blit(game_over, game_over.get_rect(center=(400, 120)))


    # final score text
    score_text = small_font.render(
        f"Final Score: {score}",
        True,
        (0, 0, 0)
    )
    screen.blit(score_text, (300, 230))

    # restart instructions
    restart = small_font.render(
        "Press R to Restart",
        True,
        (0, 0, 0)
    )
    screen.blit(restart, (280, 300))


# draws the win screen
def draw_win_screen():
    # background color
    screen.fill((100, 200, 100))

    # win message
    win = title_font.render("YOU WIN!", True, (0, 0, 0))
    screen.blit(win, win.get_rect(center=(400, 120)))

    # final score text
    score_text = small_font.render(f"Final Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (300, 230))

    # restart instructions
    restart = small_font.render(
        "Press R to Restart",
        True,
        (0, 0, 0)
    )
    screen.blit(restart, (280, 300))


# game loop runs while game is open
running = True

while running:
    #road for mini car in the homescreen
    
    # little car on the home screen
    if game_state == "start":
                menu_car_x += 5
                if menu_car_x > 900:
                    menu_car_x = -100


    # checks for events
    for event in pygame.event.get():

        # closes game window
        if event.type == pygame.QUIT:
            running = False

        # start screen controls
        if game_state == "start":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    reset_game()
                    pygame.mixer.music.play(-1)
                    game_state = "playing"

        # gameplay controls
        elif game_state == "playing":
            if event.type == pygame.KEYDOWN:

                # move car up a lane
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    if current_lane > 0:
                        current_lane -= 1

                # move car down a lane
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if current_lane < len(lanes) - 1:
                        current_lane += 1

                # move car left
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    car_x -= 20

                # move car right
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    car_x += 20

        # restart controls for end screens
        elif game_state == "game_over" or game_state == "win":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game_state = "start"

    # only runs game logic during gameplay
    if game_state == "playing":

        # updates car y position
        car_y = lanes[current_lane]

        # keeps car inside track boundaries
        if car_x < 50:
            car_x = 50

        if car_x > 750 - 90:
            car_x = 750 - 90

        # moves coin across screen
        coin_x -= 10

        # respawns coin when off screen
        if coin_x < -20:
            coin_x = 800
            coin_lane = random.randint(0, 3)
            coin_y = lanes[coin_lane]

        # hitboxes for collision detection
        car_rect = pygame.Rect(car_x, car_y, 90, 60)
        coin_rect = pygame.Rect(coin_x - 12, coin_y, 40, 40)

        # checks if car collected coin
        if car_rect.colliderect(coin_rect):
            score += 1
            coin_sound.play()

            coin_x = 800
            coin_lane = random.randint(0, 3)
            coin_y = lanes[coin_lane]

        # calculates elapsed time
        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000

        # updates countdown timer
        time_left = max(0, int(time_limit - elapsed_time))

        # if you win
        if score >= 20:
            pygame.mixer.music.stop()
            game_state = "win"
            

        # if you lose
        if time_left <= 0:
            pygame.mixer.music.stop()
            game_state = "game_over"

    # draws correct screen
    if game_state == "start":
        draw_start_screen()

    elif game_state == "playing":
        draw_game()

    elif game_state == "game_over":
        draw_game_over()

    elif game_state == "win":
        draw_win_screen()

    # updates screen
    pygame.display.flip()

    # limits game to 60 FPS
    clock.tick(60)

# closes pygame
pygame.quit()
