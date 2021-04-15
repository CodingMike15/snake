import pygame

pygame.init()

size = 500, 500
screen = pygame.display.set_mode(size)
pygame.display.set_caption('SNAKE')

FPS = 10
fps_clock = pygame.time.Clock()

GREEN = (45, 87, 44)
GREY = (155, 155, 155)
BLUE = (0, 0, 255)

x_snake = 400
y_snake = 200
x_direction = 0
y_direction = 0
x_speed = 0
y_speed = 0

class Snake():
    def __init__(self):
        super().__init__()

    def draw_snake(self, x, y, rect_width, rect_height):
        pygame.draw.rect(screen, BLUE, [x, y, rect_width, rect_height]) 

def update_screen():
    screen.fill(GREEN)
    draw_grid(500, 500, 20)
    snake.draw_snake(x_snake, y_snake, 20, 20)
    pygame.display.update()

def draw_grid(height, width, rect_size):
    x_height = 0
    y_width = 0
    rect_size = rect_size

    for i in range(height):
        x_height = x_height + rect_size
        pygame.draw.line(screen, GREY, (x_height, 0), (x_height, 500))

    for i in range(width):
        y_width = y_width + rect_size
        pygame.draw.line(screen, GREY, (0, y_width), (500, y_width))

snake = Snake()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                x_speed = 0
                y_speed = -20

            if event.key == pygame.K_DOWN:
                x_speed = 0
                y_speed = 20

            if event.key == pygame.K_RIGHT:
                x_speed = 20
                y_speed = 0

            if event.key == pygame.K_LEFT:
                x_speed = -20
                y_speed = 0

    x_direction = x_snake + x_speed
    y_direction = y_snake + y_speed

    x_snake = x_direction
    y_snake = y_direction

    if x_snake >= 500:
        run = False

    if y_snake >= 500:
        run = False

    update_screen()
    fps_clock.tick(FPS)

pygame.quit()