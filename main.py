import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game")

clock = pygame.time.Clock()

#car start position
car_x = 150
car_y = 150

#track lanes
lanes = [120, 220, 320, 420]
current_lane = 1

#coins
coin_x = 800
score = 0
coin_lane = random.randint(0, 3)
coin_y = lanes[coin_lane]
font = pygame.font.SysFont(None, 36)

#timer countdown
start_time = pygame.time.get_ticks()
time_limit = 60

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # car movement controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if current_lane > 0:
                    current_lane -= 1

            if event.key == pygame.K_DOWN:
                if current_lane < len(lanes) - 1:
                    current_lane += 1

    car_y = lanes[current_lane]

    #background color
    screen.fill((157, 193, 183))

    #the race track
    pygame.draw.rect(screen, (100, 100, 100), (50, 50, 700, 500))
    pygame.draw.line(screen, (255, 255, 255), (50, 175), (750, 175), 3)
    pygame.draw.line(screen, (255, 255, 255), (50, 275), (750, 275), 3)
    pygame.draw.line(screen, (255, 255, 255), (50, 375), (750, 375), 3)

    #the car color and stuff
    pygame.draw.rect(screen, (255, 0, 0), (car_x, car_y, 50, 30))

    #drawing the coin
    pygame.draw.circle(screen, (255, 255, 0), (coin_x, coin_y + 15), 12)
    
    #how the coins show up and move
    coin_x -= 10
    if coin_x < -20:
        coin_x = 800
        coin_lane = random.randint(0, 3)
        coin_y = lanes[coin_lane]

    car_rect = pygame.Rect(car_x, car_y, 50, 30)
    coin_rect = pygame.Rect(coin_x - 12, coin_y, 24, 24)

    if car_rect.colliderect(coin_rect):
        score += 1
        coin_x = 800
        coin_lane = random.randint(0, 3)
        coin_y = lanes[coin_lane]
    
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    #time countdown display
    elapsed_time = (pygame.time.get_ticks() - start_time) / 1000
    time_left = max(0, int(time_limit - elapsed_time))

    timer_text = font.render(f"Time: {time_left}", True, (255, 255, 255))
    screen.blit(timer_text, (650, 10))

    if score >= 20:
        print("YOU WIN!")
        running = False

    if time_left <= 0:
        print("YOU LOSE!")
        running = False

    clock.tick(60)
    pygame.display.flip()


pygame.quit()




import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game")
font = pygame.font.SysFont(None, 50)

#
car_x = 150
lanes = [110, 210, 310, 410]
current_lane = 1
car_y = lanes[current_lane]

def draw_start_screen():
    screen.fill((157, 193, 183))

    # title
    title = font.render("ROAD RUSH", True, (0, 0, 0))
    screen.blit(title, (250, 100))

    # instructions
    text = font.render("Press ENTER to Start", True, (0, 0, 0))
    screen.blit(text, (220, 250))

def draw_game():
    screen.fill((157, 193, 183))

    # race track
    pygame.draw.rect(screen, (100, 100, 100), (50, 50, 700, 500))
    pygame.draw.line(screen, (255, 255, 255), (50, 175), (750, 175), 3)
    pygame.draw.line(screen, (255, 255, 255), (50, 275), (750, 275), 3)
    pygame.draw.line(screen, (255, 255, 255), (50, 375), (750, 375), 3)

    # draw car
    pygame.draw.rect(screen, (255, 0, 0), (car_x, car_y, 50, 30))
    

def draw_game_over():
    screen.fill((200, 100, 100))

    game_over = font.render("GAME OVER", True, (0, 0, 0))
    screen.blit(game_over, (250, 150))

    restart = font.render("Press R to Restart", True, (0, 0, 0))
    screen.blit(restart, (220, 250))

def draw_win_screen():
    screen.fill((100, 200, 100))

    win = font.render("YOU WIN!", True, (0, 0, 0))
    screen.blit(win, (300, 150))

    restart = font.render("Press R to Restart", True, (0, 0, 0))
    screen.blit(restart, (220, 250))


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # START SCREEN
        if game_state == "start":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_state = "playing"

        # GAMEPLAY
        elif game_state == "playing":
            if event.type == pygame.KEYDOWN:

                # TEST GAME OVER
                if event.key == pygame.K_g:
                    game_state = "game_over"

                 # UP
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    if current_lane > 0:
                        current_lane -= 1

                # DOWN
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if current_lane < len(lanes) - 1:
                        current_lane += 1

                # LEFT
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    car_x -= 20

                # RIGHT
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    car_x += 20

        # RESTART
        elif game_state == "game_over" or game_state == "win":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game_state = "start"
                    current_lane = 1

    car_y = lanes[current_lane]

    # boundaries
    if car_x < 50:
        car_x = 50

    if car_x > 700:
        car_x = 700

    if game_state == "start":
            draw_start_screen()
        
    elif game_state == "playing":
        draw_game()
        
    elif game_state == "game_over":
        draw_game_over()
        
    elif game_state == "win":
        draw_win_screen()



    pygame.display.flip()

pygame.quit()
