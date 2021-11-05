class DrawActorsAction():
    """A code template for drawing actors. The responsibility of this class of
    objects is use an output service to draw all actors on the screen.
    
    Stereotype:
        Controller

    Attributes:
        _output_service (OutputService): An instance of OutputService.
    """

    def __init__(self, output_service):
        """The class constructor.
        
        Args:
            output_service (OutputService): An instance of OutputService.
        """
        self._output_service = output_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            self: The instance of the draw actors action class
            cast (dict): The game actors {key: tag, value: list}.
        """
        self._output_service.clear_screen()
        
        for group in cast.values():
            self._output_service.draw_actors(group)

        self._output_service.flush_buffer()

    def print_game_over(self):
        """Prints the game over message.
        
        Args:
            self: The instance of the draw actors action class
        """
        self._output_service.print_game_over()

    def print_congrats(self):
        """Prints the congratulations message.
        
        Args:
            self: The instance of the draw actors action class
        """
        self._output_service.print_congrats()