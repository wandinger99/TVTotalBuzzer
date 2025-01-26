import pygame
from typing import Tuple
from Object import Object

class Rectangle(Object):
    def __init__(self, position: pygame.Vector2, 
                 visible=True, 
                 size: Tuple[int, int] = (20, 10), 
                 color: pygame.Color = pygame.Color("white")):
        super().__init__(position, visible)
        self._size = size  # Private attribute for size (width, height)
        self._color = color  # Private attribute for color

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
        """Getter for the rectangle's color."""
        return self._color

    @color.setter
    def color(self, new_color: pygame.Color):
        """Setter for the rectangle's color."""
        if not isinstance(new_color, pygame.Color):
            raise TypeError("Color must be a pygame.Color object.")
        self._color = new_color

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

    def handle_key_press(self, key: int):
        """
        Handles key press events to change the rectangle's color.

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
        """Draw the rectangle on the given screen."""
        if self.visible:
            pygame.draw.rect(screen, 
                             self.color, 
                             pygame.Rect(int(self.position.x), 
                                         int(self.position.y), 
                                         self._size[0], 
                                         self._size[1]))
