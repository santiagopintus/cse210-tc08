from game import constants
from game.point import Point

class Actor:
    """A visible, moveable thing that participates in the game. The responsibility of Actor is to keep track of its appearance, position 
    and velocity in 2d space.

    Stereotype:
        Information Holder

    Attributes:
        _text (string): The textual representation of the actor.
        _position (Point): The actor's position in 2d space.
        _velocity (Point): The actor's speed and direction.
    """

    def __init__(self):
        """The class constructor."""
        self._text = ""
        self._position = Point(0, 0)
        self._velocity = Point(0, 0)

    def get_position(self):
        """Gets the actor's position in 2d space.
        
        Returns:
            Point: The actor's position in 2d space.
        """
        return self._position
    
    def get_text(self):
        """Gets the actor's textual representation.
        
        Returns:
            string: The actor's textual representation.
        """
        return self._text

    def get_velocity(self):
        """Gets the actor's speed and direction.
        
        Returns:
            Point: The actor's speed and direction.
        """
        return self._velocity

    def set_position(self, position):
        """Updates the actor's position to the given one.
        
        Args:
            position (Point): The given position.
        """
        self._position = position
    
    def set_text(self, text):
        """Updates the actor's text to the given value.
        
        Args:
            text (string): The given value.
        """
        self._text = text

    def set_velocity(self, velocity):
        """Updates the actor's velocity to the given one.
        
        Args:
            velocity (Point): The given velocity.
        """
        self._velocity = velocity
    
    def set_x_velocity(self, x):
        """Sets the actor's x velocity to the given one.
        
        Args:
            x (int): The given value.
        """
        self._velocity = Point(x, self._velocity.get_y())
        self.set_velocity(self._velocity)

    def invert_velocity(self):
        """Inverts the actor's velocity."""
        self._velocity = Point(-self._velocity.get_x(), -self._velocity.get_y())
        self.set_velocity(self._velocity)

    def invert_y_velocity(self):
        """Inverts the actor's y velocity."""
        self._velocity = Point(self._velocity.get_x(), -self._velocity.get_y())
        self.set_velocity(self._velocity)

    def invert_x_velocity(self):
        """Inverts the actor's x velocity."""
        self._velocity = Point(-self._velocity.get_x(), self._velocity.get_y())
        self.set_velocity(self._velocity)