""" the Sensor Abstract type

Author: Henry Zhang
Date:August 22, 2019
"""

# module


# parameters


# classes
class Sensor():
  def __init__(self, sensor_type, position = (0,0,0), frequency = 10, orientation = 0):
    self.type = sensor_type
    self.pos = position
    self.freq = frequency
    self.orientation = orientation
    self.sensor_data = []
  
  def read(self, objs):
    pass

class SensorData():
  def __init__(self, sensor_type, time, data):
    self.type = sensor_type
    self.time = time
    self.data = data

# functions


# main
def main():
  pass

if __name__ == "__main__":
  main()