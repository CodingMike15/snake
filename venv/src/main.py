from typing import Tuple
import pygame
import random

pygame.init()

#------------------------- SCREEN ---------------------------------------------------------------------------------------------------------------

size = 500, 500
screen = pygame.display.set_mode(size)
pygame.display.set_caption('SNAKE')

#------------------------ VARIABLES ----------------------------------------------------------------------------------------------------------

# FPS
FPS = 8
fps_clock = pygame.time.Clock()

# COLORS
GREEN = (45, 87, 44)
OTHER_GREEN = (45, 80, 44)
GREY = (155, 155, 155)
BLUE = (0, 0, 255)
DARK_BLUE = (0, 0, 230)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# SNAKE VARIABLES
x_snake = 400
y_snake = 200
direction = ''
snake_pos_x = [x_snake]
snake_pos_y = [y_snake]

# APPLE VARIABLES
apples = []

# UI
font = pygame.font.Font(None, 30)
font_title = pygame.font.Font(None, 100)
font_play_btn = pygame.font.Font(None, 40)
text_play_btn = font_play_btn.render('Play', 0, WHITE)
score_text = font.render("Score:", 0, WHITE)
title = font_title.render("SNAKE", 0, WHITE)
score = 0

#-------------------------- CLASSES --------------------------------------------------------------------------------------------------------------

class Snake():
    def __init__(self):
        super().__init__()
        self.width = 20
        self.height = 20

    def draw_snake(self, x, y):
        pygame.draw.rect(screen, DARK_BLUE, [x, y, self.width, self.height]) 
    
    def draw_body(self):
        for i in range(1, len(snake_pos_x)):
            pygame.draw.rect(screen, BLUE, [snake_pos_x[i], snake_pos_y[i], self.width, self.height])

class Apple():
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.apple_width = 20
        self.apple_height = 20

    def draw_apple(self):
        pygame.draw.rect(screen, RED, [self.x, self.y, self.apple_width, self.apple_height])

class Button():
    def __init__(self, x, y, width, height, color, text):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.pressed = False

    def draw_button(self):
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.width, self.height])   

#----------------------- FUNCTIONS ------------------------------------------------------------------------------------------------------------

def update_game():
    screen.fill(GREEN)
    draw_grid(500, 500, 20)
    apple.draw_apple()
    snake.draw_snake(snake_pos_x[0], snake_pos_y[0])
    snake.draw_body()
    score_number = font.render(str(score), 0, WHITE)
    screen.blit(score_text, (20, 20))
    screen.blit(score_number, (90, 21))
    pygame.display.update()

def update_menu():
    screen.fill(GREEN)
    screen.blit(title, (120, 50))
    btn_play.draw_button()
    screen.blit(text_play_btn, (219, 168))
    pygame.display.update()

def draw_grid(height, width, rect_size):
    x_height = 0
    y_width = 0
    rect_size = rect_size

    for i in range(height):
        x_height = x_height + rect_size
        pygame.draw.line(screen, OTHER_GREEN, (x_height, 0), (x_height, 500))

    for i in range(width):
        y_width = y_width + rect_size
        pygame.draw.line(screen, OTHER_GREEN, (0, y_width), (500, y_width))

#------------------------- MAIN LOOP ------------------------------------------------------------------------------------------------------------------

snake = Snake()
btn_play = Button(190, 150, 120, 60, GREY, 'Play')

run = True
menu = True
play = False
while run:

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
                run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos() > (btn_play.x, btn_play.y) and pygame.mouse.get_pos() < (btn_play.x + btn_play.width, btn_play.y + btn_play.height):
                menu = False
                play = True
        
        update_menu()

    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != 'DOWN':
                    direction = 'UP'

                if event.key == pygame.K_DOWN and direction != 'UP':
                    direction = 'DOWN'

                if event.key == pygame.K_RIGHT and direction != 'LEFT':
                    direction = 'RIGHT'

                if event.key == pygame.K_LEFT and direction != 'RIGHT':
                    direction = 'LEFT'
        
        if direction == 'UP':
            y_snake -= 20

        if direction == 'DOWN':
            y_snake += 20

        if direction == 'RIGHT':
            x_snake += 20

        if direction == 'LEFT':
            x_snake -= 20

        snake_pos_x.insert(0, x_snake)
        snake_pos_y.insert(0, y_snake)

        snake_pos_x.pop(len(snake_pos_x) - 1)
        snake_pos_y.pop(len(snake_pos_y) - 1)

        if snake_pos_x[0] >= 500 or snake_pos_x[0] < 0 or snake_pos_y[0] >= 500 or snake_pos_y[0] < 0:
            play = False
            run = False

        for i in range(1, len(snake_pos_x)):
            if snake_pos_x[0] == snake_pos_x[i] and snake_pos_y[0] == snake_pos_y[i]:
                play = False
                run = False

        if len(apples) == 0:
            x_apple = random.randrange(0, 480, 20)
            y_apple = random.randrange(0, 480, 20)
            apple = Apple(x_apple, y_apple)
            apples.append(apple)

        if x_apple == snake_pos_x[0] and y_apple == snake_pos_y[0]:
            apples.pop(0)
            score += 1
            if direction == 'UP':
                snake_pos_x.append(snake_pos_x[len(snake_pos_x) - 1])
                snake_pos_y.append(snake_pos_y[len(snake_pos_y)- 1] + 20)

            if direction == 'DOWN':
                snake_pos_x.append(snake_pos_x[len(snake_pos_x) - 1])
                snake_pos_y.append(snake_pos_y[len(snake_pos_y) -1] - 20)

            if direction == 'RIGHT':
                snake_pos_x.append(snake_pos_x[len(snake_pos_x) - 1] - 20)
                snake_pos_y.append(snake_pos_y[len(snake_pos_y) - 1])

            if direction == 'LEFT':
                snake_pos_x.append(snake_pos_x[len(snake_pos_x) - 1] + 20)
                snake_pos_y.append(snake_pos_y[len(snake_pos_y) - 1])

        update_game()
        fps_clock.tick(FPS)

pygame.quit()