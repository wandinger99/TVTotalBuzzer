import pygame
from typing import Tuple
from Object import Object

class Rectangle(Object):
    def __init__(self, position: pygame.Vector2, 
                 visible=True, 
                 size: Tuple[int, int] = (20, 10), 
                 color: pygame.Color = pygame.Color("white"),
                 border_color: pygame.Color = pygame.Color("black"),
                 border_width: int = 1):
        super().__init__(position, visible)
        self._size = size  # Private attribute for size (width, height)
        self._color = color  # Private attribute for fill color
        self._border_color = border_color  # Private attribute for border color
        self._border_width = border_width  # Private attribute for border width

    @property
    def size(self) -> Tuple[int, int]:
        """Getter for the rectangle's size (width, height)."""
        return self._size

    @size.setter
    def size(self, new_size: Tuple[int, int]):
        """Setter for the rectangle's size."""
        if (not isinstance(new_size, tuple) or 
            len(new_size) != 2 or 
            not all(isinstance(dim, int) and dim >= 0 for dim in new_size)):
            raise ValueError("Size must be a tuple of two non-negative integers (width, height).")
        self._size = new_size

    @property
    def color(self) -> pygame.Color:
        """Getter for the rectangle's fill color."""
        return self._color

    @color.setter
    def color(self, new_color: pygame.Color):
        """Setter for the rectangle's fill color."""
        if not isinstance(new_color, pygame.Color):
            raise TypeError("Color must be a pygame.Color object.")
        self._color = new_color

    @property
    def border_color(self) -> pygame.Color:
        """Getter for the rectangle's border color."""
        return self._border_color

    @border_color.setter
    def border_color(self, new_color: pygame.Color):
        """Setter for the rectangle's border color."""
        if not isinstance(new_color, pygame.Color):
            raise TypeError("Border color must be a pygame.Color object.")
        self._border_color = new_color

    @property
    def border_width(self) -> int:
        """Getter for the rectangle's border width."""
        return self._border_width

    @border_width.setter
    def border_width(self, new_width: int):
        """Setter for the rectangle's border width."""
        if not isinstance(new_width, int) or new_width < 0:
            raise ValueError("Border width must be a non-negative integer.")
        self._border_width = new_width

    def change_size(self, width_delta: int, height_delta: int):
        """
        Changes the rectangle's size by the given deltas.

        Args:
            width_delta (int): Change in width (can be positive or negative).
            height_delta (int): Change in height (can be positive or negative).
        """
        new_width = max(0, self._size[0] + width_delta)
        new_height = max(0, self._size[1] + height_delta)
        self.size = (new_width, new_height)

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
        """Draw the rectangle on the given screen."""
        if self.visible:
            # Draw the filled rectangle
            pygame.draw.rect(screen, 
                             self.color, 
                             pygame.Rect(int(self.position.x), 
                                         int(self.position.y), 
                                         self._size[0], 
                                         self._size[1]))
            # Draw the border if width > 0
            if self.border_width > 0:
                pygame.draw.rect(screen, 
                                 self.border_color, 
                                 pygame.Rect(int(self.position.x), 
                                             int(self.position.y), 
                                             self._size[0], 
                                             self._size[1]), 
                                 self.border_width)
