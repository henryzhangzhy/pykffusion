""" Entry of the simulation and fusion

Author: Henry Zhang
Date:August 22, 2019
"""

# module

from src.simulator.simulator import Simulator
from src.sensor.sensor_group import SensorGroup
from src.sensor.camera import Camera


# parameters


# classes


# functions


# main
def main():
  sim = Simulator()
  sim.env_init()
  sim.ego_init()
  sim.obj_init()
  
  sensor_group = SensorGroup(sim)
  sensor_group.add(Camera((0,0,0), 10))
  sensor_group.add(Lidar((0,0,0), 10))
  sensor_group.add(Radar((0,0,0), 50))

  fuser = Fusion()

  viz = Visualization()

  log = Logger()

  end_flag = true

  while (not end_flag):
    sim.simulate(dt)

    sensor_data = sensor_group.read()

    estimation = fuser.fuse(sensor_data)
    
    log.write()
    
    viz.display()

if __name__ == "__main__":
  main()