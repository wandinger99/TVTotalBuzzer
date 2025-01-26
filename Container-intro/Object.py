import pygame
from abc import ABC, abstractmethod
from typing import Tuple

class Object:
    def __init__(self, position: pygame.Vector2, 
                 visible=True):
        self._position = position  # Private attribute for position
        self._visible = visible    # Private attribute for visibility

    @property
    def position(self) -> pygame.Vector2:
        """Getter for the position."""
        return self._position

    @position.setter
    def position(self, new_position: pygame.Vector2):
        """Setter for the position."""
        if not isinstance(new_position, pygame.Vector2):
            raise TypeError("Position must be a pygame.Vector2 object.")
        self._position = new_position

    @property
    def visible(self) -> bool:
        """Getter for the visibility."""
        return self._visible

    @visible.setter
    def visible(self, is_visible: bool):
        """Setter for the visibility."""
        if not isinstance(is_visible, bool):
            raise TypeError("Visible must be a boolean value.")
        self._visible = is_visible

    def toggle_visibility(self):
        """Toggles the visibility of the object."""
        self._visible = not self._visible
    
    @abstractmethod
    def draw(self, screen: pygame.Surface):
        """
        Abstract method to draw the object on the screen.
        Must be implemented by subclasses.
        """
        pass

    @abstractmethod
    def handle_key_press(self, key: int):
        """
        Abstract method to draw the object on the screen.
        Must be implemented by subclasses.
        """
        pass
