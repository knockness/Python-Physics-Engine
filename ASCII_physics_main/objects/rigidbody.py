# Project Imports
import globals
import math2d
import math

# Rigidbody property classes
class Transform:
    def __init__(self, position: math2d.Vector2, rotation: float):
        self.position: math2d.Vector2 = position
        self.rotation: float = rotation

class Motion:
    def __init__(self, velocity: math2d.Vector2, acceleration: math2d.Vector2, drag: float):
        self.velocity: math2d.Vector2 = velocity
        self.acceleration: math2d.Vector2 = acceleration
        self.drag: float = drag

# Actual Rigidbody class
class Rigidbody:
    def __init__(self, gravity: math2d.Vector2, mass, linear: Motion, angular: Motion, transform: Transform, sprite):
        # instantiation arguments
        self.gravity: math2d.Vector2 = gravity
        self.mass: float = mass
        self.linear: Motion = linear
        self.angular: Motion = angular
        self.transform: Transform = transform
        self.sprite = sprite

        # Transform change variables (pre subpixel acumualtion)
        self.positionChange = math2d.Vector2.zero()
        self.rotationChange = 0

        # Subpixel Acumulation Variables
        self.positionPixelAcumulator = math2d.Vector2.zero()
        self.rotationPixelAcumulator = 0

            # Step variables (Integer component of transform change)
        self.positionStep = math2d.Vector2.zero()
        self.rotationStep = 0

            # Subpixel Variables (Float component of transform change)
        self.positionSubpixel = math2d.Vector2.zero()
        self.rotationSubpixel = 0
    # Executes one full Rigidbody time step (physics AND rendering)
    def tick(self):
        self.update()
        self.render()
    # Only updates the position as a single point in the scene based on the initial properties in __init__
    def update(self):
        # Velocity
        self.linear.velocity = self.linear.velocity + (self.gravity + self.linear.acceleration - self.linear.velocity * self.linear.drag) * globals.deltaTime
        self.angular.velocity = self.angular.velocity + (self.angular.acceleration - self.angular.velocity * self.angular.drag) * globals.deltaTime

        # Calculate transform change in floats (pre subpixel acumulation)
            # Position
        self.positionChange.x = self.linear.velocity.x * globals.deltaTime * globals.pixelsPerMeter
        self.positionChange.y = self.linear.velocity.y * globals.deltaTime * globals.pixelsPerMeter
            # Rotation
        self.rotationChange = self.angular.velocity * globals.deltaTime

        # Calculate subpixel acumulation
            # Position
        self.positionPixelAcumulator += self.positionChange

                # Separate subpixel and step
        positionSubpixelX, positionStepX = math.modf(self.positionPixelAcumulator.x)
        positionSubpixelY, positionStepY = math.modf(self.positionPixelAcumulator.y)

                # Store current Subpixel Change and total Acumulation
        self.positionSubpixel = math2d.Vector2(positionSubpixelX, positionSubpixelY)
        self.positionPixelAcumulator = math2d.Vector2(positionSubpixelX, positionSubpixelY)

        self.positionStep = math2d.Vector2(positionStepX / globals.pixelsPerMeter, positionStepY / globals.pixelsPerMeter)


            # Rotation
        self.rotationPixelAcumulator += self.rotationChange
        self.rotationSubpixel, self.rotationStep = math.modf(self.rotationPixelAcumulator)

        self.rotationPixelAcumulator = self.rotationSubpixel

        # transform update
            # position change application
        self.transform.position += self.positionStep
        if self.transform.position.x < 0: self.transform.position.x = 0
        if self.transform.position.y < 0: self.transform.position.y = 0
            # Angle Change
        self.transform.rotation += self.rotationStep
    # Only updates the render based on the properties modified in update
    def render(self):
        pass