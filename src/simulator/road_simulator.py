""" Road Simulator class

Author: Henry Zhang
Date:August 22, 2019
"""

# module
from simulator.simulator import Simulator

# parameters


# classes
class RoadSimulator(Simulator):
  def __init__(self):
    self.objects = []
    self.boundary = None
  
  def simulate(self):
    self.clean_objects()
    self.generate_objects()
    
    for obj in self.objects:
      obj.simulate()
    
    self.update_boundary()
  
  def get_objects(self):
    pass
  
  def clean_objects(self):
    """ clean up the out of bound objects """
    pass
  
  def generate_objects(self):
    """ generate objects at the boundary """
    pass
  
  def update_boundary(self):
    """ update the boundaries """
    pass

# functions


# main
def main():
  pass

if __name__ == "__main__":
  main()