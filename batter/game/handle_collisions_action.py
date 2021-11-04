from game.counter import Counter
from game.point import Point
from game import constants

class HandleCollisionsAction():
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller

    Attributes:
        __counter (Counter): An instance of the counter class.
        __constants: Some constants.
    """
    def __init__(self):
        """The class constructor

        """
        self.__counter = Counter()
        self.__constants = constants

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        ball = cast["ball"][0] # there's only one
        paddle = cast["paddle"][0] # there's only one
        bricks = cast["brick"]

        ball_y = ball.get_position().get_y()
        ball_x = ball.get_position().get_x()
        ball_xy = ball.get_position()
        
        for brick in bricks:
            #If the ball hits a brick:
            if ball.get_position().equals(brick.get_position()):
                bricks.remove(brick)
                self.__counter.increment()
                ball.invert_y_velocity()

        #If the ball hits the paddle:
        paddle_x = []
        for x in range(self.__constants.PADDLE_WIDTH):
            #Getting al the x coordinates of the paddle
            paddle_x.append(paddle.get_position().get_x() + x)

        if ball_y == paddle.get_position().get_y() - 1:
            if ball_x in paddle_x:
                #If the ball hits the first half of the paddle:
                if ball_x <= paddle_x[int(round(self.__constants.PADDLE_WIDTH / 2))]:
                    #The ball goes to the left
                    ball.set_x_velocity(-1)
                else:
                    #The ball goes to the right
                    ball.set_x_velocity(1)
                ball.invert_y_velocity()

        #If the ball hits the top of the screen:
        if ball_y == 1:
            if ball.get_velocity().get_x() > 0:
                new_position = ball.get_position().add(Point(1, 0))
            else:
                new_position = ball.get_position().add(Point(-1, 0))
            ball.set_position(new_position)
            ball.invert_y_velocity()
        
        #If the ball hits the bottom of the screen:
        if ball_y == self.__constants.MAX_Y - 1:
            self.__counter.decrement_lives()
            ball.set_position(Point(int(self.__constants.MAX_X / 2), int(self.__constants.MAX_Y / 2)))
            ball.set_velocity(Point(1, -1))
        
        #If the ball hits the left side of the screen:
        if (ball_x == 1 
            or 
            ball_x == self.__constants.MAX_X - 1):
            ball.invert_x_velocity()

