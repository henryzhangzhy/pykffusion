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
class Radar(Sensor):
  def __init__(self, position = (0,0,0), frequency = 50, orientation = 0, mode='center', b_noise=True):
    super(Radar, self).__init__('Radar', position, frequency, orientation)
    self.mode = mode
    self.b_noise = b_noise
    self.set_variances()
  
  def set_variances(self):
    if self.b_noise:
      self.variance_distance = 0.1
      self.variance_angle = 0.05
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
      point_ds = math.hypot( point[0] - self.pos[0], point[1] - self.pos[1])
      point_theta = math.atan2( point[1] - self.pos[1],  point[0] - self.pos[0])
      ds = point_ds + random.gauss(0, self.variance_distance)
      theta = point_theta + random.gauss(0, self.variance_angle)
      # print(ds, close_point_ds, theta, close_point_theta)
      
      x = self.pos[0] + ds * math.cos(theta)
      y = self.pos[1] + ds * math.sin(theta)
      vx = obj.velocity * math.cos(obj.orientation) + random.gauss(0, self.variance_velocity)
      vy = obj.velocity * math.sin(obj.orientation) + random.gauss(0, self.variance_velocity)
      
      sensor_data.append((x, y, vx, vy))
    
    self.sensor_data = SensorData(self.type, time_acc, sensor_data)

    return self.sensor_data
  
  def viz(self):
    x = [data[0] for data in self.sensor_data.data]
    y = [data[1] for data in self.sensor_data.data]
    plt.scatter(x, y, c='g', label='radar {}'.format(self.mode))




# functions


# main
def main():
  pass

if __name__ == "__main__":
  main()