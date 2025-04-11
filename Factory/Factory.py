from abc import ABC, abstractmethod
import math

# Definition of abstract class  
class Shape(ABC):

    @abstractmethod
    def compute_area(self) -> float:
        pass

class Circle(Shape):

    def __init__(self, radius: float):
        self.radius = radius

    # Redefinition of abstract method to ensure reusability
    def compute_area(self) -> float:
        return self.radius**2 * math.pi

class Rectangle(Shape):

    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def compute_area(self) -> float:
        return self.length * self.width

class Trapeze(Shape):

    def __init__(self, base1: float, base2: float, height: float):
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def compute_area(self) -> float:
        return (self.base1 + self.base2) * self.height / 2
    


class ShapeFactory:
    @staticmethod
    def create_shape(shape_type: str, **kwargs) ->Shape:

        if shape_type =='circle':
            return Circle(radius=kwargs.get("radius", 1.0))
        elif shape_type == 'rectangle':
            return Rectangle(length = kwargs.get("length", 1.0), width=kwargs.get("width", 1.0))
        
        elif shape_type=="trapeze": 
            return Trapeze(
                base1=kwargs.get("base1", 1.0),
                base2=kwargs.get("base2", 1.0),
                height=kwargs.get("height", 1.0)
            )
        else:
            raise ValueError(f'Unknown shape type: {shape_type}')



# Example usage
if __name__ == "__main__":
    factory = ShapeFactory()
    
    print(f"Area of circle: {factory.create_shape('circle', radius=10).compute_area()}")
    print(f"Area of rectangle: {factory.create_shape('rectangle', length=10, width = 5).compute_area()}")
    print(f"Area of Trapeze: {factory.create_shape('trapeze', base1 = 50, base2 = 17, height =85).compute_area()}")