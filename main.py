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