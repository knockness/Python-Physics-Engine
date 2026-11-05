# Project Imports
import globals
import math2d

# Base Vector2 Class
class Vector2:
    x: float
    y: float

    def __init__(self, x, y):
        self.x = x  
        self.y = y
    # Vector math
    def __add__(self, other: "Vector2") -> "Vector2":
        return Vector2(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: "Vector2") -> "Vector2":
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float) -> "Vector2":
        return Vector2(self.x * scalar, self.y * scalar)
    __rmul__ = __mul__
    
    @classmethod
    def zero(cls) -> "Vector2":
        return cls(0, 0)