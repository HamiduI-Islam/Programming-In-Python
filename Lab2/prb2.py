#Problem 2
import math

#inputs for the first point (x1, y1)
print("Enter coordinates for Point 1:")
x1 = float(input("x1: "))
y1 = float(input("y1: "))

#inputs for the second point (x2, y2)
print("\nEnter coordinates for Point 2:")
x2 = float(input("x2: "))
y2 = float(input("y2: "))

# distance using the formula: d = √((x2-x1)² + (y2-y1)²)
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# 4. Print the output values
print(f"\nThe distance between two points is: {distance:}")
