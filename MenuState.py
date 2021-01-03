import pygame
import pygame.freetype
import os

from pygame import Rect
from State import State

class MenuState(State):


    def __init__(self, main):
        super().__init__()
        self.app = main

        self.title_img = pygame.image.load("assets/title.png").convert()
        self.start_default_img = pygame.image.load("assets/start_default.png").convert()
        self.start_hover_img = pygame.image.load("assets/start_hover.png").convert()
        self.quit_default_img = pygame.image.load("assets/quit_default.png").convert()
        self.quit_hover_img = pygame.image.load("assets/quit_hover.png").convert()

        self.title_rect = Rect(self.app.width/2 - 512/2, self.app.height / 8, self.title_img.get_width(), self.title_img.get_height())
        self.start_rect = Rect(self.app.width/2 - 384/2, self.app.height / 2, self.start_default_img.get_width(), self.start_default_img.get_height())
        self.quit_rect = Rect(self.app.width/2 - 384/2, self.app.height / 1.35, self.quit_default_img.get_width(), self.quit_default_img.get_height())
        return 


    def render(self):
        super().render()
        self.app.screen.blit(self.title_img, self.title_rect)
        self.app.screen.blit(self.start_default_img, self.start_rect)
        self.app.screen.blit(self.quit_default_img, self.quit_rect)
        return 


    def mouse_down(self):
        mousePos = pygame.mouse.get_pos()
        if( self.start_rect.collidepoint(mousePos) ):
            self.app.currentState = self.app.states['game']
        
        elif( self.quit_rect.collidepoint(mousePos) ):
            self.app.quit()

        else:
            return