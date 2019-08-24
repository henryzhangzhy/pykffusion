""" test for Radar class

Author: Henry Zhang
Date:August 22, 2019
"""

# module
from matplotlib import pyplot as plt

from src.sensor.radar import Radar
from src.simulator.car import Car
# parameters


# classes
class Test_Radar():
  radar = Radar()

  def test_create_radar(self):
    assert self.radar.freq == 50
    assert self.radar.pos == (0,0,0)
    assert self.radar.orientation == 0

  def test_read(self):
    car = Car()
    objs = [car.get_object([-10, 1, 0])]
    sensor_data = self.radar.read(objs, 0)
    print('testing reading radar')
    print(sensor_data.data)
    car.viz()
    self.radar.viz()
    plt.pause(0.5)

    
# functions


# main
def main():
  pass

if __name__ == "__main__":
  main()