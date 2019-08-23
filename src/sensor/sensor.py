""" the Sensor Abstract type

Author: Henry Zhang
Date:August 22, 2019
"""

# module


# parameters


# classes
class Sensor():
  def __init__(self, position = (0,0,0), frequency = 10, orientation = 0):
    self.pos = position
    self.freq = frequency
    self.orientation = orientation
    self.sensor_data = []
  
  def read(self, objs):
    pass

# functions


# main
def main():
  pass

if __name__ == "__main__":
  main()