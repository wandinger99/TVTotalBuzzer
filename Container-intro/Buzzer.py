import pygame
from typing import Tuple
from Object import Object
from Circle import Circle
from Rectangle import Rectangle

class Buzzer(Object):
    def __init__(self, position, 
                 visible=True,
                 size: Tuple[int, int] = (50, 50),  # Buzzer should be square-shaped
                 in_color: pygame.Color = pygame.Color("green"),
                 out_color: pygame.Color = pygame.Color("gray")):
        super().__init__(position, visible)
        self._size = size  # Tuple for width and height
        self._in_color = in_color
        self._out_color = out_color
        
        # Falls position kein Vector2 ist, wird sie hier konvertiert
        if not isinstance(self.position, pygame.Vector2):
            self.position = pygame.Vector2(self.position)

    # Getter und Setter für die Größe (size)
    @property
    def size(self) -> Tuple[int, int]:
        """Getter for the size of the buzzer (width, height)."""
        return self._size
    
    @size.setter
    def size(self, new_size: Tuple[int, int]):
        """
        Setter for the size of the buzzer. 
        Ensures that the size is a tuple of two non-negative integers.
        """
        if (
            not isinstance(new_size, tuple) or 
            len(new_size) != 2 or 
            not all(isinstance(dim, int) and dim >= 0 for dim in new_size)
        ):
            raise ValueError("Size must be a tuple of two non-negative integers (width, height).")
        self._size = new_size

    # Getter und Setter für die innere Farbe (in_color)
    @property
    def in_color(self) -> pygame.Color:
        """Getter for the inner color of the buzzer."""
        return self._in_color
    
    @in_color.setter
    def in_color(self, new_color: pygame.Color):
        """Setter for the inner color of the buzzer."""
        if not isinstance(new_color, pygame.Color):
            raise TypeError("Inner color must be a pygame.Color object.")
        self._in_color = new_color

    # Getter und Setter für die äußere Farbe (out_color)
    @property
    def out_color(self) -> pygame.Color:
        """Getter for the outer color of the buzzer."""
        return self._out_color
    
    @out_color.setter
    def out_color(self, new_color: pygame.Color):
        """Setter for the outer color of the buzzer."""
        if not isinstance(new_color, pygame.Color):
            raise TypeError("Outer color must be a pygame.Color object.")
        self._out_color = new_color

    def handle_key_press(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:  # If the '1' key is pressed
                self.in_color = pygame.Color("red")
            elif event.key == pygame.K_2:  # If the '2' key is pressed
                self.in_color = pygame.Color("green")
        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_1:  # If the '1' key is released
                self.in_color = pygame.Color("green")  # Reset to green when the key is released


    def draw(self, screen: pygame.Surface):
        """Draw a buzzer. Square with a centered Circle inside"""
        if self.visible:
            # Größe als Tuple, daher Zugriff auf die einzelnen Dimensionen
            width, height = self.size  # Unpacking der Größe in width und height
            
            # Rechteck erstellen
            square = Rectangle(self.position, size=(width, height), color=self.out_color)
            
            # Berechnung des Zentrums, Annahme: self.position ist ein Vector
            center = self.position + pygame.Vector2(width / 2, height / 2)  # Vermeide direkte Tuple-Operationen
            
            # Kreis erstellen
            circle = Circle(center, radius=width / 2 -5 , color=self.in_color)  # radius basiert auf der Breite
            
            # Zeichne beide Objekte
            square.draw(screen)
            circle.draw(screen)

    
