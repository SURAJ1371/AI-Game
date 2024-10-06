import numpy as np
import random
import pygame
from rl_agent import QLearningAgent
from player import Player
from obstacle import Obstacle
from procedural_gen import generate_obstacle_pattern
from ai_model import build_model

# Initialize Pygame
pygame.init()

# Game settings
WIDTH, HEIGHT = 800, 600
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Initialize Q-learning agent
actions = ['left', 'right']
agent = QLearningAgent(actions)

# Initialize player and obstacles
player = Player()
obstacles = [Obstacle(random.randint(0, WIDTH), 0)]

# Initialize Neural Network model
input_shape = (3,)  # State size (player.x, obstacle.x, obstacle.y)
model = build_model(input_shape, actions)

# Game loop
running = True
time = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Procedural generation
    time += 1
    new_obstacle_x = generate_obstacle_pattern(time)
    obstacles.append(Obstacle(new_obstacle_x, 0))

    # Get current state
    state = np.array([player.x, obstacles[0].x, obstacles[0].y])
    action_values = model.predict(state.reshape(1, -1))
    action = actions[np.argmax(action_values)]  # Select action based on NN output

    # Perform action
    if action == 'left':
        player.move_left()
    elif action == 'right':
        player.move_right()

    # Update reward based on collision or avoidance
    collision = player.check_collision(obstacles)
    if collision:
        reward = -100
    else:
        reward = 1

    # Update Q-Table
    next_state = np.array([player.x, obstacles[0].x, obstacles[0].y])
    agent.update_q_value(state.tobytes(), action, reward, next_state.tobytes())

    # Update game graphics
    screen.fill((255, 255, 255))  # Clear screen
    player.draw(screen)
    for obstacle in obstacles:
        obstacle.draw(screen)

    pygame.display.flip()  # Update the display
    clock.tick(FPS)  # Cap the frame rate

pygame.quit()
