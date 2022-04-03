import pygame
pygame.font.init() 
   
def draw_grid(surface, grid):
    sx = top_left_x
    sy = top_left_y
    #Traverse 20 rows, draw 20 lines with color (0,128,128) that is 20 horizontal lines, 
    #each line is separated by 1 block_size = 30, starting from top_left_x position and ending top_left_x + play_width
    for i in range(1):
        pygame.draw.line(surface, (0,128,128), (sx, sy), (sx + play_width, sy))
        #iterate through each cell in 1 row, draw 10 colored lines (0,128,128) that is 10 vertical rows, 
        #each line is separated by 1 block_size = 30
        for j in range(1):
            pygame.draw.line(surface, (0, 128, 128), (sx, sy),(sx, sy + play_height))

s_width = 800
s_height = 700
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 30 height per block
top_left_x = (s_width - play_width) // 2 
top_left_y = s_height - play_height 
win = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption('Tetris')

while True:
    win.fill((0,0,0))
    grid = [[(0,0,0) for _ in range(10)] for _ in range(20)]
    draw_grid(win, grid)
    pygame.display.update()

