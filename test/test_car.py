""" test for the Car class

Author: Henry Zhang
Date:August 22, 2019
"""

# module
from matplotlib import pyplot as plt

from src.simulator.car import Car, CarObject

# parameters


# classes
class Test_Car():
  car_1 = Car(v=5)
  car_2 = Car([10,0,0], 0, 0, 0)
  
  def test_create_class(self):
    assert self.car_1.pos == [0,0,0]
    assert self.car_1.orientation == 0
    assert self.car_1.v == 5
    assert self.car_1.mode == 'constant acceleration'
    assert self.car_1.b_static == False

  def test_generate_outline(self):
    outline = self.car_1.get_outline()
    for line in outline:
      print(line)
  
  def test_viz(self):
    plt.figure(1, figsize=(20,12))
    self.car_1.viz()
    plt.pause(1)
  
  def test_get_object(self):
    obj_1 = self.car_1.get_object([1,1,0])
    assert obj_1.velocity == 5
    assert obj_1.close_point == (2, 1.75/2)

    obj_2 = self.car_2.get_object([0,0,0])
    print(obj_2.close_point)
    print(obj_2.other_points)
    plt.figure(figsize=(20,12))
    obj_2.viz()
    plt.pause(1)



# functions
# main
def main():
  pass

if __name__ == "__main__":
  main()