import pygame
import random

pygame.init()
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])  # Initialise the screen
pygame.display.set_caption("Snake Game By Harika")  # set caption to the screen

clock = pygame.time.Clock()  # to set speed of snake movement on the screen
snake_speed = 7
snake_block_size = 10

font_style = pygame.font.SysFont(None, 30)


def display_score(score):
    score_message = font_style.render("Your score: " + str(score), True, 'yellow')
    screen.blit(score_message, [0, 0])


def display_message(message, color):
    message = font_style.render(message, True, color)
    screen.blit(message, [100, 100])


def render_snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, 'green', [x[0], x[1], snake_block_size, snake_block_size])  # setting snake on screen [x-coOrd, y-coOrd, width, height]


def snake_game():
    screen_alive = True  # flag to keep the game screen alive
    game_alive = True  # flag to keep the game alive

    snake_x = screen_width/2  # initial snake x-coordinate position on screen
    snake_y = screen_height/2  # initial snake y-coordinate position on screen

    x_change = 0
    y_change = 0

    food_x = random.randrange(0, screen_width - snake_block_size, snake_block_size)
    food_y = random.randrange(0, screen_height - snake_block_size, snake_block_size)

    snake_length = 1
    snake_body = []

    while screen_alive:
        while not game_alive:
            screen.fill('white')
            display_message("You lost with Score: " + str(snake_length - 1) + ", Press Q:Quit or R:Retry", 'red')
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    screen_alive = False
                    game_alive = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        screen_alive = False
                        game_alive = True
                    if event.key == pygame.K_r:
                        snake_game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # on clicking the game screen close button
                screen_alive = False
            if event.type == pygame.KEYDOWN:  # on clicking any keyboard key
                if event.key == pygame.K_RIGHT:
                    x_change = snake_block_size
                    y_change = 0
                if event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = snake_block_size
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block_size
                    y_change = 0
                if event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -snake_block_size

        if snake_x >= screen_width or snake_x < 0 or snake_y >= screen_height or snake_y < 0:  # to quit the game when snake touch borders
            game_alive = False

        snake_x += x_change
        snake_y += y_change
        screen.fill([35, 35, 35])  # setting background color
        pygame.draw.rect(screen, 'blue', [food_x, food_y, snake_block_size, snake_block_size])  # setting food position on screen
        snake_head = [snake_x, snake_y]
        snake_body.append(snake_head)
        if len(snake_body) > snake_length:
            del snake_body[0]

        for tail in snake_body[:-1]:  # to quit the game when snake touch its tail
            if tail == snake_head:
                game_alive = False

        render_snake(snake_body)
        display_score(snake_length - 1)

        pygame.display.update()  # update display to show the events on screen

        if snake_x == food_x and snake_y == food_y:
            food_x = random.randrange(0, screen_width - snake_block_size, snake_block_size)
            food_y = random.randrange(0, screen_height - snake_block_size, snake_block_size)
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


snake_game()
