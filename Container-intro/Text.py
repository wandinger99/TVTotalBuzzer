import pygame
from Object import Object

class Text(Object):
    def __init__(self, position: pygame.Vector2, 
                 visible=True, 
                 color: pygame.Color = pygame.Color("white"),
                 text: str = "no text",
                 fontsize: int = 36):
        super().__init__(position, visible)
        self._text = text  # Use private attributes for encapsulation
        self._color = color
        self._fontsize = fontsize

    @property
    def fontsize(self) -> int:
        """Getter for fontsize."""
        return self._fontsize

    @property
    def text(self) -> str:
        """Getter for the text content."""
        return self._text

    @fontsize.setter
    def fontsize(self, new_size: int):
        """Setter for the fontsize."""
        if not isinstance(new_size, int):
            raise TypeError("Text must be a int.")
        self._text = new_size

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
        """Draw the text on the given screen."""
        if self.visible:
            font = pygame.font.Font(None, self.fontsize)  # Default font and size
            text_surface = font.render(self.text, True, self.color)
            screen.blit(text_surface, 
                        (int(self.position.x), int(self.position.y)))