""" the 2D Radar class

Author: Henry Zhang
Date:August 22, 2019
"""

# module
from src.sensor.sensor import Sensor

# parameters


# classes
class Radar(Sensor):
  def __init__(self, position = (0,0,0), frequency = 50, orientation = 0):
    super(Radar, self).__init__(position, frequency, orientation)
  
  def read(self, objs):
    pass


# functions


# main
def main():
  pass

if __name__ == "__main__":
  main()