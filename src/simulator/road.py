""" the Road class

Author: Henry Zhang
Date:August 22, 2019
"""

# module
from matplotlib import pyplot as plt
import math

# parameters


# classes
class Road():

  def __init__(self, start=(0,0,0), end=(10000,0,0), lane_num=1, lane_width=4):
    self.start = start
    self.end = end
    self.b_static = True
    self.lane_width = lane_width
    self.lane_num = lane_num
    self.b_bidirection = True
    self.lines = self.create_lines()
  

  def get_generating_point(self, boundary):
    if self.start[1] != self.end[1]:
      raise Exception('We assume that start and end is equal for this mock')
    pos_x = boundary[2]
    pos_y = self.start[1] + self.lane_width/2
    pos_z = 0
    orientation = math.pi * -1
    return [pos_x, pos_y, pos_z], orientation
  

  def create_lines(self):
    lines = []
    for lane_id in range(-self.lane_num, self.lane_num + 1, 1):
      lines.append(((self.start[0], self.end[0]), 
                   (self.start[1] + self.lane_width * lane_id, self.end[1] + self.lane_width * lane_id)))
    return lines


  def viz(self):
    for line in self.lines:
      plt.plot(line[0], line[1], c='k')

# functions


# main
def main():
  pass

if __name__ == "__main__":
  main()