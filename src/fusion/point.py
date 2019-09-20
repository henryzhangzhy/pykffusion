""" the Point model class

Author: Henry Zhang
Date:August 23, 2019
"""

# module
import numpy as np
import matplotlib.pyplot as plt
import math

from src.fusion.kalman_filter import KalmanFilter

# parameters


# classes
class Point2D():
  def __init__(self, x, y, vx, vy, obj_id, ax=0, ay=0):
    ''' constant acceleration 2D point model '''
    self.x = x
    self.y = y
    self.vx = vx
    self.vy = vy
    self.ax = ax
    self.ay = ay
    self.type = 'Point'
    self.filter = None
    self.id = obj_id
  
  def generate_filter(self):
    state = np.array([self.x, self.y, self.vx, self.vy, self.ax, self.ay])
    variance = np.diag([0.1, 0.1, 0.5, 0.5, 1.0, 1.0])
    transition_matrix = np.array([[1, 0, 0, 0, 0, 0],
                               [0, 1, 0, 0, 0, 0],
                               [0, 0, 1, 0, 0, 0], 
                               [0, 0, 0, 1, 0, 0],
                               [0, 0, 0, 0, 1, 0],
                               [0, 0, 0, 0, 0, 1]])
    observation_matrix = np.eye(state.shape[0])
    control_matrix = 0
    process_noise = np.diag([0.5, 0.5, 1.0, 1.0, 1.0, 1.0])
    observation_noise = np.diag([4.0, 4.0, 1.5, 1.5, 1.0, 1.0])
    
    self.filter = KalmanFilter(x_prior=state, \
                        P_prior=variance, \
                        mtx_transition=transition_matrix, \
                        mtx_observation=observation_matrix, \
                        mtx_control=control_matrix, \
                        noise_process=process_noise, \
                        noise_observation=observation_noise)
  
  def generate_observation(self, target_type='Point'):
    if target_type == self.type:
      return np.array([self.x, self.y, self.vx, self.vy, self.ax, self.ay])
    elif target_type == 'Box':
      orientation = math.atan2(self.vy, self.vx)
      v = math.hypot(self.vx, self.vy)
      a = math.hypot(self.ax, self.ay)
      return np.array([self.x, self.y, v, a, orientation, 0, 0, 0])
  
  def predict(self, dt):
    self.update_mtx_transition(dt)
    self.filter.predict(dt)
  
  def update(self, z):
    self.filter.update(z)
  
  def update_mtx_transition(self, dt):
    matrix = np.array([[1, 0, dt, 0, (dt**2)/2, 0],
                       [0, 1, 0, dt, 0, (dt**2)/2],
                       [0, 0, 1, 0, dt, 0], 
                       [0, 0, 0, 1, 0, dt],
                       [0, 0, 0, 0, 1, 0],
                       [0, 0, 0, 0, 0, 1]])
    self.filter.mtx_transition = matrix
  
  def get_orientation(self):
    orientation = math.atan2(self.vy, self.vx)
    return orientation
  
  def viz(self):
    plt.scatter(self.x, self.y, c='y', marker='o', label='proposal')
    plt.text(self.x, \
             self.y + 1.5, \
             'Pid:{:d}, v:({:.1f}, {:.1f})'.format(self.id, self.vx, self.vy))


# functions


# main
def main():
  pass

if __name__ == "__main__":
  main()