""" the 2D Lidar class

Author: Henry Zhang
Date:August 22, 2019
"""

# module
from src.sensor.sensor import Sensor

# parameters


# classes
class Lidar(Sensor):
  def __init__(self, rel_pos=(0,0,0), frequency=10, orientation=0, abs_pos=[0,0,0]):
    super(Lidar, self).__init__('Lidar', rel_pos, frequency, orientation, abs_pos)
  
  def read(self, objs, time_acc):
    pass


# functions


# main
def main():
  pass

if __name__ == "__main__":
  main()