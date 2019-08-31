""" the 2D box model class

Author: Henry Zhang
Date:August 23, 2019
"""

# module
from matplotlib import pyplot as plt

from src.util.utils import get_box_outline

# parameters


# classes
class Box2D():
  def __init__(self, x, y, orientation, omega, w, l, v=0, a=0):
    self.x = x
    self.y = y
    self.orientation = orientation
    self.omega = omega
    self.w = w
    self.l = l
    self.v = v
    self.a = a
  
  def viz(self):
    outline = get_box_outline(self.x, self.y, self.orientation, self.l, self.w)
    for line in outline:
      plt.plot(line[0], line[1], c='b')

# functions


# main
def main():
  pass

if __name__ == "__main__":
  main()