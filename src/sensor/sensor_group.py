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
  
  def read(self, objs, time_acc):
    self.update_pos()
    self.sensor_data = [sensor.read(objs, time_acc) for sensor in self.sensor_group]
    self.viz()
    return self.sensor_data
  
  def get_min_interval(self):
    freq_max = max([sensor.freq for sensor in self.sensor_group])
    dt = 1 / freq_max
    return dt
  
  def update_pos(self):
    ego_pos = self.sim.ego_object.pos
    for sensor in self.sensor_group:
      sensor.abs_pos = [ego_pos[0] + sensor.rel_pos[0], \
                        ego_pos[1] + sensor.rel_pos[1], \
                        ego_pos[2] + sensor.rel_pos[2]]


  def viz(self):
    for sensor in self.sensor_group:
      sensor.viz()

# functions


# main
def main():
  pass

if __name__ == "__main__":
  main()