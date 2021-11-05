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
        
        self.handle_brick_collision(ball, ball_xy, bricks)

        self.handle_paddle_collision(ball, ball_x, ball_y, paddle)

        self.handle_screen_collision(ball, ball_x, ball_y)

    def handle_brick_collision(self, ball, ball_xy, bricks):
        """Handles the brick collision.

        Args:
            self: An instance of handle_collisions_action class.
            ball (Actor): The ball actor.
            ball_xy (Point): The ball position.
            bricks (list): The list of bricks.
        """
        for brick in bricks:
            if ball_xy.equals(brick.get_position()):
                bricks.remove(brick)
                self.__counter.increment()
                ball.invert_y_velocity()

    def handle_paddle_collision(self, ball, ball_x, ball_y, paddle):
        """Handles the paddle collision.

        Args:
            self: An instance of handle_collisions_action class.
            ball (Actor): The ball actor.
            ball_xy (Point): The ball position.
            paddle (Actor): The paddle actor.
        """
        paddle_x = []
        for x in range(self.__constants.PADDLE_WIDTH):
            #Getting al the x coordinates of the paddle
            paddle_x.append(paddle.get_position().get_x() + x)

        if ball_y == paddle.get_position().get_y() - 1:
            if ball_x in paddle_x:
                #If the ball hits the first half of the paddle:
                if ball_x <= paddle_x[int(round(self.__constants.PADDLE_WIDTH / 2)) - 2]:
                    #The ball goes to the left
                    ball.set_x_velocity(-1)
                else:
                    #The ball goes to the right
                    ball.set_x_velocity(1)
                ball.invert_y_velocity()
                paddle_v_x = paddle.get_velocity().get_x()
                if paddle_v_x != 0:
                    if ball_x > 2 and ball_x < self.__constants.MAX_X - 2:
                        ball.set_position(Point(ball_x + paddle_v_x, ball_y))

    def handle_screen_collision(self, ball, ball_x, ball_y):
        """Handles the screen collision.

        Args:
            self: An instance of handle_collisions_action class.
            ball (Actor): The ball actor.
            ball_x (int): The ball x position.
            ball_y (int): The ball y position.
        """
        #If the ball hits the top of the screen:
        if ball_y == 1:
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