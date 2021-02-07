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

    def __init__(self, x, y, vel):

        """
        Initialization of all variables and Sprite.

        Parameters
        ----------
        x - horizontal location
        y - vertical location
        vel - velocity of player

        Raises
        ----------
        None

        Authors
        ----------
        Aidan Traboulay
        """ 

        pygame.sprite.Sprite.__init__(self)

        self.location = location
        self.vel = vel

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
        self.xVel = 0

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
        """ 

        #Horizontal
        if key[pygame.K_LEFT]:
            self.xVel = -self.vel

        elif key[pygame.K_RIGHT]:
            self.xVel = self.vel

        else:
            self.xVel = 0

        #Check falling or jumping
        if key[pygame.K_UP] and not self.jumping and not self.falling:
            self.jumping = True
        
        if self.jumping:
            self.y -= self.vel

        elif self.falling:
            self.y += self.vel
        
        return

