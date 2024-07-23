#Calculate Surface Volume and Area of a Cylinder
import math

def cylinder_volume(radius, height):
    return math.pi * radius**2 * height

def cylinder_surface_area(radius, height):
    return 2 * math.pi * radius * (radius + height)

# Example usage:
radius = 3
height = 5
print(f"Volume of the cylinder: {cylinder_volume(radius, height)}")  # Output: 141.3716694115407
print(f"Surface area of the cylinder: {cylinder_surface_area(radius, height)}")  # Output: 150.79644737231007