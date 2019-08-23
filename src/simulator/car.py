""" the Car class

Author: Henry Zhang
Date:August 22, 2019
"""

# module
import random
import math
from matplotlib import pyplot as plt

# parameters


# classes
class Car():

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
  

  def get_outline(self):
    l_2 = self.l / 2
    w_2 = self.w / 2
    yaw_cos = math.cos(self.orientation)
    yaw_sin = math.sin(self.orientation)

    front_left_x = self.pos[0] + l_2 * yaw_cos - w_2 * yaw_sin
    front_left_y = self.pos[1] + l_2 * yaw_sin + w_2 * yaw_cos
    front_right_x = self.pos[0] + l_2 * yaw_cos + w_2 * yaw_sin
    front_right_y = self.pos[1] + l_2 * yaw_sin - w_2 * yaw_cos
    back_left_x = self.pos[0] - l_2 * yaw_cos - w_2 * yaw_sin
    back_left_y = self.pos[1] - l_2 * yaw_sin + w_2 * yaw_cos
    back_right_x = self.pos[0] - l_2 * yaw_cos + w_2 * yaw_sin
    back_right_y = self.pos[1] - l_2 * yaw_sin - w_2 * yaw_cos
    front_mid_x = self.pos[0] + l_2 / 2 * yaw_cos
    front_mid_y = self.pos[1] + l_2 / 2 * yaw_sin

    outline = []
    outline.append( ( (front_left_x, front_right_x), (front_left_y, front_right_y) ) )
    outline.append( ( (front_right_x, back_right_x), (front_right_y, back_right_y) ) )
    outline.append( ( (back_right_x, back_left_x), (back_right_y, back_left_y) ) )
    outline.append( ( (back_left_x, front_left_x), (back_left_y, front_left_y) ) )
    outline.append( ( (self.pos[0], front_mid_x), (self.pos[1], front_mid_y) ) )
    return outline
  

  def viz(self):
    outline = self.get_outline()
    for line in outline:
      plt.plot(line[0], line[1], c='b')



# functions


# main
def main():
  pass

if __name__ == "__main__":
  main()