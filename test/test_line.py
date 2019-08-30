""" the test for line class

Author: Henry Zhang
Date:August 29, 2019
"""

# module
import numpy as np
import matplotlib.pyplot as plt

from src.sensor.line import Line

# parameters


# classes
class Test_Line():
  points_1 = [(0.0, 0.0), (1.0, 1.0)]
  points_2 = [(0.0, 0.0), (0.0, 1.0)]
  points_3 = [(0.0, 0.0), (1.0, 0.0)]
  points_4 = [(0.0, 0.0), (0.0, 0.0)]
  points_5 = [(0.0, 0.0), (1.0, 1.0), (2.0, 2.0)]

  def test_find_line_two_points(self):
    line_1 = Line.find_line_two_point(self.points_1[0], self.points_1[1])
    print(line_1)
    line_2 = Line.find_line_two_point(self.points_2[0], self.points_2[1])
    print(line_2)
    line_3 = Line.find_line_two_point(self.points_3[0], self.points_3[1])
    print(line_3)
    line_4 = Line.find_line_two_point(self.points_4[0], self.points_4[1])
    print(line_4)
  
  def test_viz(self):
    plt.figure(figsize=(20,10))
    line_1 = Line.find_line_two_point(self.points_1[0], self.points_1[1])
    line_1.viz()
    line_2 = Line.find_line_two_point(self.points_2[0], self.points_2[1])
    line_2.viz()
    line_3 = Line.find_line_two_point(self.points_3[0], self.points_3[1])
    line_3.viz()
    line_4 = Line.find_line_two_point(self.points_4[0], self.points_4[1])
    line_4.viz()
    plt.pause(1)
  
  def test_find_line(self):
    plt.figure(figsize=(20,10))
    line_5, is_line_5 = Line.find_line(self.points_5)
    print(line_5)
    line_5.viz()
    plt.pause(3)
  
  def test_distance(self):
    line_1 = Line.find_line_two_point(self.points_1[0], self.points_1[1])
    assert line_1.distance((0.0, 0.0)) == 0
    assert abs(line_1.distance((0.0, 1.0)) - np.sqrt(2)/2) < 0.00001
# functions


# main
def main():
  pass

if __name__ == "__main__":
  main()