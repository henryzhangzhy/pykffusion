""" the Tracker class that handles tracking using filter

Author: Henry Zhang
Date:August 23, 2019
"""

# module
import math
import matplotlib.pyplot as plt
import numpy as np
np.set_printoptions(precision=3)

from src.fusion.kalman_filter import KalmanFilter
from src.fusion.point import Point2D
from src.fusion.box import Box2D

# parameters


# classes
class Estimation():
  def __init__(self, obj_id, state, variance, innovation):
    self.id = obj_id
    self.state = state
    self.variance = variance
    self.innovation = innovation
  
  def is_close(self, estimate):
    state_diff = self.state - estimate.state
    diff_norm = np.linalg.norm(state_diff)
    print("diff_norm", diff_norm, self.id, estimate.id, state_diff)
    print(self.state, estimate.state)
    return diff_norm < 2

class Tracker():
  def __init__(self, time, model):
    self.model = self.initialize(time, model)
    self.observation = None
    self.id = self.model.id
    self.estimate = Estimation(self.id, \
                               self.model.filter.x_post, \
                               self.model.filter.P_post, \
                               self.model.filter.innovation)
    self.threshold_associate = 2
  
  def initialize(self, time, model):
    self.update_time = time
    self.predict_time = time
    model.generate_filter()
    return model 

  def predict(self, time_acc):
    self.model.predict(time_acc - self.predict_time)
    self.estimate = Estimation(self.id, \
                               self.model.filter.x_pre, \
                               self.model.filter.P_pre, \
                               self.model.filter.innovation)
    self.predict_time = time_acc
  
  def update(self):
    if not self.observation is None:
      self.model.update(self.observation)
      self.estimate = Estimation(self.id, \
                                 self.model.filter.x_post, \
                                 self.model.filter.P_post, \
                                 self.model.filter.innovation)
      self.update_time = self.predict_time
    else:
      pass
    
    self.observation = None
  
  def find_associate_score(self, model):
    ''' associate track and proposal, return True if success and update observation, False if not associated '''
    threshold = self.threshold_associate
    score = math.hypot(model.x - self.estimate.state[0], model.y - self.estimate.state[1])
    if score < threshold:
      return score
    else:
      return None
  
  def associate(self, model):
    ''' associate track and proposal, return True if success and update observation, False if not associated '''
    threshold = self.threshold_associate
    if math.hypot(model.x - self.estimate.state[0], model.y - self.estimate.state[1]) < threshold:
      self.observation = model.generate_observation()
      return True
    else:
      self.observation = None
      return False
  
  def is_close(self, tracker):
    return self.estimate.is_close(tracker.estimate)
  
  def merge(self, tracker):
    ''' return the one with a smaller innovation '''
    norm_self = np.linalg.norm(self.estimate.innovation)
    norm_else = np.linalg.norm(tracker.estimate.innovation)
    if norm_self < norm_else:
      return self
    else:
      return tracker
  
  def viz(self):
    plt.scatter(self.estimate.state[0], \
                self.estimate.state[1], \
                c='r', marker='o', label='tracker')
    plt.text(self.estimate.state[0], \
             self.estimate.state[1] + 2, \
             'Tid:{:d}, v:({:.1f}, {:.1f})'.format(self.id, \
                                                   self.estimate.state[2], \
                                                   self.estimate.state[3]))
                    
  
    
# functions


# main
def main():
  pass

if __name__ == "__main__":
  main()