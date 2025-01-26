import pygame
from typing import Tuple

class Object:
    def __init__(self, position: pygame.Vector2, visible=True):
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
    
class Circle(Object):
    def __init__(self, position: pygame.Vector2, visible=True, 
                 radius: int = 10, color: pygame.Color = pygame.Color("white")):
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
        self.radius = max(0, self._radius + amount)  # Ensure radius is non-negative

class Text(Object):
    def __init__(self, position: pygame.Vector2, visible=True, 
                 color: pygame.Color = pygame.Color("white"),
                 text: str = "no text"):
        super().__init__(position, visible)
        self._text = text  # Use private attributes for encapsulation
        self._color = color

    @property
    def text(self) -> str:
        """Getter for the text content."""
        return self._text

    @text.setter
    def text(self, new_text: str):
        """Setter for the text content."""
        if not isinstance(new_text, str):
            raise TypeError("Text must be a string.")
        self._text = new_text

    @property
    def color(self) -> pygame.Color:
        """Getter for the text color."""
        return self._color

    @color.setter
    def color(self, new_color: pygame.Color):
        """Setter for the text color."""
        if not isinstance(new_color, pygame.Color):
            raise TypeError("Color must be a pygame.Color object.")
        self._color = new_color
    






# Example Usage
if __name__ == "__main__":
    position = pygame.Vector2(100, 100)
    circle = Circle(position, radius=20, color=pygame.Color("blue"))
    circle.bigger(10)
    circle.smaller(5)
    print(f"Circle position: {circle.pos()}, radius: {circle.get_radius()}, color: {circle.color}")

    
