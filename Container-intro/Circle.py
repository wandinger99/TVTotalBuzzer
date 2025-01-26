import pygame
from typing import Tuple
from Object import Object

class Circle(Object):
    def __init__(self, position: pygame.Vector2, 
                 visible=True, 
                 radius: int = 10, 
                 color: pygame.Color = pygame.Color("white")):
        super().__init__(position, visible)
        self._radius = radius  # Private attribute for radius
        self._color = color    # Private attribute for color

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
        """Getter for the circle's color."""
        return self._color

    @color.setter
    def color(self, new_color: pygame.Color):
        """Setter for the circle's color."""
        if not isinstance(new_color, pygame.Color):
            raise TypeError("Color must be a pygame.Color object.")
        self._color = new_color

    def change_size(self, amount: int):
        """Changes the radius by the given amount (can be positive or negative)."""
        self.radius = max(0, self._radius + amount)

    def handle_key_press(self, key: int):
        """
        Handles key press events to change the circle's color.

        Args:
            key (int): The key code of the pressed key.
        """
        if key == pygame.K_1:  # If the '1' key is pressed
            self.color = pygame.Color("red")
        elif key == pygame.K_2:  # If the '2' key is pressed
            self.color = pygame.Color("green")
        elif key == pygame.K_3:  # If the '3' key is pressed
            self.color = pygame.Color("blue")

    def draw(self, screen: pygame.Surface):
        """Draw the circle on the given screen."""
        if self.visible:
            pygame.draw.circle(screen, 
                               self.color, 
                               (int(self.position.x), int(self.position.y)), 
                                self.radius)
