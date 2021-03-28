import pygame
import level
import math

class Enemy(pygame.sprite.Sprite):

    """
    Represents an Enemy within the Game State System.
    
    Can move, jump, kill (soon), die; follows player

    Attributes
    ----------
    PyGame Sprite - controllable object


    Methods
    ----------
    __init__():
        Program initialisation.

    update():
        Updates state.

    draw():
        Draws images onto game panel.

    attack():
        Attack method of enemy.

    die():
        Kills enemy based on health.
   
    """

    def __init__(self):

        """
        Initialization of all variables and Sprite.

        Parameters
        ----------
        None

        Raises
        ----------
        None

        Authors
        ----------
        Aidan Traboulay
        """ 

        pygame.sprite.Sprite.__init__(self)

        self.rect = self.image.get_rect()

        self.rect.x = 0 #Adjust to spawn randomly - need screen size
        self.rect.y = 0

        #check level and adjust velocity and acceleration accordingly - static for now
        self.xVel = 0
        self.yVel = 0

        #Implement acceleration based on levels eventually
        self.xAccel = 0
        self.yAccel = 0

        self.jumping = False
        self.falling = True

        #Initializations to be implemented later on
        self.health = 0
        self.difficulty = 0


    def follow_player(self, player):

        """
        Basic algorithm to follow player
        - ghetto version
        - will implement a better one using vectors

        Parameters
        ----------
        None

        Raises
        ----------
        None

        Authors
        ----------
        Aidan Traboulay
        """ 

        if self.rect.x >= player.x:
            self.rect.x -= self.xVel

        if self.rect.x < player.x:
            self.rect.x += self.xVel

        return 
        
    def load_images(self):

        """
        Loads images onto frame to be drawn.

        Parameters
        ----------
        None

        Raises
        ----------
        None

        Authors
        ----------
        Aidan Traboulay
        """ 

        return

    def draw(self):

        """
        Draws onto game panel and updates screen.

        Parameters
        ----------
        None

        Raises
        ----------
        None

        Authors
        ----------
        Aidan Traboulay
        """ 

        return

    def attack(self):

        """
        Implements attack functionality for enemy.

        Parameters
        ----------
        None

        Raises
        ----------
        None

        Authors
        ----------
        Aidan Traboulay
        """ 

        #Check proximity of player to enemy first 

        #Check level for attack attributes
        
        #Determine damange level based on level

        #Update weapon images

        return

    def die(self):

        """
        Checks if enemy health is zero and updates sprite for level.

        Parameters
        ----------
        None

        Raises
        ----------
        None

        Authors
        ----------
        Aidan Traboulay
        """ 

        if self.health < 1:
            pass #To be implemented later on

        return
        
    def update(self):

        """
        Updates game logic, enemy movement and mechanics.

        Parameters
        ----------
        None

        Raises
        ----------
        None

        Authors
        ----------
        Aidan Traboulay
        """ 

        
        return