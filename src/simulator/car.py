""" the Car class

Author: Henry Zhang
Date:August 22, 2019
"""

# module
import random
import math
from matplotlib import pyplot as plt

from src.util.utils import get_box_corners, get_box_outline

# parameters


# classes
class CarObject():
  def __init__(self, close_point, other_points, velocity, orientation, pos, obj_id):
    ''' Contains all the data that sensors need to generate observations '''
    self.close_point = close_point
    self.other_points = other_points
    self.velocity = velocity
    self.orientation = orientation
    self.pos = pos
    self.id = obj_id
  
  def viz(self):
    plt.scatter(self.close_point[0], self.close_point[1], c='r', marker='*', label='close point')
    for point in self.other_points:
      plt.scatter(point[0], point[1], c='g', marker='P', label='other points')


class Car():

  count = 0
  def __init__(self, position=[0,0,0], orientation=0, v = 0, a = 0, mode='constant acceleration'):
    self.pos = position
    self.orientation = orientation
    self.v = v
    self.a = a
    self.turn_rate = 0
    self.w = 1.75
    self.h = 1.65
    self.l = 4.0
    self.mode = mode
    self.b_static = False
    self.id = Car.count
    Car.count += 1
  

  def simulate(self, dt):
    if (self.mode == 'constant acceleration'):
      self.simulate_constant_acceleration(dt)
    elif (self.mode == 'random acceleration'):
      self.simulate_random_acceleration(dt)
    else:
      raise NotImplementedError
  

  def simulate_constant_acceleration(self, dt):
    if (self.v == 0 and self.a == 0):
      return
    elif (self.a == 0):
      average_speed = self.v + self.a * dt / 2
    else:
      average_speed = self.v
    
    vx, vy = self.get_partial(average_speed)

    self.pos[0] += vx * dt
    self.pos[1] += vy * dt
  

  def simulate_random_acceleration(self, dt):
    self.a += random.random - 1
    average_speed = self.v + self.a * dt / 2

    vx, vy = self.get_partial(average_speed)

    self.pos[0] += vx * dt
    self.pos[1] += vy * dt
  

  def get_partial(self, scaler):
    ''' Given a scaler, e.g. v, a, return its partial at x, and y direction '''
    scaler_x = scaler * math.cos(self.orientation)
    scaler_y = scaler * math.sin(self.orientation)
    
    return scaler_x, scaler_y

  def get_object(self, pos):
    corners = get_box_corners(self.pos[0], self.pos[1], self.orientation, self.l, self.w)
    corners = [corners[0], corners[1], corners[2], corners[3]]

    close_point = None
    close_distance = math.inf
    close_index = -1
    far_index = -1
    far_distance = (0, 0)
    for idx, point in enumerate(corners):
      distance = math.hypot(point[0] - pos[0], point[1] - pos[1])
      if (distance < close_distance):
        close_point = point
        close_index = idx
        close_distance = distance
    for idx, point in enumerate(corners):
      distance = (math.hypot(point[0] - pos[0], point[1] - pos[1]), \
                  math.hypot(close_point[0] - point[0], close_point[1] - point[1]))
      if (distance > far_distance):
        far_index = idx
        far_distance = distance
      # print(distance, point)
    
    other_points = [point for idx, point in enumerate(corners) if (idx != close_index and idx != far_index)]

    return CarObject(close_point, other_points, self.v, self.orientation, self.pos, self.id)


  def is_distance_safe(self, pos):
    ''' safety distance is set to be 1 m '''
    # assume that cars are of the same width and length
    safety_distance = 1
    if self.pos[0] - (self.l + safety_distance) > pos[0] or \
       self.pos[0] + (self.l + safety_distance) < pos[0] or \
       self.pos[1] - (self.w + safety_distance) > pos[1] or \
       self.pos[1] + (self.w + safety_distance) < pos[1]:
      return True
    else:
      return False
       
  

  def viz(self):
    outline = get_box_outline(self.pos[0], self.pos[1], self.orientation, self.l, self.w)
    for line in outline:
      plt.plot(line[0], line[1], c='b')
    plt.text(self.pos[0], \
             self.pos[1]+1, \
             'id:{:d}, v:{:.1f}, a:{:.1f}'.format(self.id, self.v, self.a))



# functions


# main
def main():
  pass

if __name__ == "__main__":
  main()