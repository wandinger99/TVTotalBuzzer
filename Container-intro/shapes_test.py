import unittest
import pygame

from Object import Object
from Circle import Circle
from Text import Text
from Container import Container

class TestObject(unittest.TestCase):
    def test_object_initialization(self):
        obj = Object(pygame.Vector2(100, 200), visible=True)
        self.assertEqual(obj.position, pygame.Vector2(100, 200))
        self.assertTrue(obj.visible)

    def test_position_setter(self):
        obj = Object(pygame.Vector2(100, 200))
        obj.position = pygame.Vector2(300, 400)
        self.assertEqual(obj.position, pygame.Vector2(300, 400))

        with self.assertRaises(TypeError):
            obj.position = (300, 400)  # Invalid type

    def test_visibility_toggle(self):
        obj = Object(pygame.Vector2(100, 200))
        obj.toggle_visibility()
        self.assertFalse(obj.visible)
        obj.toggle_visibility()
        self.assertTrue(obj.visible)


class TestCircle(unittest.TestCase):
    def test_circle_initialization(self):
        circle = Circle(pygame.Vector2(50, 50), visible=True, radius=15, color=pygame.Color("red"))
        self.assertEqual(circle.position, pygame.Vector2(50, 50))
        self.assertEqual(circle.radius, 15)
        self.assertEqual(circle.color, pygame.Color("red"))

    def test_radius_setter(self):
        circle = Circle(pygame.Vector2(50, 50))
        circle.radius = 25
        self.assertEqual(circle.radius, 25)

        with self.assertRaises(ValueError):
            circle.radius = -5  # Negative radius is invalid

    def test_color_setter(self):
        circle = Circle(pygame.Vector2(50, 50))
        circle.color = pygame.Color("blue")
        self.assertEqual(circle.color, pygame.Color("blue"))

        with self.assertRaises(TypeError):
            circle.color = "blue"  # Invalid color type

    def test_change_size(self):
        circle = Circle(pygame.Vector2(50, 50), radius=10)
        circle.change_size(5)
        self.assertEqual(circle.radius, 15)

        circle.change_size(-20)  # Should not go below 0
        self.assertEqual(circle.radius, 0)


class TestText(unittest.TestCase):
    def test_text_initialization(self):
        text = Text(pygame.Vector2(10, 10), visible=True, text="Hello", color=pygame.Color("green"))
        self.assertEqual(text.position, pygame.Vector2(10, 10))
        self.assertEqual(text.text, "Hello")
        self.assertEqual(text.color, pygame.Color("green"))

    def test_text_setter(self):
        text = Text(pygame.Vector2(10, 10))
        text.text = "Updated Text"
        self.assertEqual(text.text, "Updated Text")

        with self.assertRaises(TypeError):
            text.text = 123  # Invalid text type

    def test_color_setter(self):
        text = Text(pygame.Vector2(10, 10))
        text.color = pygame.Color("yellow")
        self.assertEqual(text.color, pygame.Color("yellow"))

        with self.assertRaises(TypeError):
            text.color = "yellow"  # Invalid color type


class TestContainer(unittest.TestCase):
    def test_add_object(self):
        container = Container()
        obj = Object(pygame.Vector2(10, 20))
        container.add_object(obj)
        self.assertIn(obj, container.get_objects())
        self.assertEqual(len(container), 1)

    def test_remove_object(self):
        container = Container()
        obj1 = Object(pygame.Vector2(10, 20))
        obj2 = Object(pygame.Vector2(30, 40))
        container.add_object(obj1)
        container.add_object(obj2)

        container.remove_object(obj1)
        self.assertNotIn(obj1, container.get_objects())
        self.assertEqual(len(container), 1)

        with self.assertLogs(level="WARNING"):
            container.remove_object(obj1)  # Removing an already removed object logs a warning

    def test_clear_objects(self):
        container = Container()
        obj1 = Object(pygame.Vector2(10, 20))
        obj2 = Object(pygame.Vector2(30, 40))
        container.add_object(obj1)
        container.add_object(obj2)

        container.clear_objects()
        self.assertEqual(len(container), 0)
        self.assertEqual(container.get_objects(), [])

    def test_invalid_add_object(self):
        container = Container()
        with self.assertRaises(TypeError):
            container.add_object("Not an Object")  # Adding a non-Object raises an error


if __name__ == "__main__":
    unittest.main()
