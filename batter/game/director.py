from time import sleep
from game import constants

class Director:

    def __init__(self, cast, script):
        """ An instance of Director is responsible for directing the other classes.
        Coordinates the game's flow and the game's actors.

        Attributes:
            cast (dictionary): A dictionary of actors in the game.
            script (dictionary): A dictionary of actions for the game.
            keep_playing (boolean): A boolean that determines if the game should continue.
            constants: Contains the constants for the game.
        """
        self.__cast = cast
        self.__script = script
        self.__keep_playing = True
        self.__user_won = True
        self.__constants = constants

    def start_game(self):
        """Starts the game!
        """
        while self.__keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
            sleep(self.__constants.FRAME_LENGTH)

        if self.__user_won:
            self.print_congrats()
        else:
            self.print_game_over()


    def get_inputs(self):
        """Gets the inputs from the user.

        Args:
            self: An instance of the Director class.
        """
        #Setting direction
        self.__script["input"][0].execute(self.__cast)

    def do_updates(self):
        """Does the updates to the game.

        Args:
            self: An instance of the Director class.
        """
        for script in self.__script["update"]:
            script.execute(self.__cast)
        self.__keep_playing, self.__user_won = self.__script["update"][1].get_final_results()
            
    def do_outputs(self):
        """Does the outputs to the user.

        Args:
            self: An instance of the Director class.
        """
        self.__script["output"][0].execute(self.__cast)

    def print_game_over(self):
        """Prints the game over message.

        Args:
            self: An instance of the Director class.
        """
        self.__script["output"][0].print_game_over()

    def print_congrats(self):
        """Prints the congratulations message.

        Args:
            self: An instance of the Director class.
        """
        self.__script["output"][0].print_congrats()
