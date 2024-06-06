#import pygame  # Import the pygame module to use its functions and classes
#import random  # Import the random module for generating random numbers
#import sys     # Import the sys module for exiting the game

pygame.init()  # Initialize the pygame module

screen = pygame.display.set_mode((300, 300))  # Set up the display with a size of 300x300 pixels
pygame.display.set_caption('Snake Game')  # Set the window title to 'Snake Game'

# Set up the snake and food
snake_pos = [[20, 10]]
food_pos = [random.randint(0, 29), random.randint(0, 29)]
direction = pygame.K_RIGHT

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()  # Use sys.exit() to exit the game
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != pygame.K_RIGHT:
                direction = pygame.K_LEFT
            elif event.key == pygame.K_RIGHT and direction != pygame.K_LEFT:
                direction = pygame.K_RIGHT
            elif event.key == pygame.K_UP and direction != pygame.K_DOWN:
                direction = pygame.K_UP
            elif event.key == pygame.K_DOWN and direction != pygame.K_UP:
                direction = pygame.K_DOWN

    # Move the snake
    new_head = [snake_pos[0][0] + (1 if direction == pygame.K_RIGHT else -1 if direction == pygame.K_LEFT else 0),
                snake_pos[0][1] + (1 if direction == pygame.K_DOWN else -1 if direction == pygame.K_UP else 0)]

    # Check for collisions with the walls or itself
    if new_head[0] < 0 or new_head[0] > 29 or new_head[1] < 0 or new_head[1] > 29 or new_head in snake_pos:
        pygame.quit()
        sys.exit()

    # Update the snake's position
    snake_pos.insert(0, new_head)

    # Check for collisions with the food
    if snake_pos[0] == food_pos:
        food_pos = [random.randint(0, 29), random.randint(0, 29)]
    else:
        snake_pos.pop()

    for pos in snake_pos:
        pygame.draw.rect(screen, (0, 128, 0), pygame.Rect(pos[1] * 10, pos[0] * 10, 10, 10))  # Draw the snake

    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(food_pos[1] * 10, food_pos[0] * 10, 10, 10))  # Draw the food
    pygame.display.flip()  # Update the display
