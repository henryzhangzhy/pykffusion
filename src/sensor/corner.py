""" the Corner class for lidar detection corner feature

Author: Henry Zhang
Date:August 30, 2019
"""

# module
import matplotlib.pyplot as plt

from src.sensor.line import Line

# parameters


# classes
class Corner():
  def __init__(self, intersect, line_1, line_2):
    self.intersect = intersect
    self.line_1 = line_1
    self.line_2 = line_2
    self.type = 'corner'
  
  def viz(self):
    self.line_1.viz()
    self.line_2.viz()
    plt.scatter(self.intersect[0], self.intersect[1], marker='X', label='corner')
  
  def __repr__(self):
    str1 = "Corner: Intersect: {}\n".format(self.intersect)
    str1 += "Line1: {}\n".format(self.line_1)
    str1 += "Line2: {}".format(self.line_2)
    return str1

# functions


# main
def main():
  pass

if __name__ == "__main__":
  main()