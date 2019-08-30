""" the Line class

Author: Henry Zhang
Date:August 29, 2019
"""

# module
import numpy as np
import math
from matplotlib import pyplot as plt

# parameters


# classes
class Line():
  method = 'RANSAC'
  close_threshold = 0.1
  def __init__(self, a, b, c, points, vertices):
    ''' ax + by + c = 0, y = - a/b x - c/b '''
    self.a = a
    self.b = b
    self.c = c
    self.points = points
    self.vertices = vertices
    self.type = 'line'
  
  @ classmethod
  def find_line(cls, points):
    if len(points) < 3:
      return None, False
    else:
      if cls.method == 'RANSAC':
        return cls.find_line_ransac(points)
      elif cls.method == 'weighted_least_square':
        raise NotImplementedError
      else:
        raise NotImplementedError
  
  @ classmethod
  def find_line_ransac(cls, points):
    rand_pair = np.random.randint(0, len(points), [50,2])
    line_points_num_max = 0
    line_max_support = None
    for idx_pair in rand_pair:
      if idx_pair[0] == idx_pair[1]:
        continue
      else:
        line = cls.find_line_two_point(points[idx_pair[0]], points[idx_pair[1]])
        line_points, _ = line.find_points_close_line(points, cls.close_threshold)
        line_points_num = len(line_points)
        if line_points_num > line_points_num_max:
          line_points_num_max = line_points_num
          line_max_support = line
        # print(line)
        # print(line_points_num, points[idx_pair[0]], points[idx_pair[1]], idx_pair[0], idx_pair[1])
    line_max_support.update_vertices()
    return line_max_support, line_points_num_max >= len(points) / 2
  
  @ classmethod
  def find_line_two_point(cls, pt1, pt2):
    if (pt1 == pt2):
      return Line(a=0, b=0, c=0, points=[pt1, pt2], vertices=[])
    else:
      dx = pt2[0] - pt1[0] 
      dy = pt2[1] - pt1[1]
      if dx == 0:
        return Line(a=1, b=0, c=-pt1[0], points=[pt1, pt2], vertices=[pt1, pt2])
      elif dy == 0:
        return Line(a=0, b=1, c=-pt1[1], points=[pt1, pt2], vertices=[pt1, pt2])
      else:
        c = dy * pt1[0] - dx * pt1[1]
        return Line(a=-dy, b=dx, c=c, points=[pt1, pt2], vertices=[pt1, pt2])
  
  def find_points_close_line(self, points, threshold):
    points_close, points_far = [], []
    for point in points:
      if self.is_close(point, threshold):
        points_close.append(point)
      else:
        points_far.append(point)
    self.points = points_close
    return points_close, points_far
    
  def is_close(self, point, threshold):
    distance = self.distance(point)
    # print(distance, threshold, point)
    if distance < threshold:
      return True
    else:
      return False
  
  def distance(self, point):
    return abs(self.a * point[0] + self.b * point[1] + self.c) / math.hypot(self.a, self.b)
  
  def find_intersect(self, other):
    ''' find the intersection point of line self and line other, None if not '''
    if (self.a * other.b == self.b * other.a != 0) or \
       (self.a == other.a == 0 or self.b == other.b == 0) or \
       (self.a == self.b == 0 or other.a == other.b == 0):
      # three type of non intersect 1. parallel non zero a,b, 2. parallel zero a or b, 3 not a line.
      return None
    else:
      if self.a == 0 and other.b == 0:
        return (-other.c/other.a, -self.c/self.b)
      elif self.b == 0 and other.a == 0:
        return (-self.c/self.a, -other.c/other.b)
      else:
        dinominator = (self.a * other.b - other.a * self.b)
        x = (self.b * other.c - other.b * self.c) / dinominator
        y = (self.a * other.c - other.a * self.c) / -dinominator
        return (x, y)
  
  def update_vertices(self):
    if abs(self.a) >= abs(self.b):
      i, j = 1, 0
    else:
      i, j = 0, 1
    min_i = np.Inf
    max_i = -np.Inf
    for point in self.points:
      if point[i] > max_i:
        max_point = point
        max_i = point[i]
      elif point[i] < min_i:
        min_point = point
        min_i = point[i]
    if max_i <= min_i:
      return
    else:
      self.vertices = [min_point, max_point]
      return

  def __repr__(self):
    str1 = "%.2f, %.2f, %.2f" % (self.a, self.b, self.c)
    str1 += ' vertices:'
    for point in self.vertices:
      str1 += " (%.2f, %.2f)" % (point[0], point[1])
    return str1

  def viz(self):
    if len(self.vertices) == 0:
      return
    else:
      plt.plot([self.vertices[0][0], self.vertices[1][0]], \
               [self.vertices[0][1], self.vertices[1][1]], c='g')



# functions


# main
def main():
  pass

if __name__ == "__main__":
  main()