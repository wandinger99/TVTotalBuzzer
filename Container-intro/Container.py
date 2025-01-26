import pygame
import logging
from typing import List
from Object import Object
from Circle import Circle
from Text import Text


class Container(Object):
    """
    Represents a container that manages a list of objects.
    It can add or remove objects of the `Object` class.
    """
    def __init__(self, 
                 position: pygame.Vector2 = pygame.Vector2(0, 0), 
                 visible: bool = True):
        super().__init__(position, visible)
        self._objects: List[Object] = []

    def add_object(self, obj: Object):
        """Adds an object to the container."""
        if not isinstance(obj, Object):
            raise TypeError("Only instances of Object can be added.")
        self._objects.append(obj)
        logging.info(f"Added object at position {obj.position}. Total objects: {len(self._objects)}")

    def remove_object(self, obj: Object):
        """Removes an object from the container if it exists."""
        if obj in self._objects:
            self._objects.remove(obj)
            logging.info(f"Removed object from position {obj.position}. Total objects: {len(self._objects)}")
        else:
            logging.warning("Attempted to remove an object that is not in the container.")

    def clear_objects(self):
        """Removes all objects from the container."""
        count = len(self._objects)
        self._objects.clear()
        logging.info(f"Cleared all objects from the container. Removed {count} objects.")

    def get_objects(self) -> List[Object]:
        """Returns the list of objects in the container."""
        return self._objects

    def __len__(self) -> int:
        """Returns the number of objects in the container."""
        return len(self._objects)

    @property
    def visible(self) -> bool:
        """Getter for visibility."""
        return self._visible

    @visible.setter
    def visible(self, is_visible: bool):
        """Setter for visibility. Applies recursively to contained objects."""
        self._visible = is_visible
        for obj in self._objects:
            obj.visible = is_visible  # Ensure contained objects match visibility


    

if __name__ == "__main__":
    # Initialize pygame to use Vector2 and Color.
    pygame.init()

    # Create a container
    container = Container()

    # Create objects
    obj1 = Object(pygame.Vector2(10, 20))
    obj2 = Circle(pygame.Vector2(30, 40), radius=15, color=pygame.Color("blue"))
    obj3 = Text(pygame.Vector2(50, 60), text="Hello, world!", color=pygame.Color("green"))

    # Add objects to the container
    container.add_object(obj1)
    container.add_object(obj2)
    container.add_object(obj3)

    # Print the current objects
    logging.info(f"Current objects in container: {container.get_objects()}")

    # Remove an object
    container.remove_object(obj2)

    # Clear all objects
    container.clear_objects()

    # Check the container length
    logging.info(f"Final container length: {len(container)}")

    pygame.quit()