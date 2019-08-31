""" the LidarProc class that processes lidar data

Author: Henry Zhang
Date:August 29, 2019
"""

# module
import numpy as np
import math
from matplotlib import pyplot as plt

from src.sensor.line import Line
from src.sensor.corner import Corner
from src.fusion.box import Box2D

# parameters


# classes
class LidarProc():
  def __init__(self, scan):
    self.scan = scan
  
  @ classmethod
  def find_models(cls, time, observation):
    ''' generate proposal from lidar data '''
    feature = cls.find_feature(observation.scan)
    models = cls.find_models_from_feature(feature, observation.sensor_pos)
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
  def find_models_from_feature(cls, feature, sensor_pos):
    if feature == None:
      return None
    elif feature.type == 'line':
      return cls.find_models_from_line(feature, sensor_pos)
    elif feature.type == 'corner':
      return cls.find_models_from_corner(feature)
    else:
      raise NotImplementedError

  @ classmethod
  def find_models_from_line(cls, line, sensor_pos):
    direction_1 = line.find_perpendicular_vector()
    if direction_1 != None and len(line.vertices) > 0:
      vector = (sensor_pos[0] - line.vertices[0][0], \
                sensor_pos[1] - line.vertices[0][1])
      if vector[0] * direction_1[0] + vector[1] * direction_1[1] < 0:
        pass
      else:
        direction_1 = (-direction_1[0], -direction_1[1])
      direction_2_base_0 = (line.vertices[1][0] - line.vertices[0][0], \
                            line.vertices[1][1] - line.vertices[0][1])
      direction_2_base_1 = (line.vertices[0][0] - line.vertices[1][0], \
                            line.vertices[0][1] - line.vertices[1][1])
      model_base_0_0 = cls.find_models_from_vectors(line.vertices[0], direction_1, direction_2_base_0)
      model_base_0_1 = cls.find_models_from_vectors(line.vertices[0], direction_2_base_0, direction_1)
      model_base_1_0 = cls.find_models_from_vectors(line.vertices[1], direction_1, direction_2_base_1)
      model_base_1_1 = cls.find_models_from_vectors(line.vertices[1], direction_2_base_1, direction_1)
      models = model_base_0_0 + model_base_0_1 + model_base_1_0 + model_base_1_1
      return models
    else:
      return None  

  
  @ classmethod
  def find_models_from_corner(cls, corner):
    if distance(corner.line_1.vertices[0], corner.intersect) > \
       distance(corner.line_1.vertices[1], corner.intersect):
      direction_1 = direction(corner.intersect, corner.line_1.vertices[0])
    else:
      direction_1 = direction(corner.intersect, corner.line_1.vertices[1])
    
    if distance(corner.line_2.vertices[0], corner.intersect) > \
       distance(corner.line_2.vertices[1], corner.intersect):
      direction_2 = direction(corner.intersect, corner.line_2.vertices[0])
    else:
      direction_2 = direction(corner.intersect, corner.line_2.vertices[1])
      
    models_1 = cls.find_models_from_vectors(corner.intersect, direction_1, direction_2)
    models_2 = cls.find_models_from_vectors(corner.intersect, direction_2, direction_1)
    
    return models_1 + models_2

  @ classmethod
  def find_models_from_vectors(cls, intersect, vector_1, vector_2):
    ''' return 2D box models from given intersect point and directions '''
    l, w = 4.0, 1.75
    l_2, w_2 = l / 2, w / 2
    angle_1 = math.atan2(vector_1[1], vector_1[0])
    angle_2 = math.atan2(vector_2[1], vector_2[0])
    angle_cos_1, angle_sin_1 = math.cos(angle_1), math.sin(angle_1)
    angle_cos_2, angle_sin_2 = math.cos(angle_2), math.sin(angle_2)
    
    x = intersect[0] + l_2 * angle_cos_1 + w_2 * angle_cos_2
    y = intersect[1] + l_2 * angle_sin_1 + w_2 * angle_sin_2
    orientation = angle_1
    omega = 0
    v = 0
    a = 0
    box_1 = Box2D(x, y, orientation, omega, w, l, v, a)
    box_2 = Box2D(x, y, orientation + math.pi, omega, w, l, v, a)
    return [box_1, box_2]
# functions

def distance(point_1, point_2):
  return math.hypot(point_1[0] - point_2[0], point_1[1] - point_1[1])

def direction(point_base, point_target):
  return (point_target[0] - point_base[0], point_target[1] - point_base[1])

# main
def main():
  pass

if __name__ == "__main__":
  main()