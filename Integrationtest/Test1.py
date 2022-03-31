import pygame

pygame.font.init()
s_width = 800
s_height = 700
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 30 height per block
block_size = 30

top_left_x = (s_width - play_width) // 2 
top_left_y = s_height - play_height

def draw_text_middle(surface, text, size, color):
    font = pygame.font.SysFont("comicsans", size, bold=True)
    label = font.render(text, 1, color)

    surface.blit(label, (top_left_x + play_width /2 - (label.get_width()/2), 
    top_left_y + play_height/3 - label.get_height()/2))

def draw_grid(surface, grid):
    sx = top_left_x
    sy = top_left_y
    #Traverse 20 rows, draw 20 lines with color (0,128,128) that is 20 horizontal lines, 
    #each line is separated by 1 block_size = 30, starting from top_left_x position and ending top_left_x + play_width
    for i in range(len(grid)):
        pygame.draw.line(surface, (0,128,128), (sx, sy + i*block_size), 
        (sx+play_width, sy+ i*block_size))
        #iterate through each cell in 1 row, draw 10 colored lines (0,128,128) that is 10 vertical rows, 
        #each line is separated by 1 block_size = 30
        for j in range(len(grid[i])):
            pygame.draw.line(surface, (0, 128, 128), (sx + j*block_size, sy),
            (sx + j*block_size, sy + play_height))

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

    # #
    # for i in range(len(grid)):
    #     for j in range(len(grid[i])):
    #         pygame.draw.rect(surface, grid[i][j], (top_left_x + j*block_size, top_left_y + 
    #         i*block_size, block_size, block_size), 0)

    #draw contours around the cells
    pygame.draw.rect(surface, (0,128,128), (top_left_x, top_left_y, play_width, play_height), 5)

    draw_grid(surface, grid)
    #pygame.display.update()
def main(win):  # *
    run = True
    while run:
        grid = grid = [[(0,0,0) for _ in range(10)] for _ in range(20)]
        #catch keypress events from keyboard
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()

            if event.type == pygame.KEYDOWN:
                print("test1")

        draw_window(win, grid, 0, str(0))
        pygame.display.update()

def main_menu(win):  # *
    run = True
    while run:
        win.fill((0,0,0))
        draw_text_middle(win, 'Press Any Key To Play', 60, (255,255,255))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                main(win)
    pygame.display.quit()

win = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption('Tetris')
main_menu(win)