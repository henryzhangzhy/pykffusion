""" the Tracker class that handles tracking using filter

Author: Henry Zhang
Date:August 23, 2019
"""

# module
from src.fusion.kalman_filter import KalmanFilter

# parameters


# classes
class Tracker():
  def __init__(self, proposal):
    self.model = self.initialize(proposal)
    self.observation = None
    self.state = None
  
  def initialize(self, proposal):
    return KalmanFilter(x_prior, P_prior, mtx_transition, mtx_observation, mtx_control, noise_process, noise_observation)

  def predict(self, dt):
    self.model.predict(dt)
    self.state = self.model.x_pre
  
  def update(self):
    self.model.update(self.observation)
    self.state = self.model.x_post
  
  def associate(self, proposal):
    ''' associate track and proposal, return True if success and update observation, False if not associated '''
    self.observation = None
    return False

# functions


# main
def main():
  pass

if __name__ == "__main__":
  main()