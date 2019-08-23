""" tests of the Road class

Author: Henry Zhang
Date:August 22, 2019
"""

# module
import matplotlib.pyplot as plt

from src.simulator.road import Road
# parameters


# classes


# functions
class Test_Road():
  road = Road(start=(0,0,0), end=(10,0,0), lane_num=1, lane_width=4)

  def test_create_road(self):
    assert self.road.start == (0,0,0)
    assert self.road.end == (10,0,0)
    assert self.road.lane_num == 1
    assert self.road.lane_width == 4
  
  def test_create_lines(self):
    lines = self.road.create_lines()
    for line in lines:
      print(line)
  
  def test_viz(self):
    plt.figure(figsize=(20,12))
    self.road.viz()
    plt.show(1)

# main
def main():
  pass

if __name__ == "__main__":
  main()