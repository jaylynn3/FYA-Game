import pygame
from classes.player import Player
from classes.enemy import Enemy

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")

# Load background image
background = pygame.image.load("assets/space_background.png")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Create a Player object
player = Player(x=SCREEN_WIDTH // 2, y=SCREEN_HEIGHT - 100, screen_width=SCREEN_WIDTH)

# Initialize score
score = 0
font = pygame.font.Font(None, 36)

# Initialize enemies
enemies = []
rows = 3  # Number of rows of enemies
columns = 6  # Number of enemies per row
enemy_speed = 2

for row in range(rows):
    for col in range(columns):
        x_position = 100 + col * 70  # Horizontal spacing
        y_position = 50 + row * 50  # Vertical spacing
        enemy = Enemy(x_position, y_position, speed=enemy_speed)
        enemies.append(enemy)

def check_collision(obj1, obj2):
    """
    Checks if two objects collide based on their rectangular areas.

    Parameters:
    - obj1: First object (e.g., laser).
    - obj2: Second object (e.g., enemy).

    Returns:
    - True if the rectangles overlap, False otherwise.
    """
    return (
        obj1.x < obj2.x + obj2.width and
        obj1.x + obj1.width > obj2.x and
        obj1.y < obj2.y + obj2.height and
        obj1.y + obj1.height > obj2.y
    )

def render_score(screen, score, font):
    """
    Displays the player's score in the top-left corner.

    Parameters:
    - screen: The game screen where the text will be drawn.
    - score: The current score to display.
    - font: The font used to render the text.
    """
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))  # White text
    screen.blit(score_text, (10, 10))  # Draw the score at the top-left corner

def update_enemies():
    """
    Moves all enemies in the list.
    """
    for enemy in enemies:
        enemy.move(SCREEN_WIDTH)

def draw_enemies():
    """
    Draws all enemies on the screen.
    """
    for enemy in enemies:
        enemy.draw(screen)

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move('left')
    if keys[pygame.K_RIGHT]:
        player.move('right')
    if keys[pygame.K_SPACE]:  
        player.shoot()


    # Check for collisions between lasers and enemies
    lasers_to_remove = []
    enemies_to_remove = []

    for laser in player.lasers:
        for enemy in enemies:
            if check_collision(laser, enemy):
                lasers_to_remove.append(laser)
                enemies_to_remove.append(enemy)
                score += 10  # Increase score when an enemy is destroyed

    # Remove lasers and enemies safely after looping
    for laser in lasers_to_remove:
        if laser in player.lasers:
            player.lasers.remove(laser)

    for enemy in enemies_to_remove:
        if enemy in enemies:
            enemies.remove(enemy)

    # Clear the screen
    screen.blit(background, (0, 0))  # Draw background
    update_enemies()
    player.update_lasers()
    
    # Draw game elements
    player.draw(screen)
    draw_enemies()

    # Display the score
    render_score(screen, score, font)

    pygame.display.flip()

    # Limit frame rate
    clock.tick(60)

pygame.quit()
