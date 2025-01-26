import pygame
from Container import Container
from Object import Object
from Circle import Circle
from Text import Text
from Rectangle import Rectangle
from Buzzer import Buzzer

import random

# Generate a random color
random_color = pygame.Color(
    random.randint(0, 255),  # Random Red component
    random.randint(0, 255),  # Random Green component
    random.randint(0, 255)   # Random Blue component
)

def display_container(container):
    """
    Displays all objects in the container, including nested containers, within a Pygame window.

    Args:
        container (Container): The container holding objects to display.
        window_size (tuple): The size of the Pygame window (width, height).
        background_color (tuple): The background color of the window (R, G, B).
    """
    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode(container.window_size, pygame.RESIZABLE)
    pygame.display.set_caption("Container Display")
    clock = pygame.time.Clock()

    # Main loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        screen.fill(container.background_color)

        #draw container
        container.draw(screen)

        # Update the display iterativ
        pygame.display.flip()
        clock.tick(60)  # Limit to 60 frames per second

    # Quit Pygame
    pygame.quit()

def display_container_dyn(container):
    """
    Displays all objects in the container, including nested containers, within a Pygame window.

    Args:
        container (Container): The container holding objects to display.
    """
    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode(container.window_size, pygame.RESIZABLE)
    pygame.display.set_caption("Container Display")
    clock = pygame.time.Clock()

    # Main loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            container.handle_key_press(event)

        # Clear the screen
        screen.fill(container.background_color)

        # Draw the container
        container.draw(screen)

        # Update the display
        pygame.display.flip()
        clock.tick(60)  # Limit to 60 frames per second

    # Quit Pygame
    pygame.quit()


if __name__ == "__main__":
    import pygame

    # Create objects for the root container
    circle1 = Circle(position=pygame.Vector2(150, 150), radius=50, color=pygame.Color("red"))
    circle2 = Circle(position=pygame.Vector2(200, 200), radius=60, color=pygame.Color("green"))
    text1 = Text(position=pygame.Vector2(180, 160), text="Overlap", color=pygame.Color("white"))

    # Create objects for the first nested container
    circle3 = Circle(position=pygame.Vector2(400, 300), radius=40, color=pygame.Color("blue"))
    text2 = Text(position=pygame.Vector2(380, 280), text="Nested 1", color=pygame.Color("yellow"), fontsize=50)
    buzzer = Buzzer((10,10))

    # Create the first nested container
    nested_container1 = Container(position=pygame.Vector2(0, 0))
    nested_container1.add_object(circle3)
    nested_container1.add_object(text2)
    nested_container1.add_object(buzzer)

    # Create objects for the second nested container
    circle4 = Circle(position=pygame.Vector2(500, 400), radius=30, color=pygame.Color("purple"))
    text3 = Text(position=pygame.Vector2(480, 380), text="Nested 2", color=pygame.Color("cyan"))
    rectangle1 = Rectangle(position=pygame.Vector2(200, 800))


    # Create the second nested container
    nested_container2 = Container(position=pygame.Vector2(0, 0))
    nested_container2.add_object(circle4)
    nested_container2.add_object(text3)
    nested_container2.add_object(rectangle1)

    # Add a nested container inside another nested container
    nested_container1.add_object(nested_container2)

    # Create the root container
    root_container = Container(position=pygame.Vector2(0, 0))
    root_container.add_object(circle1)
    root_container.add_object(circle2)
    root_container.add_object(text1)
    root_container.add_object(nested_container1)

    # Display the container
    display_container_dyn(root_container)
