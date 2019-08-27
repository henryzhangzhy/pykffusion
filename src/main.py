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
  
  fig_name_1 = "world"
  fig_name_2 = "logger"
  plt.figure(fig_name_1, figsize=(20,12))
  
  sim = RoadSimulator(gen_mode='constant', object_num=5, obj_mode='keeping', fig_name=fig_name_1)
  
  sensor_group = SensorGroup(sim, fig_name=fig_name_1)
  
  
  sensor_group.add(Radar((-15,0,0), 50))
  sensor_group.add(Radar((15,0,0), 50))
  # sensor_group.add(Camera((0,0,0), 10))
  # sensor_group.add(Lidar((0,0,0), 10))
  dt = sensor_group.get_min_interval()

  multi_sensor_filter = MultiSensorFusion(mode='sequential', fig_name=fig_name_1)
  
  log = Logger(fig_name=fig_name_2)

  time_acc = 0
  end_flag = False

  while (end_flag == False):
    objs, time_acc = sim.simulate(dt)

    sensor_data = sensor_group.read(objs, time_acc)

    estimation = multi_sensor_filter.estimate(sensor_data, time_acc)
    
    log.add_timed(time_acc,{'objs':objs, 'sensor_data':sensor_data, 'estimation':estimation})
    log.viz()
    
    end_flag = (time_acc > 5)
    display([fig_name_1, fig_name_2], end_flag)

  plt.show()

def display(fig_names, end_flag):
    for fig_name in fig_names:
        plt.figure(fig_name)
        plt.legend()
    plt.pause(0.0001)
    if end_flag:
      return
    else:
      for fig_name in fig_names:
        plt.figure(fig_name)
        plt.clf()

if __name__ == "__main__":
  main()