""" the Tracker class that handles tracking using filter

Author: Henry Zhang
Date:August 23, 2019
"""

# module
import math
import matplotlib.pyplot as plt

from src.fusion.kalman_filter import KalmanFilter
from src.fusion.point import Point2D
from src.fusion.box import Box2D

# parameters


# classes
class Tracker():
  def __init__(self, proposal):
    self.model = self.initialize(proposal)
    self.observation = None
    self.state = self.model.x_post
    self.update_time = 0
  
  def initialize(self, proposal):
    return proposal.generate_filter()

  def predict(self, time_acc):
    self.model.predict(time_acc - self.update_time)
    self.state = self.model.x_pre
    self.update_time = time_acc
  
  def update(self):
    if not self.observation is None:
      self.model.update(self.observation)
      self.state = self.model.x_post
  
  def associate(self, proposal):
    ''' associate track and proposal, return True if success and update observation, False if not associated '''
    threshold = 2
    if math.hypot(proposal.model.x - self.state[0], proposal.model.y - self.state[1]) < threshold:
      self.observation = proposal.model.generate_observation()
      return True
    else:
      self.observation = None
      return False
  
  def viz(self):
    plt.scatter(self.state[0], self.state[1], c='r', marker='o', label='tracker')
    plt.text(self.state[0], self.state[1] + 2, 'v:({:.1f}, {:.1f})'.format(self.state[2], self.state[3]))
# functions


# main
def main():
  pass

if __name__ == "__main__":
  main()