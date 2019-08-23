""" Road Simulator class

Author: Henry Zhang
Date:August 22, 2019
"""

# module
import random
import matplotlib.pyplot as plt

from src.simulator.simulator import Simulator
from src.simulator.car import Car
from src.simulator.road import Road

# parameters


# classes
class RoadSimulator(Simulator):

  def __init__(self, gen_mode = 'constant', object_num = 1, probability = 0.1, obj_mode='static'):
    ''' Road Simulator class
    
    Args:
      mode='constant': defines the mode of generating objects, 
                      'constant' keeps the number of object specified by object_num,
                      'random' keeps the probability of generating object
      object_num=1: defines the number of objects expected
      probability=0.1: defines the probability of generating objects
      obj_mode='static': defines the motion type of the generated objects.
                         'static' for not moving
                         'keeping' for random speed but keep it.
                         'accelerate' for random acceleration from zero velocity.
    '''
    self.gen_mode = gen_mode
    self.object_num = object_num
    self.gen_prob = probability
    self.obj_mode = obj_mode
    self.objects = []
    self.boundary_offset = (-20, -10, 20, 10)
    self.boundary = [-20, -10, 20, 10]
    self.ego_object = Car(position=[0,-2,0], orientation=0, v=5, a=0, mode='constant')
    self.road = Road(start=(0,0,0), end=(100,0,0), lane_num=1, lane_width=4)
  

  def simulate(self, dt):
    self.clean_objects()
    
    self.generate_objects()
    
    for obj in self.objects:
      if not obj.b_static:
        obj.simulate(dt)
    
    self.update_boundary()
    
    self.viz()
  
  def get_objects(self):
    pass
  

  def clean_objects(self):
    """ clean up the out of bound objects """
    new_objects = []

    for obj in self.objects:
      if self.is_pos_in_boundary(obj.pos):
        new_objects.append(obj)

    self.objects = new_objects
  

  def generate_objects(self):
    """ generate objects at the boundary """
    if self.gen_mode == 'constant':
      self.generate_objects_constant()
    elif self.gen_mode == 'random':
      self.generate_objects_random()
  

  def generate_objects_constant(self):
    if len(self.objects) < self.object_num:
      self.generate_an_object()
  

  def generate_objects_random(self):
    if random.random() < self.gen_prob:
      self.generate_an_object()
  

  def generate_an_object(self):
    pos, orientation = self.get_generating_point()
    mode = 'constant acceleration'
    
    if self.obj_mode == 'static':
      v = 0
      a = 0
    elif self.obj_mode == 'keeping':
      v = random.randint(0,10)
      a = 0
    elif self.obj_mode == 'accelerating':
      v = 0
      a = random.randint(0,10)
    else:
      raise NotImplementedError

    self.objects.append(Car(pos, orientation, v, a, mode))
  

  def get_generating_point(self):
    ''' return the position and orientation an object an be generated.'''
    return self.road.get_generating_point(self.boundary)


  def update_boundary(self):
    ''' get the new boundary around the ego_vehicle '''
    self.boundary[0] = self.ego_object.pos[0] + self.boundary_offset[0]
    self.boundary[1] = self.ego_object.pos[1] + self.boundary_offset[1]
    self.boundary[2] = self.ego_object.pos[0] + self.boundary_offset[2]
    self.boundary[3] = self.ego_object.pos[1] + self.boundary_offset[3]
  

  def is_pos_in_boundary(self, pos):
    if ( self.boundary[0] <= pos[0] <= self.boundary[2] and \
      self.boundary[1] < pos[1] < self.boundary[3]):
      return True
    else:
      return False


  def viz(self):
    plt.figure(1)
    plt.gca().set_xlim([self.boundary[0], self.boundary[2]])
    plt.gca().set_ylim([self.boundary[1], self.boundary[3]])
    self.ego_object.viz()
    self.road.viz()
    for obj in self.objects:
      obj.viz()

    

# functions


# main
def main():
  pass

if __name__ == "__main__":
  main()