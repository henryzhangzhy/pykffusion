""" the LidarProc class that processes lidar data

Author: Henry Zhang
Date:August 29, 2019
"""

# module
import numpy as np
from matplotlib import pyplot as plt

from src.sensor.line import Line
from src.sensor.corner import Corner

# parameters


# classes
class LidarProc():
  def __init__(self, scan):
    self.scan = scan
  
  @ classmethod
  def find_models(cls, time, observation):
    ''' generate proposal from lidar data '''
    feature = cls.find_feature(observation.scan)
    models = cls.find_models_from_feature(feature)
    return models
  
  @ classmethod
  def find_feature(cls, scan):
    line_feature_1, is_line_1 = Line.find_line(scan)
    if is_line_1:
      _, points_far = line_feature_1.find_points_close_line(scan, line_feature_1.close_threshold)
      line_feature_2, is_line_2 = Line.find_line(points_far)
      if is_line_2:
        corner_feature = cls.find_corner_feature(line_feature_1, line_feature_2)
        if corner_feature is None:
          return line_feature_1
        else:
          return corner_feature
      else:
        return line_feature_1
    else:
      return None
  
  @ classmethod
  def find_corner_feature(cls, line_1, line_2):
    res = line_1.find_intersect(line_2)
    if res is None:
      return None
    else:
      return Corner(res, line_1, line_2)

  
  @ classmethod
  def find_models_from_feature(cls, feature):
    models = []
    return models

# functions


# main
def main():
  pass

if __name__ == "__main__":
  main()