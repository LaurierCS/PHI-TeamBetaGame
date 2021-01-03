import pygame
import pygame.sprite

from pygame import Rect
from random import randint
from random import randrange
from State import State

class GameState(State):


    def __init__(self, main):  
        super().__init__()         
        self.app = main
        self.boundary = Rect(0, 0, self.app.width, self.app.height)

        self.dirX = 0
        self.dirY = 0
        self.foodX = randint(round(self.app.width * 0.05), round(self.app.width * 0.95))
        self.foodY = randint(round(self.app.height * 0.05), round(self.app.height * 0.95))

        self.snake = []
        self.snakeWidth = 50
        self.snakeSprites = pygame.sprite.Group()
        self.speed = 5

        self.snake.append( (self._generate_color(), 100, 100) )
        return


    def update(self):
        super().update()
        for i in range(len(self.snake)):
            self.snake[i] = (self.snake[i][0], self.snake[i][1] + self.dirX, self.snake[i][2] + self.dirY)
            if(not self.boundary.contains( Rect(self.snake[i][0], self.snake[i][1], self.snakeWidth, self.snakeWidth) )):
                self.app.quit()

        return


    def render(self):
        super().render()
        pygame.draw.rect(self.app.screen, (0,255,0), (self.foodX, self.foodY, self.snakeWidth, self.snakeWidth))

        for x in self.snake:
            pygame.draw.rect(self.app.screen, x[0], (x[1], x[2], self.snakeWidth, self.snakeWidth))

        return


    def key_down(self, key):
        super().key_down(key)
        if(key == pygame.K_w or key == pygame.K_UP):
            self.dirY = -self.speed
            self.dirX = 0

        elif(key == pygame.K_a or key == pygame.K_LEFT):
            self.dirX = -self.speed
            self.dirY = 0

        elif(key == pygame.K_s or key == pygame.K_DOWN):
            self.dirY = +self.speed
            self.dirX = 0

        elif(key == pygame.K_d or key == pygame.K_RIGHT):  
            self.dirX = +self.speed
            self.dirY = 0

        elif(key == pygame.K_ESCAPE):
            self.app.quit()

        else:
            return 


    def _generate_color(self):
        return pygame.Color(randint(0, 255), randint(0, 255), randint(0, 255))
