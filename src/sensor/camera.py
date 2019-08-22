""" the Camera class

Author: Henry Zhang
Date:August 22, 2019
"""

# module
from src.sensor.sensor import Sensor

# parameters


# classes
class Camera(Sensor):
  def __init__(self, position = (0,0,0), frequency = 10, orientation = 0):
    self.pos = position
    self.freq = frequency
    self.orientation = orientation
  
  def read(self):
    pass


# functions


# main
def main():
  pass

if __name__ == "__main__":
  main()