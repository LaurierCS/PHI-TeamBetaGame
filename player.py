from tile import Tile
from level import get_position_tile
import pygame

class Player(pygame.sprite.Sprite):

    """
    Represents a Player within the Game State System.
    
    Can move, jump, run (eventually), collect points (eventually), die (eventually)

    Attributes
    ----------
    PyGame Sprite - controllable object


    Methods
    ----------
    __init__():
        Program initialisation.

    set_location():
        Set initial position.

    draw():
        Draw to screen.

    load_images():
        Load images.

    update():
        State update.
    """

    def __init__(self, x, y):

        """
        Initialization of all variables and Sprite.

        Parameters
        ----------
        x - horizontal location
        y - vertical location

        Raises
        ----------
        None

        Authors
        ----------
        Aidan Traboulay
        """ 

        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y 
        self.tile = get_position_tile(x, y)

        #Player should be immobile on initialization
        self.x_vel = 0
        self.y_vel = 0

        self.jumping = False
        self.falling = True


    def set_location(self, x, y):

        """
        Sets location of sprite on frame.

        Parameters
        ----------
        x - horizontal location
        y - vertical location

        Raises
        ----------
        None

        Authors
        ----------
        Aidan Traboulay
        """ 

        #Start
        self.x = x
        self.y = y

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

        #Screen
        display = pygame.display.get_surface()


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

    def update(self, key):

        """
        Updates game logic, player movement and mechanics.

        Parameters
        ----------
        key

        Raises
        ----------
        None

        Authors
        ----------
        Aidan Traboulay
        Branden Wheeler
        """ 
        self.tile.physics.affect_things(self) #Update velocities for movement

        #Let player move left if pressing left and there is no solid tile where they want to go
        if key[pygame.K_LEFT] and get_position_tile(self.x-self.xVel, self.y).maxSpeed != 0:
            self.x -= self.x_vel
        #Let player move right if pressing right and there is no solid tile where they want to go
        elif key[pygame.K_RIGHT] and get_position_tile(self.x+self.xVel, self.y).maxSpeed != 0:
            self.x += self.x_vel
        else:
            self.x_vel = 0 #Sets velocity to 0 if they don't press a key or they run into a solid tile


        #If y_vel is not 0, the player is jumping or falling
        if self.y_vel != 0:
            #Only lets the player jump higher or fall further if there is
            #not a solid tile either above them or under them
            if get_position_tile(self.x, self.y-y_vel).maxSpeed != 0:
                self.y -= self.y_vel
            else:
                #Indicates the player fell on a solid tile so they are no longer jumping
                if self.y_vel < 0:
                    self.jumping = False
                self.y_vel = 0
                self.falling = False
        else:
            #If y_vel is 0 and the player is jumping, it indicates they've hit the peak
            #of their jump and are now falling
            if self.jumping:
                self.falling = True
            #If there is no solid tile under the player, they must begin falling
            if get_position_tile(self.x, self.y+1).maxSpeed != 0:
                self.y_vel -= self.tile.yAccel
                self.y += self.y_vel
                self.falling = True

        #Check falling or jumping
        if key[pygame.K_UP] and not self.jumping:
            self.jumping = True
            self.y_vel += self.tile.maxSpeed #Sets initial jump speed
        
        
        return

