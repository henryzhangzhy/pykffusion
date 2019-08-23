""" test for the Car class

Author: Henry Zhang
Date:August 22, 2019
"""

# module
from matplotlib import pyplot as plt

from src.simulator.car import Car

# parameters


# classes
class Test_Car():
  car = Car(v=5)
  
  def test_create_class(self):
    assert self.car.pos == [0,0,0]
    assert self.car.orientation == 0
    assert self.car.v == 5
    assert self.car.mode == 'constant acceleration'
    assert self.car.b_static == False

  def test_generate_outline(self):
    outline = self.car.get_outline()
    for line in outline:
      print(line)
  
  def test_viz(self):
    plt.figure(1, figsize=(20,12))
    self.car.viz()
    plt.show(1)


# functions
# main
def main():
  pass

if __name__ == "__main__":
  main()