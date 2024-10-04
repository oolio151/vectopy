import math

class Vector2:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        self.magnitude = Vector2.magnitude(x, y)


    #PREDEFINED VECTORS
    @staticmethod
    def down():
        return Vector2.Vector2(0, -1)
    
    @staticmethod
    def left():
        return Vector2.Vector2(-1, 0)
    
    @staticmethod
    def one():
        return Vector2.Vector2(1, 1)
    
    @staticmethod
    def right():
        return Vector2.Vector2(1, 0)
    
    @staticmethod
    def up():
        return Vector2.Vector2(0, 1)
    
    @staticmethod
    def zero():
        return Vector2.Vector2(0, 0)
    
    @staticmethod
    def positive_infinity():
        return Vector2.Vector2(float("inf"), float("inf"))
    
    @staticmethod
    def negative_infinity():
        return Vector2.Vector2(float("-inf"), float("-inf"))

    #CLASS FUNCTIONS
    def equals(vector, self):
        return vector.x == self.x and vector.y == self.y
    
    def do_normalize(self):
        self.x/=Vector2.find_magnitude(self)
        self.y/=Vector2.find_magnitude(self)
    
    def set_vals(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    #ACUTAL STATIC FUNCTIONS
    @staticmethod
    def normalize(vector):
        mag = Vector2.find_magnitude(vector.x, vector.y)
        return Vector2.Vector2(vector.x/mag, vector.y/mag)
    
    @staticmethod
    def find_magnitude(vector):
        return math.sqrt(vector.x**2 + vector.y**2)

    #u1v1+u2v2
    @staticmethod
    def dot_product(vector1, vector2):
        return vector1.x * vector2.x + vector1.y * vector2.y

    #returns in degrees
    @staticmethod
    def angle(vector1, vector2):
        return math.degrees(math.acos(Vector2.dot_product(vector1, vector2)/(vector1.magnitude * vector2.magnitude)))