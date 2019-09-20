""" test for the LidarProc class

Author: Henry Zhang
Date:August 30, 2019
"""

# module
import matplotlib.pyplot as plt

from src.simulator.car import Car, CarObject
from src.sensor.lidar import Lidar, LidarData
from src.sensor.lidar_proc import LidarProc

# parameters


# classes
class Test_LidarProc():
  ego_pos = [0,0,0]
  car = Car([10,5,0], 0, 0, 0)
  objs = [car.get_object(ego_pos)]
  lidar = Lidar((0,0,0), 10, 0, abs_pos=ego_pos)
  sensor_data = lidar.read(objs, 0)
  data = sensor_data.data[0]
  

  def test_find_feature(self):
    plt.figure(figsize=(20,12))
    feature = LidarProc.find_feature(self.data.scan)
    print(feature)
    # self.car.viz()
    feature.viz()
    self.lidar.viz()
    plt.gca().axis('equal')
    plt.pause(2)
    plt.close()
  
  def test_find_model_from_feature(self):
    plt.figure(figsize=(20,12))
    feature = LidarProc.find_feature(self.data.scan)
    feature.viz()
    models = LidarProc.find_models_from_feature(feature, self.data.sensor_pos)
    print(models)
    for model in models:
      model.viz()
    plt.pause(2)

# functions


# main
def main():
  pass

if __name__ == "__main__":
  main()