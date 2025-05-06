
# setting up pygame
import pygame 
pygame.init()
pygame.display.set_caption("Battleship")

# global variables
SQ_SIZE = 35
H_MARGIN = SQ_SIZE * 2
V_MARGIN = SQ_SIZE * 2
WIDTH = SQ_SIZE * 10 * 2 + H_MARGIN 
HEIGHT = SQ_SIZE * 10 * 2 + V_MARGIN
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# COLORS
GREY = (40, 50, 60)
WHITE = (255, 250, 250)

# function to draw the grid
def draw_grid(left = 0, top = 0):
    for i in range(100):
        x = left + i % 10 * SQ_SIZE
        y = top + i // 10 * SQ_SIZE
        square = pygame.Rect(x, y, SQ_SIZE, SQ_SIZE)
        pygame.draw.rect(SCREEN, WHITE, square, width = 2)



# pygame loop
animating = True
pausing = False
while animating:

    # track user interaction
    for event in pygame.event.get():

        # user closes the pygame window
        if event.type == pygame.QUIT:
            animating = False
        
        # user presses a key on keyboard
        if event.type == pygame.KEYDOWN:

            # escape key to close animation
            if event.key == pygame.K_ESCAPE:
                animating = False

            # space bar to pause and unpause the animation
            if event.key == pygame.K_SPACE:
                pausing = not pausing
                print(pausing)

    # execution
    if not pausing: 

        # draw background
        SCREEN.fill(GREY)

        # draw search grids
        draw_grid()
        draw_grid(left = (WIDTH - H_MARGIN) // 2 + H_MARGIN, top = (HEIGHT - V_MARGIN) // 2 + V_MARGIN)
        
        # draw position grids
        draw_grid(top = (HEIGHT - V_MARGIN) // 2 + V_MARGIN)
        draw_grid(left = (WIDTH - H_MARGIN) // 2 + H_MARGIN)

        # update display
        pygame.display.flip() 