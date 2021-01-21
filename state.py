class State:
    """
    Represents a state within the Game State System.
    
    A State represents a 'screen' that the player interacts with at a certain point a time.
    A State contains code to update its own logic, render its own assets, and receives events from the main game loop. A State should bundle things, 
    such as buttons, UI elements, AI, etc...


    Attributes
    ----------
    None


    Methods
    ----------
    __init__():
        Program initialisation.

    load():
        State load.

    update():
        Update State logic.

    render():
        Update State drawing.

    deload():
        State deload.

    key_down(key : str):
        Key pressed.

    key_up(key : str):
        Key released.

    mouse_down():
        Mouse clicked.

    mouse_up():
        Mouse unclicked.

    mouse_moved():
        Mouse moved.

    """
    
    def __init__(self):
        """
        Called on program initialisation to load everything needed by this game state.

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
        return

    
    def load(self):
        """
        Called when the Game State Manager is told to switch to this specific State.

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
        return


    def update(self):
        """
        Called once per frame to update everything related to logic and calculations for the current state of the game.

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
        return


    def render(self):
        """
        Called once per frame to update the screen with the current frame of the current state of the game.

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
        return


    def deload(self):
        """
        Called when the Game State Manager is told to switch from this specific State to another State.

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
        return


    def key_down(self, key):
        """
        Called during a frame when a key is pressed down.

        Parameters
        ----------
        key : str
            The key that has been pressed.

        Raises
        ----------
        None

        Authors
        ----------
        Nausher Rao
        """ 
        return


    def key_up(self, key):
        """
        Called during a frame when a key is released.

        Parameters
        ----------
        key : str
            The key that has been released.

        Raises
        ----------
        None

        Returns
        ----------
        None

        Authors
        ----------
        Nausher Rao
        """ 
        return


    def mouse_down(self):
        """
        Called during a frame when a mouse button is pressed down.

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
        return


    def mouse_up(self):
        """
        Called during a frame when a mouse button is released.

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
        return


    def mouse_moved(self):
        """
        Called during a frame when the mouse pointer is moved.

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
        return 