import pygame
import random

pygame.font.init()

# GLOBALS VARS
s_width = 800
s_height = 700
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 30 height per block
block_size = 30

top_left_x = (s_width - play_width) // 2 
top_left_y = s_height - play_height


# SHAPE FORMATS
S = [['.....',
      '.....',
      '..00.',
      '.00..',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['.....',
      '..0..',
      '..0..',
      '..0..',
      '..0..'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.....',
      '.0...',
      '.000.',
      '.....'],
     ['.....',
      '.....',
      '..00.',
      '..0..',
      '..0..'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '.....',
      '..0..',
      '.000.',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

#The shapes you want to drop
shapes = [S, Z, I, O, J, L, T]

#colors for the shapes
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), 
(255, 165, 0), (0, 0, 255), (128, 0, 128)]
class Tetris(object):  # *
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0

def create_grid(locked_pos={}): 
    #Initialize a grid variable as a multidimensional list, 
    #each list contains 20 sublists - representing 20 rows, each sublist contains 10 elements
    #Each element in the sublist represents the color of that cell and has the form (0,0,0) - black
    grid = [[(0,0,0) for _ in range(10)] for _ in range(20)]

    for i in range(len(grid)): #traverse 20 rows
        for j in range(len(grid[i])): #traverse each cell in each row
            #locked_pos ={} is a dictionary data type in python, each element is a key-value pair, 
            #where key will be the position of the cell in the table, and value is the color of that cell
            if (j, i) in locked_pos:
                #The locked position parameter c = locked_pos ={[j,i]} contains the position of the falling block in the game board and its color, 
                #assign grid[i][j] = c => find the corresponding position respond in the game board with a locked position and change color
                c = locked_pos[(j,i)]
                grid[i][j] = c
    return grid

def get_shape():
    #Returns any block shape to drop and drop position x = 5, y = 0 in game board
    return Tetris(5, 0, random.choice(shapes))

def convert_shape_format(shape):
    positions = []
    #different shapes of 1 block, each block has up to 4 different shapes
    format = shape.shape[shape.rotation % len(shape.shape)]

    #i is index only, line is each element in "format"
    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                positions.append((shape.x + j, shape.y + i))

    #move the drop-down block to the center
    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 2)

    return positions

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

    #
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j*block_size, top_left_y + 
            i*block_size, block_size, block_size), 0)

    #draw contours around the cells
    pygame.draw.rect(surface, (0,128,128), (top_left_x, top_left_y, play_width, play_height), 5)

    draw_grid(surface, grid)

def main(win):  # *
    run = True
    change_piece = False
    locked_positions = {}
    clock = pygame.time.Clock()
    current_piece = get_shape()
    fall_time = 0
    fall_speed = 0.27 #falling speed
    while run:
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime() #time falls
        clock.tick()


        if fall_time/1000 > fall_speed:
            fall_time = 0
            current_piece.y += 1

        #catch keypress events from keyboard
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                if event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                if event.key == pygame.K_DOWN:
                    current_piece.y += 1
                if event.key == pygame.K_UP:
                    current_piece.rotation += 1
        shape_pos = convert_shape_format(current_piece)

        #add color to the blocks
        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.color
        draw_window(win, grid, 0, str(0))
        pygame.display.update()

def main_menu(win):  
    while True:
        win.fill((0,0,0))
        main(win)
        pygame.display.update()

win = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption('Tetris')
main_menu(win)