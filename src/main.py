""" Entry of the simulation and fusion

Author: Henry Zhang
Date:August 22, 2019
"""

# module
from matplotlib import pyplot as plt

import sys, os
sys.path.append(os.path.curdir)
#for path in sys.path:
#  print(path)

from src.simulator.road_simulator import RoadSimulator
from src.sensor.sensor_group import SensorGroup
from src.sensor.camera import Camera
from src.sensor.lidar import Lidar
from src.sensor.radar import Radar


# parameters


# classes


# functions


# main
def main():
  sim = RoadSimulator(gen_mode='constant', object_num=1, obj_mode='keeping')
  
  sensor_group = SensorGroup(sim)
  sensor_group.add(Camera((0,0,0), 10))
  sensor_group.add(Lidar((0,0,0), 10))
  sensor_group.add(Radar((0,0,0), 50))

  # fuser = Fusion()

  plt.figure(figsize=(20,12))

  # log = Logger()

  end_flag = False

  dt = sensor_group.get_min_interval()
  time_acc = 0

  while (not end_flag):
    sim.simulate(dt)

    # sensor_data = sensor_group.read()

    # estimation = fuser.fuse(sensor_data)
    
    time_acc += dt

    # log.write()
    plt.title('world {}, dt={}'.format(time_acc, dt))
    plt.pause(0.0001)
    plt.clf()

    if time_acc > 10:
      end_flag = True

if __name__ == "__main__":
  main()