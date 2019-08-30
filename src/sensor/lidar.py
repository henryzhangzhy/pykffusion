""" the 2D Lidar class

Author: Henry Zhang
Date:August 22, 2019
"""

# module
import math
import matplotlib.pyplot as plt

from src.sensor.sensor import Sensor, SensorData

# parameters


# classes
class LidarData():
  def __init__(self, obj_id, scan):
    ''' scan represents the points of an object '''
    self.id = obj_id
    self.scan = scan

class Lidar(Sensor):
  def __init__(self, rel_pos=(0,0,0), frequency=10, orientation=0, abs_pos=[0,0,0], angle_resolution=math.pi/180/4):
    super(Lidar, self).__init__('Lidar', rel_pos, frequency, orientation, abs_pos)
    self.angle_res = angle_resolution
    self.variance_distance = 0.01
    self.variance_angle = 0.0025
  
  def read(self, objs, time_acc):
    ''' generate lidar scan from obj '''
    sensor_data = []

    for obj in objs:
      visible_edges = self.find_visible_edges(obj)
      scan = self.find_scan(visible_edges)
      sensor_data.append(LidarData(obj.id, scan))
    
    self.data = SensorData('Lidar', time_acc, sensor_data)
    return self.data
  
  def find_visible_edges(self, obj):
    visible_edges = []
    for point_i in obj.other_points:
      edge_i = self.create_edge(self.abs_pos, point_i)
      is_free = True
      for point_j in obj.other_points:
        if not point_j is point_i:
          edge_j = self.create_edge(obj.close_point, point_j)
          if self.is_intersect(edge_i, edge_j):
            is_free = False
      if is_free:
        visible_edges.append((obj.close_point, point_i))

    return visible_edges
  
  def is_intersect(self, edge_1, edge_2):
    e1p1 = edge_1[0]
    e1p2 = edge_1[1]
    e2p1 = edge_2[0]
    e2p2 = edge_2[1]
    # y - e1p1[1] = (e1p2[1] - e1p1[1]) / (e1p2[0] - e1p1[0]) * (x - e1p1[0])
    # y - e2p1[1] = (e2p2[1] - e2p1[1]) / (e2p2[0] - e2p1[0]) * (x - e2p1[0])
    # (e1p2[1] - e1p1[1]) / (e1p2[0] - e1p1[0]) * (x - e1p1[0]) + e1p1[1] - e2p1[1] = (e2p2[1] - e2p1[1]) / (e2p2[0] - e2p1[0]) * (x - e2p1[0])
    if (e1p2[0] - e1p1[0] == 0) :
      x = e1p1[0]
      if self.is_x_between(x, edge_2):
        ratio = (x - e2p1[0]) / (e2p2[0] - e2p1[0])
        y = ratio * (e2p2[1] - e2p1[1]) + e2p1[1]
        return self.is_y_between(y, edge_1)
      else:
        return False
    elif (e2p2[0] - e2p1[0] == 0) :
      x = e2p1[0]
      if self.is_x_between(x, edge_1):
        ratio = (x - e1p1[0]) / (e1p2[0] - e1p1[0])
        y = ratio * (e1p2[1] - e1p1[1]) + e1p1[1]
        return self.is_y_between(y, edge_2)
      else:
        return False
    else:
      k1 = (e1p2[1] - e1p1[1]) / (e1p2[0] - e1p1[0])
      k2 = (e2p2[1] - e2p1[1]) / (e2p2[0] - e2p1[0])
      
      if k1 == k2:
        return False
      else:
        x = (k1 * e1p1[0] - k2 * e2p1[0] - e1p1[1] + e2p1[1]) / (k1 - k2)
        if self.is_x_between(x, edge_1) and self.is_x_between(x, edge_2):
          return True
        else:
          return False
  
  def is_x_between(self, x, edge):
    if (edge[0][0] <= x <= edge[1][0]) or (edge[1][0] <= x <= edge[0][0]):
      return True
    else:
      return False
  
  def is_y_between(self, y, edge):
    if (edge[0][1] <= y <= edge[1][1]) or (edge[1][1] <= y <= edge[0][1]):
      return True
    else:
      return False

  def create_edge(self, point_1, point_2):
    p1 = self.get_2d_point(point_1)
    p2 = self.get_2d_point(point_2)
    return (p1, p2)

  def get_2d_point(self, point):
    if (len(point) == 3 and point[2] == 0) or len(point) == 2:
      point_2d = (point[0], point[1])
    else:
      raise Exception("Point dimension must be 2 or 3")
    
    return point_2d
  
  def find_scan(self, visible_edges):
    scan_data = []
    
    for edge in visible_edges:
      scan = self.find_edge_scan(edge)
      for point in scan:
        scan_data.append(point)

    return scan_data
  
  def find_edge_scan(self, edge):
    angle_1 = math.atan2(edge[0][1] - self.abs_pos[1], edge[0][0] - self.abs_pos[0])
    angle_2 = math.atan2(edge[1][1] - self.abs_pos[1], edge[1][0] - self.abs_pos[0])
    point_num = math.ceil(abs(angle_1 - angle_2) / self.angle_res)
    seg_num = max(1, (point_num - 1))
    
    points = []
    for i in range(point_num):
      x = i / seg_num * edge[0][0] + (seg_num - i) / seg_num * edge[1][0]
      y = i / seg_num * edge[0][1] + (seg_num - i) / seg_num * edge[1][1]
      points.append((x, y))
    
    return points
  
  def viz(self):
    x = []
    y = []
    for data in self.data.data:
      for point in data.scan:
        x.append(point[0])
        y.append(point[1])
    plt.scatter(x, y, marker='.', label='Lidar')


# functions


# main
def main():
  pass

if __name__ == "__main__":
  main()