""" the 2D Radar class

Author: Henry Zhang
Date:August 22, 2019
"""

# module
import random
import math
import matplotlib.pyplot as plt

from src.sensor.sensor import Sensor, SensorData

# parameters


# classes
class RadarData():
  def __init__(self, x, y, vx, vy, obj_id):
    self.x = x
    self.y = y
    self.vx = vx
    self.vy = vy
    self.id = obj_id

class Radar(Sensor):
  def __init__(self, rel_pos=(0,0,0), frequency=50, orientation=0, mode='center', b_noise=True, abs_pos=[0,0,0]):
    super(Radar, self).__init__('Radar', rel_pos, frequency, orientation, abs_pos)
    self.mode = mode
    self.b_noise = b_noise
    self.set_variances()
  
  def set_variances(self):
    if self.b_noise:
      self.variance_distance = 0.1
      self.variance_angle = 0.02
      self.variance_velocity = 0.5
    else:
      self.variance_distance = 0
      self.variance_angle = 0
      self.variance_velocity = 0
  
  def read(self, objs, time_acc):
    sensor_data = []
    
    for obj in objs:
      if (self.mode == 'close'):
        point = obj.close_point
      elif (self.mode == 'center'):
        point = obj.pos
      point_ds = math.hypot( point[0] - self.abs_pos[0], point[1] - self.abs_pos[1])
      point_theta = math.atan2( point[1] - self.abs_pos[1],  point[0] - self.abs_pos[0])
      ds = point_ds + random.gauss(0, self.variance_distance)
      theta = point_theta + random.gauss(0, self.variance_angle)
      # print(ds, point_ds, theta, point_theta)
      # print(ds - point_ds, theta - point_theta)
      
      x = self.abs_pos[0] + ds * math.cos(theta)
      y = self.abs_pos[1] + ds * math.sin(theta)
      vx = obj.velocity * math.cos(obj.orientation) + random.gauss(0, self.variance_velocity)
      vy = obj.velocity * math.sin(obj.orientation) + random.gauss(0, self.variance_velocity)
      
      sensor_data.append(RadarData(x, y, vx, vy, obj.id))
    
    self.sensor_data = SensorData(self.type, time_acc, sensor_data)

    return self.sensor_data
  
  def viz(self):
    x = [data.x for data in self.sensor_data.data]
    y = [data.y for data in self.sensor_data.data]
    plt.scatter(x, y, c='g', label='radar {}'.format(self.mode))




# functions


# main
def main():
  pass

if __name__ == "__main__":
  main()