import pygame
import random

pygame.init()

size = 500, 500
screen = pygame.display.set_mode(size)
pygame.display.set_caption('SNAKE')

#------------------------ VARIABLES ----------------------------------------------------------------------------------------------------------

FPS = 10
fps_clock = pygame.time.Clock()

GREEN = (45, 87, 44)
OTHER_GREEN = (45, 80, 44)
GREY = (155, 155, 155)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

x_snake = 400
y_snake = 200
x_direction = 0
y_direction = 0
x_speed = 0
y_speed = 0

font = pygame.font.Font(None, 30)
score_text = font.render("Score:", 0, WHITE)

score = 0

#-------------------------- CLASSES --------------------------------------------------------------------------------------------------------------

class Snake():
    def __init__(self):
        super().__init__()
        
    def draw_snake(self, x, y, rect_width, rect_height):
        pygame.draw.rect(screen, BLUE, [x, y, rect_width, rect_height]) 

class Apple():
    def __init__(self, x, y, apple_width, apple_height):
        super().__init__()
        self.x = x
        self.y = y
        self.apple_width = apple_width
        self.apple_height = apple_height

    def draw_apple(self):
        pygame.draw.rect(screen, RED, [self.x, self.y, self.apple_width, self.apple_height])

#----------------------- FUNCTIONS ------------------------------------------------------------------------------------------------------------

def update_screen():
    screen.fill(GREEN)
    draw_grid(500, 500, 20)
    apple.draw_apple()
    snake.draw_snake(x_snake, y_snake, 20, 20)
    score_number = font.render(str(score), 0, WHITE)
    screen.blit(score_text, (20, 20))
    screen.blit(score_number, (90, 21))
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

snake = Snake()
apples = []

#------------------------- MAIN LOOPs ------------------------------------------------------------------------------------------------------------------

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and y_speed != 20:
                x_speed = 0
                y_speed = -20

            if event.key == pygame.K_DOWN and y_speed != -20:
                x_speed = 0
                y_speed = 20

            if event.key == pygame.K_RIGHT and x_speed != -20:
                x_speed = 20
                y_speed = 0

            if event.key == pygame.K_LEFT and x_speed != 20:
                x_speed = -20
                y_speed = 0

    x_direction = x_snake + x_speed
    y_direction = y_snake + y_speed

    x_snake = x_direction
    y_snake = y_direction

    if x_snake >= 500 or x_snake < 0 or y_snake >= 500 or y_snake < 0:
        run = False

    if len(apples) == 0:
        x_apple = random.randrange(0, 480, 20)
        y_apple = random.randrange(0, 480, 20)
        apple = Apple(x_apple, y_apple, 20, 20)
        apples.append(apple)

    if x_apple == x_snake and y_apple == y_snake:
        apples.pop(0)
        score += 1

    update_screen()
    fps_clock.tick(FPS)

pygame.quit()