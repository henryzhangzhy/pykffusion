""" the Camera class

Author: Henry Zhang
Date:August 22, 2019
"""

# module
from src.sensor.sensor import Sensor

# parameters


# classes
class Camera(Sensor):
  def __init__(self, rel_pos=(0,0,0), frequency=10, orientation=0, abs_pos=[0,0,0]):
    super(Camera, self).__init__('Camera', rel_pos, frequency, orientation, abs_pos)
  
  def read(self, objs, time_acc):
    pass


# functions


# main
def main():
  pass

if __name__ == "__main__":
  main()