import pygame

pygame.font.init()
s_width = 800
s_height = 700
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 30 height per block
#block_size = 30

top_left_x = (s_width - play_width) // 2 
top_left_y = s_height - play_height

def draw_text_middle(surface, text, size, color):
    font = pygame.font.SysFont("comicsans", size, bold=True)
    label = font.render(text, 1, color)

    surface.blit(label, (top_left_x + play_width /2 - (label.get_width()/2), 
    top_left_y + play_height/3 - label.get_height()/2))

win = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption('Tetris')

while True:
    win.fill((0,0,0))
    draw_text_middle(win, 'Press Any Key To Play', 60, (255,255,255))
    pygame.display.update()
