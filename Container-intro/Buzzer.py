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
                in_color_inactive: pygame.Color = pygame.Color("green"),
                in_color_active: pygame.Color = pygame.Color("red"),
                out_color: pygame.Color = pygame.Color("gray"),
                trigger_key: str = '1'   # Which key triggers color change
                ):
        super().__init__(position, visible)
        self._size = size  # Tuple for width and height
        self._in_color = in_color
        self._in_color_inactive = in_color_inactive
        self._in_color_active = in_color_active
        self._out_color = out_color
        self._trigger_key = trigger_key
        
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

    @property
    def in_color(self) -> pygame.Color:
        """Getter for the inner color of the buzzer when inactive."""
        return self._in_color
    
    @in_color.setter
    def in_color(self, new_color: pygame.Color):
        """Setter for the inner color of the buzzer."""
        if not isinstance(new_color, pygame.Color):
            raise TypeError("Inner color must be a pygame.Color object.")
        self._in_color = new_color

    # Getter und Setter für die innere Farbe (in_color_inactive)
    @property
    def in_color_inactive(self) -> pygame.Color:
        """Getter for the inner color of the buzzer when inactive."""
        return self._in_color_inactive
    
    @in_color_inactive.setter
    def in_color_inactive(self, new_color: pygame.Color):
        """Setter for the inner color of the buzzer when inactive."""
        if not isinstance(new_color, pygame.Color):
            raise TypeError("Inner color must be a pygame.Color object.")
        self._in_color_inactive = new_color

    # Getter und Setter für die innere Farbe (in_color_active)
    @property
    def in_color_active(self) -> pygame.Color:
        """Getter for the inner color of the buzzer when active."""
        return self._in_color_active
    
    @in_color_active.setter
    def in_color_active(self, new_color: pygame.Color):
        """Setter for the inner color of the buzzer when active."""
        if not isinstance(new_color, pygame.Color):
            raise TypeError("Inner color must be a pygame.Color object.")
        self._in_color_active = new_color

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

    # Getter und Setter für den Trigger-Key
    @property
    def trigger_key(self) -> str:
        """Getter for the trigger key."""
        return self._trigger_key
    
    @trigger_key.setter
    def trigger_key(self, new_key: str):
        """Setter for the trigger key."""
        if not isinstance(new_key, str):
            raise TypeError("Trigger key must be an integer.")
        self._trigger_key = new_key

    def handle_key_press(self, event):
        """
        Handles key press and release events to change the buzzer's inner color.
        
        Args:
            event: The Pygame event object.
        """
        # Dynamically convert the trigger_key to the correct Pygame key code
        trigger = getattr(pygame, 'K_' + self.trigger_key, None)  # Get the pygame key code from the string

        if trigger is None:
            return  # If the key code doesn't exist, do nothing

        if event.type == pygame.KEYDOWN:
            if event.key == trigger:  # If the trigger key is pressed
                self._in_color = self.in_color_active  # Change color to active
        elif event.type == pygame.KEYUP:
            if event.key == trigger:  # If the trigger key is released
                self._in_color = self.in_color_inactive  # Reset to inactive color when key is released

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
            circle = Circle(center, radius=width / 2 - 5, color=self.in_color)  # radius basiert auf der Breite
            
            # Zeichne beide Objekte
            square.draw(screen)
            circle.draw(screen)


    
