from tempfile import tempdir
import pygame

HEIGHT = 1200
WIDTH = 800
WIN = pygame.display.set_mode((HEIGHT, WIDTH))

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class block:
    def __init__(self, row, y, width, color):
        self.x = row * width
        self.y = y
        self.color = color
        self.width = width
    
    def draw(self):
        pygame.draw.rect(WIN, self.color, (self.x, self.y, self.width, WIDTH - self.y))
        pygame.draw.rect(WIN, BLACK, (self.x, 0, self.width, self.y))
        pygame.draw.line(WIN, BLACK, (self.x + self.width, 0), (self.x + self.width, WIDTH))
        pygame.draw.line(WIN, BLACK, (self.x, 0), (self.x, WIDTH))
        pygame.display.update()
        
        

def draw_all(Grid):
    for node in Grid:
        node.draw()
        
        
def bubblesort(Grid):
    for i in range(len(Grid)):
        for j in range(len(Grid)-i-1):
            if Grid[j].y > Grid[j+1].y:
                temp = Grid[j+1].y
                Grid[j+1].y = Grid[j].y
                Grid[j].y = temp
                Grid[j].color = RED
                Grid[j].draw()
                Grid[j].color = BLUE
                Grid[j].draw()
        Grid[len(Grid)-1-i].color = GREEN
        Grid[len(Grid)-1-i].draw()
        
        
       

def main():
    n = 200
    width = HEIGHT // n
    Grid = []
    clk = pygame.time.Clock()
    for i in range(n+1):
        Grid.append(block(i, WIDTH, width, BLACK))
    
    while True:
        for event in pygame.event.get():
            if pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                x = x // width
                Grid[x].y = y
                Grid[x].color = BLUE
                Grid[x].draw()
                
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bubblesort(Grid)
                    draw_all(Grid)
        
        

main()
        