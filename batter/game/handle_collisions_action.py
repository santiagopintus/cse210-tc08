import random
from game import constants

class HandleCollisionsAction():
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        ball = cast["ball"][0] # there's only one
        brick = cast["brick"][0] # there's only one
        bricks = cast["brick"]
        
        for brick in bricks:
            if ball.get_position().equals(brick.get_position()):
                print("collision removing brick")
                bricks.remove(brick)
                print("increase score")