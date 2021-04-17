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
font_title_menu = pygame.font.Font(None, 100)
font_play_btn = pygame.font.Font(None, 40)
font_quit_btn = pygame.font.Font(None, 40)
font_title_game_over = pygame.font.Font(None, 100)


text_play_btn = font_play_btn.render('Play', 0, WHITE)
text_quit_btn = font_quit_btn.render('Quit', 0, WHITE)
score_text = font.render("Score:", 0, WHITE)
title_menu = font_title_menu.render("SNAKE", 0, WHITE)
title_game_over = font_title_game_over.render('GAME OVER', 0, WHITE)

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
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

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
    screen.blit(title_menu, (120, 50))
    btn_play.draw_button()
    screen.blit(text_play_btn, (219, 168))
    btn_quit.draw_button()
    screen.blit(text_quit_btn, (219, 257))
    pygame.display.update()

def update_game_over():
    screen.fill(RED)
    screen.blit(title_game_over, (40, 50))
    btn_play.draw_button()
    screen.blit(text_play_btn, (219, 168))
    btn_quit.draw_button()
    screen.blit(text_quit_btn, (219, 257))
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
btn_play = Button(190, 150, 120, 60, GREY)
btn_quit = Button(190, 240, 120, 60, GREY)

run = True
menu = True
play = False
game_over = False
while run:
    while menu:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_x > btn_play.x and mouse_x < btn_play.x + btn_play.width:
                    if mouse_y > btn_play.y and mouse_y < btn_play.y + btn_play.height:
                        menu = False
                        play = True

                if mouse_x > btn_quit.x and mouse_x < btn_quit.x + btn_quit.width:
                    if mouse_y > btn_quit.y and mouse_y < btn_quit.y + btn_quit.height:
                        menu = False
                        run = False
        
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
        
        if direction == 'NONE':
            x_snake = x_snake
            y_snake = y_snake

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
            game_over = True

        for i in range(1, len(snake_pos_x)):
            if snake_pos_x[0] == snake_pos_x[i] and snake_pos_y[0] == snake_pos_y[i]:
                play = False
                game_over = True

        if len(apples) == 0:
            x_apple = random.randrange(0, 480, 20)
            y_apple = random.randrange(0, 480, 20)

            for i in range(len(snake_pos_x)):
                if snake_pos_x[i] == x_apple and snake_pos_y[i] == y_apple:
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

    while game_over:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = False
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_x > btn_play.x and mouse_x < btn_play.x + btn_play.width:
                    if mouse_y > btn_play.y and mouse_y < btn_play.y + btn_play.height:
                        x_snake = 400
                        y_snake = 200
                        direction = 'NONE'

                        snake_pos_x.clear()
                        snake_pos_y.clear()

                        snake_pos_x.append(x_snake)
                        snake_pos_y.append(y_snake)

                        score = 0

                        game_over = False
                        play = True

                if mouse_x > btn_quit.x and mouse_x < btn_quit.x + btn_quit.width:
                    if mouse_y > btn_quit.y and mouse_y < btn_quit.y + btn_quit.height:
                        game_over = False
                        run = False
                
        update_game_over()

pygame.quit()