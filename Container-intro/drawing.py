import pygame
from Container import Container
from Object import Object
from Circle import Circle
from Text import Text

def display_container(container: Container, window_size=(800, 600), background_color=(30, 30, 30)):
    """
    Displays all objects in the container, including nested containers, within a Pygame window.

    Args:
        container (Container): The container holding objects to display.
        window_size (tuple): The size of the Pygame window (width, height).
        background_color (tuple): The background color of the window (R, G, B).
    """
    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Container Display")
    clock = pygame.time.Clock()

    def render_objects(current_container: Container):
        """Recursively renders all objects, including nested containers."""
        for obj in current_container.get_objects():
            if isinstance(obj, (Circle, Text)):
                obj.draw(screen)
            elif isinstance(obj, Container):
                # Recursively render nested containers
                render_objects(obj)

    # Main loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        screen.fill(background_color)

        # Render all objects starting from the root container
        render_objects(container)

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

    # Create the first nested container
    nested_container1 = Container(position=pygame.Vector2(0, 0))
    nested_container1.add_object(circle3)
    nested_container1.add_object(text2)

    # Create objects for the second nested container
    circle4 = Circle(position=pygame.Vector2(500, 400), radius=30, color=pygame.Color("purple"))
    text3 = Text(position=pygame.Vector2(480, 380), text="Nested 2", color=pygame.Color("cyan"))

    # Create the second nested container
    nested_container2 = Container(position=pygame.Vector2(0, 0))
    nested_container2.add_object(circle4)
    nested_container2.add_object(text3)

    # Add a nested container inside another nested container
    nested_container1.add_object(nested_container2)

    # Create the root container
    root_container = Container(position=pygame.Vector2(0, 0))
    root_container.add_object(circle1)
    root_container.add_object(circle2)
    root_container.add_object(text1)
    root_container.add_object(nested_container1)

    # Display the container
    display_container(root_container)
