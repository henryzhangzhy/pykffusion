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
    plt.pause(1)
  
  def test_get_object(self):
    obj = self.car.get_object([1,1,0])
    assert obj.velocity == 5
    assert obj.close_point == (2, 1.75/2)


# functions
# main
def main():
  pass

if __name__ == "__main__":
  main()