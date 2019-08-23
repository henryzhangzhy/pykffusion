""" the Sensor Group class

Author: Henry Zhang
Date:August 22, 2019
"""

# module


# parameters


# classes
class SensorGroup():
  def __init__(self, simulator):
    self.sim = simulator
    self.sensor_group = []
    self.sensor_data = []
  
  def add(self, sensor):
    self.sensor_group.append(sensor)
  
  def read(self):
    self.sensor_data = [sensor.read() for sensor in self.sensor_group]
    return self.sensor_data
  
  def get_min_interval(self):
    freq_max = max([sensor.freq for sensor in self.sensor_group])
    dt = 1 / freq_max
    return dt

# functions


# main
def main():
  pass

if __name__ == "__main__":
  main()