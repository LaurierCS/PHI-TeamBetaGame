import pygame

class Physics():

    """
    Represents the physics that are attributed to each tile on screen
    
    Contains a max speed, horizontal, and vertical acceleration allowed for an object affected by physics
    (e.g. enemies and the player) based on which tile type they are currently in contact with

    Attributes
    ----------
    maxSpeed - dictates the maximum speed the object can achieve in the tile
    xAccel - dictates the change in the object's horizontal speed in the tile
    yAccel - dictates the change in the object's vertical speed in the tile


    Methods
    ----------
    __init__():
        Program initialisation.
    """

    def __init__(self, maxSpeed, xAccel, yAccel):

        """
        Initialization of all variables

        Parameters
        ----------
        maxSpeed - the maximum speed for the object in the tile being utilized
        xAccel - the horizontal acceleration for the object in the tile being utilized
        yAccel - the vertical acceleration for the object in the tile being utilized

        Raises
        ----------
        None

        Authors
        ----------
        Branden Wheeler
        """ 
        self.maxSpeed = maxSpeed
        self.xAccel = xAccel
        self.yAccel = yAccel


