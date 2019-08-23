""" the 2D Radar class

Author: Henry Zhang
Date:August 22, 2019
"""

# module
import random
import math
import matplotlib.pyplot as plt

from src.sensor.sensor import Sensor

# parameters


# classes
class Radar(Sensor):
  def __init__(self, position = (0,0,0), frequency = 50, orientation = 0):
    super(Radar, self).__init__(position, frequency, orientation)
    self.variance_distance = 0.1
    self.variance_angle = 0.05
    self.variance_velocity = 0.5
  
  def read(self, objs):
    sensor_data = []
    
    for obj in objs:
      
      close_point_ds = math.hypot( obj.close_point[0] - self.pos[0], obj.close_point[1] - self.pos[1])
      close_point_theta = math.atan2( obj.close_point[1] - self.pos[1],  obj.close_point[0] - self.pos[0])
      ds = close_point_ds + random.gauss(0, self.variance_distance)
      theta = close_point_theta + random.gauss(0, self.variance_angle)
      # print(ds, close_point_ds, theta, close_point_theta)
      
      x = self.pos[0] + ds * math.cos(theta)
      y = self.pos[1] + ds * math.sin(theta)
      vx = obj.velocity * math.cos(obj.orientation) + random.gauss(0, self.variance_velocity)
      vy = obj.velocity * math.sin(obj.orientation) + random.gauss(0, self.variance_velocity)
      
      sensor_data.append((x, y, vx, vy))
    
    self.sensor_data = sensor_data

    return sensor_data
  
  def viz(self):
    x = [data[0] for data in self.sensor_data]
    y = [data[1] for data in self.sensor_data]
    plt.scatter(x, y, c='g', label='radar')




# functions


# main
def main():
  pass

if __name__ == "__main__":
  main()