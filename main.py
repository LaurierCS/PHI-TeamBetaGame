import pygame

import sys
import logging
import yaml

from state import State

#Sprites
from enemy import Enemy
from player import Player

class Main:
    """
    The main code for the game. 

    The Main class contains code pertaining to the main game loop, which interacts with every other components
    of the game for every frame of the game. The class also loads some values from a configuration file that the 
    user can interact with. This class also acts as the Game State Manager for every state in the game.


    Attributes
    ----------
    running : bool
        Whether or not the game loop should be executing.

    debug : bool
        Whether or not the game is in debug mode.

    screen : Surface
        The main game screen.

    clock : Clock
        Controls the frames per second and delta values for each frame.

    states : dict[State]
        Stores every state that 

    current_state: State
        The current State managed by the Game State Manager.


    Methods
    ----------
    __init__():
        Program initialisation.

    tick():
        Update game.

    render():
        Render game.

    quit():
        Close game.
    """


    def __init__(self):
        """
        Called before anything game related is happening. Sets up the execution of the game loop.

        Parameters
        ----------
        None


        Raises
        ----------
        None


        Authors
        ----------
        Nausher Rao
        """ 
        logging.basicConfig(level=logging.DEBUG)
        logging.info("Starting program")

        pygame.init()
        pygame.display.set_caption("Test Game")
        
        self.running = True
        self.debug = False
        self.screen = pygame.display.set_mode([self.width, self.height])
        self.clock = pygame.time.Clock()
        self.width = 1366
        self.height = 768
        self.target_fps = 60
        
        self.states = {} #TODO: Add more states
        self.current_state = None; #TODO: Set state as soon as we have some states 

        #Create group for sprites
        self.sprite_group = pygame.sprite.Group()

        #Initialize player and enemy objects; add to group
        self.player = Player()
        self.enemy = Enemy()

        self.sprite_group.add(self.player)
        self.sprite_group.add(self.enemy)

        while(self.running):
            self.tick()
            self.render()

        self.quit()
        return


    def tick(self):
        """
        Called once per frame to update evrything related to updating logic involving the game.

        Parameters
        ----------
        None


        Raises
        ----------
        None


        Authors
        ----------
        Nausher Rao
        """ 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_h):
                    self.debug = not self.debug

                self.current_state.key_down(event.key)

            elif(event.type == pygame.KEYUP):
                self.current_state.key_up(event.key)

            elif(event.type == pygame.MOUSEBUTTONDOWN):
                self.current_state.mouse_down()

            elif(event.type == pygame.MOUSEBUTTONUP):
                self.current_state.mouse_up()

            else:
                continue

        self.current_state.update()
        self.clock.tick(self.target_fps)
        return 


    def render(self):
        """
        Called once per frame to update everything related to updating the screen.

        Parameters
        ----------
        None


        Raises
        ----------
        None


        Authors
        ----------
        Nausher Rao
        """ 
        
        self.screen.fill((0, 0, 0))
        self.current_state.render()
        if(self.debug):
            print('debug')
            #TODO: Draw debug info
        
        pygame.display.flip()
        return


    def quit(self): 
        """
        Executes when the program wants to terminate.

        Parameters
        ----------
        None


        Raises
        ----------
        None


        Authors
        ----------
        Nausher Rao
        """ 
        #TODO: Save settings
        logging.info("Quitting game")
        pygame.quit()
        sys.exit()
        return 


# Starts the Python program
if( __name__ == "__main__"):
    Main()