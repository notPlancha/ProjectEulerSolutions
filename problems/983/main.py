from typing import Generator
from sympy import Circle, Point, sqrt

def find_circles_of_mat_distance(d: int, center = Point(0,0)) -> Generator[Circle, tuple[int, int]]:
  first = 0
  last = d
  while first < last: # first + last = d
    yield Circle(center, sqrt(first**2 + last**2))
    first += 1
    last -= 1
    

print(Circle(Point(0,0), 1).intersection(Circle(Point(1,1), 1)))