""" test of the Lidar class

Author: Henry Zhang
Date:August 28, 2019
"""

# module
import matplotlib.pyplot as plt

from src.simulator.car import Car, CarObject
from src.sensor.lidar import Lidar, LidarData

# parameters


# classes
class Test_Lidar():
  ego_pos = [0,0,0]
  lidar = Lidar([0,0,0], 10, 0)
  car_1 = Car([10,5,0], 0, 0, 0)
  car_2 = Car([10,0,0], 0, 0, 0)
  objs = [car_1.get_object(ego_pos), car_2.get_object(ego_pos)]

  def test_create_lidar(self):
    assert self.lidar.abs_pos == [0,0,0]
    assert self.lidar.rel_pos == [0,0,0]
    assert self.lidar.freq == 10
    assert self.lidar.orientation == 0
  
  def test_read(self):
    sensor_data = self.lidar.read(self.objs, 0)
    for data in sensor_data.data:
      print(data.scan)
  
  def test_find_visible_edges(self):
    for obj in self.objs:
      visible_edges = self.lidar.find_visible_edges(obj)
      print(visible_edges)
  
  def test_viz(self):
    plt.figure(figsize=(20,12))
    _ = self.lidar.read(self.objs, 0)
    self.lidar.viz()
    plt.pause(1)

# functions


# main
def main():
  pass

if __name__ == "__main__":
  main()