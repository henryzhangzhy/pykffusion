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
from src.simulator.logger import Logger

from src.sensor.sensor_group import SensorGroup
from src.sensor.camera import Camera
from src.sensor.lidar import Lidar
from src.sensor.radar import Radar

from src.fusion.fusion import MultiSensorFusion

# parameters


# classes


# functions


# main
def main():
  sim = RoadSimulator(gen_mode='constant', object_num=1, obj_mode='keeping')
  
  sensor_group = SensorGroup(sim)
  # sensor_group.add(Camera((0,0,0), 10))
  # sensor_group.add(Lidar((0,0,0), 10))
  sensor_group.add(Radar((0,0,0), 50))

  multi_sensor_filter = MultiSensorFusion(mode='sequential')

  plt.figure(figsize=(20,12))

  log = Logger()

  end_flag = False

  dt = sensor_group.get_min_interval()
  time_acc = 0

  while (not end_flag):
    objs = sim.simulate(dt)
    time_acc += dt

    sensor_data = sensor_group.read(objs, time_acc)

    estimation = multi_sensor_filter.estimate(sensor_data)
    
    log.add_timed(time_acc,{'objs':objs, 'sensor_data':sensor_data, 'estimation':estimation})
    
    plt.title('world {:.3f}, dt={:.3f}'.format(time_acc, dt))
    plt.legend()
    plt.pause(0.0001)
    plt.clf()

    if time_acc > 5:
      end_flag = True

if __name__ == "__main__":
  main()