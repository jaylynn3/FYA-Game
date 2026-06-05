import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game")

#
car_x = 150
car_y = 150

lanes = [120, 220, 320, 420]
current_lane = 1

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

    #the car
    pygame.draw.rect(screen, (255, 0, 0), (car_x, car_y, 50, 30))


    pygame.display.flip()

pygame.quit()