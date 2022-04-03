import pygame
import random
pygame.font.init()


def draw_window(surface, grid, score=0, last_score = 0):
    #Entire window shows black, R G B = (0,0,0) = black
    surface.fill((0, 0, 0))

    #Initializing fonts in pygame
    pygame.font.init()
    #Define font style, font size, font color, determine display position in the window
    font = pygame.font.SysFont('comicsans', 40)
    label = font.render('Tetris', 1, (255, 255, 255))
    surface.blit(label, (top_left_x + play_width / 2 - (label.get_width() / 2), 20))

    #Display current score
    font = pygame.font.SysFont('comicsans', 30)
    label = font.render('Score: ' + str(score), 1, (255,255,255))
    sx = top_left_x + play_width + 50
    sy = top_left_y + play_height/2 - 100
    surface.blit(label, (sx + 20, sy + 160))

    #Display last score
    label = font.render('High Score: ' + last_score, 1, (255,255,255))
    sx = top_left_x - 240
    sy = top_left_y + 200
    surface.blit(label, (sx + 20, sy + 160))

    #draw contours around the cells
    pygame.draw.rect(surface, (0,128,128), (top_left_x, top_left_y, play_width, play_height), 4)
    #draw_grid(surface, grid)

s_width = 800
s_height = 700
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 30 height per block
block_size = 30
top_left_x = (s_width - play_width) // 2 
top_left_y = s_height - play_height

win = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption('Tetris')

while True:
    win.fill((0,0,0))
    grid = [[(0,0,0) for _ in range(10)] for _ in range(20)]
    print(grid)
    draw_window(win, grid, 0, str(0))
    pygame.time.delay(1000)
    pygame.display.update()