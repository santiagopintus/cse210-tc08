class Director:

    def __init__(self, cast, script):
        """ An instance of Director is responsible for directing the other classes.
        Coordinates the game's flow and the game's actors.

        Attributes:
            cast (dictionary): A dictionary of actors in the game.
            script (dictionary): A dictionary of actions for the game.
        """
        self.cast = cast
        self.script = script