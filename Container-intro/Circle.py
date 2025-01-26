import pygame
from typing import Tuple
from Object import Object

class Circle(Object):
    def __init__(self, position: pygame.Vector2, 
                 visible=True, 
                 radius: int = 10, 
                 color: pygame.Color = pygame.Color("white"),
                 border_color: pygame.Color = pygame.Color("black"),
                 border_width: int = 1):
        super().__init__(position, visible)
        self._radius = radius  # Private attribute for radius
        self._color = color    # Private attribute for color
        self._border_color = border_color  # Private attribute for border color
        self._border_width = border_width  # Private attribute for border width

    @property
    def radius(self) -> int:
        """Getter for the radius of the circle."""
        return self._radius

    @radius.setter
    def radius(self, new_radius: int):
        """Setter for the radius of the circle."""
        if not isinstance(new_radius, int) or new_radius < 0:
            raise ValueError("Radius must be a non-negative integer.")
        self._radius = new_radius

    @property
    def color(self) -> pygame.Color:
        """Getter for the circle's fill color."""
        return self._color

    @color.setter
    def color(self, new_color: pygame.Color):
        """Setter for the circle's fill color."""
        if not isinstance(new_color, pygame.Color):
            raise TypeError("Color must be a pygame.Color object.")
        self._color = new_color

    @property
    def border_color(self) -> pygame.Color:
        """Getter for the circle's border color."""
        return self._border_color

    @border_color.setter
    def border_color(self, new_color: pygame.Color):
        """Setter for the circle's border color."""
        if not isinstance(new_color, pygame.Color):
            raise TypeError("Border color must be a pygame.Color object.")
        self._border_color = new_color

    @property
    def border_width(self) -> int:
        """Getter for the circle's border width."""
        return self._border_width

    @border_width.setter
    def border_width(self, new_width: int):
        """Setter for the circle's border width."""
        if not isinstance(new_width, int) or new_width < 0:
            raise ValueError("Border width must be a non-negative integer.")
        self._border_width = new_width

    def change_size(self, amount: int):
        """Changes the radius by the given amount (can be positive or negative)."""
        self.radius = max(0, self._radius + amount)

    def handle_key_press(self, event):
        """
        Handles key press and release events to change the circle's color.
        
        Args:
            event: The Pygame event object.
        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:  # If the '1' key is pressed
                self.color = pygame.Color("red")
            elif event.key == pygame.K_2:  # If the '2' key is pressed
                self.color = pygame.Color("green")
            elif event.key == pygame.K_3:  # If the '3' key is pressed
                self.color = pygame.Color("blue")

    def draw(self, screen: pygame.Surface):
        """Draw the circle on the given screen."""
        if self.visible:
            # Draw the filled circle
            pygame.draw.circle(screen, 
                               self.color, 
                               (int(self.position.x), int(self.position.y)), 
                               self.radius)
            # Draw the border if width > 0
            if self.border_width > 0:
                pygame.draw.circle(screen, 
                                   self.border_color, 
                                   (int(self.position.x), int(self.position.y)), 
                                   self.radius, 
                                   self.border_width)

