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
  
  def read(self, objs):
    self.sensor_data = [sensor.read(objs) for sensor in self.sensor_group]
    self.viz()
    return self.sensor_data
  
  def get_min_interval(self):
    freq_max = max([sensor.freq for sensor in self.sensor_group])
    dt = 1 / freq_max
    return dt
  
  def viz(self):
    for sensor in self.sensor_group:
      sensor.viz()

# functions


# main
def main():
  pass

if __name__ == "__main__":
  main()