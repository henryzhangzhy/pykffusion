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
  points_6 = [(8.0, 1.0), (8.0, 3.0)]
  point_other_1 = (8.0, 2.0)

  def test_find_line_two_points(self):
    line_1 = Line.find_line_two_point(self.points_1[0], self.points_1[1])
    print(line_1)
    line_2 = Line.find_line_two_point(self.points_2[0], self.points_2[1])
    print(line_2)
    line_3 = Line.find_line_two_point(self.points_3[0], self.points_3[1])
    print(line_3)
    line_4 = Line.find_line_two_point(self.points_4[0], self.points_4[1])
    print(line_4)
    line_6 = Line.find_line_two_point(self.points_6[0], self.points_6[1])
    assert line_6.a == 1
    assert line_6.b == 0
    assert line_6.c == -self.points_6[0][0]
  
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
    line_5, is_line_5, line_error_5 = Line.find_line(self.points_5)
    print(line_5)
    line_5.viz()
    plt.pause(3)
  
  def test_distance(self):
    line_1 = Line.find_line_two_point(self.points_1[0], self.points_1[1])
    line_6 = Line.find_line_two_point(self.points_6[0], self.points_6[1])
    assert line_1.distance((0.0, 0.0)) == 0
    assert abs(line_1.distance((0.0, 1.0)) - np.sqrt(2)/2) < 0.00001
    assert line_6.distance(self.point_other_1) == 0

  def test_find_intersect(self):
    line_1 = Line.find_line_two_point(self.points_1[0], self.points_1[1])
    line_2 = Line.find_line_two_point(self.points_2[0], self.points_2[1])
    line_3 = Line.find_line_two_point(self.points_3[0], self.points_3[1])
    line_4 = Line.find_line_two_point(self.points_4[0], self.points_4[1])
    assert line_1.find_intersect(line_2) == (0,0)
    assert line_2.find_intersect(line_3) == (0,0)
    assert line_3.find_intersect(line_4) == None
    assert line_4.find_intersect(line_1) == None
    assert line_1.find_intersect(line_3) == (0,0)
    assert line_1.find_intersect(line_4) == None
    assert line_2.find_intersect(line_4) == None

class Test_Line_Integration():
  from src.simulator.car import Car
  from src.sensor.lidar import Lidar, LidarData

  ego_pos = [0,0,0]
  car = Car([10,5,0], 0, 0, 0)
  objs = [car.get_object(ego_pos)]
  lidar = Lidar((0,0,0), 10, 0, abs_pos=ego_pos)
  sensor_data = lidar.read(objs, 0)
  scan = sensor_data.data[0].scan

  def test_find_line(self):
    plt.figure(1,figsize=(20,12))
    print(self.scan)
    line_feature_1, is_line_1, line_error_1 = Line.find_line(self.scan)
    print(line_feature_1)
    print(is_line_1)
    self.lidar.viz()
    line_feature_1.viz()
    _, points_far = line_feature_1.find_points_close_line(self.scan, line_feature_1.close_threshold)
    plt.figure(2)
    self.lidar.viz()
    plt.scatter([point[0] for point in points_far], [point[1] for point in points_far], marker='o', c='r', label='far')
    plt.legend()
    plt.show()
    line_feature_2, is_line_2, line_error_2 = Line.find_line(points_far)
    
    line_feature_2.viz()
    
# functions


# main
def main():
  pass

if __name__ == "__main__":
  main()