# Project Imports
import globals
import math2d

# Rigidbody property classes
class Transform:
    def __init__(self, position: math2d.Vector2, rotation):
        self.position = position
        self.rotation = rotation
class LinearMotion:
    def __init__(self, linearVelocity: math2d.Vector2, linearAcceleration: math2d.Vector2, LinearDrag: math2d.Vector2):
        self.linearVelocity = linearVelocity
        self.linearAcceleration = linearAcceleration
        self.LinearDrag = LinearDrag

class AngularMotion:
    def __init__(self, angularVelocity, angularAcceleration, angularDrag):
        self.angularVelocity = angularVelocity
        self.angularAcceleration = angularAcceleration
        self.angularDrag = angularDrag

# Actual Rigidbody class
class Rigidbody:
    def __init__(self, gravity, mass, linearMotion: LinearMotion, angularMotion: AngularMotion, transform: Transform, sprite):
        self.gravity = gravity
        self.mass = mass
        self.linearMotion = linearMotion
        self.angularMotion = angularMotion
        self.transform = transform
        self.sprite = sprite
    # Executes one full Rigidbody time step (physics AND rendering)
    def tick(self):
        self.update()
        self.render()
    # Only updates the position as a single point in the scene based on the initial properties in __init__
    def update(self):
        pass
    # Only updates the render based on the properties modified in update
    def render(self):
        pass