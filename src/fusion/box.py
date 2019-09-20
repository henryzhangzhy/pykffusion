""" the 2D box model class

Author: Henry Zhang
Date:August 23, 2019
"""

# module
import numpy as np
from matplotlib import pyplot as plt
import math

from src.util.utils import get_box_outline
from src.fusion.kalman_filter import KalmanFilter
# parameters


# classes
class Box2D():
  def __init__(self, x, y, orientation, yaw_rate, w, l, obj_id, v=0, a=0):
    self.x = x
    self.y = y
    self.orientation = orientation
    self.yaw_rate = yaw_rate
    self.w = w
    self.l = l
    self.v = v
    self.a = a
    self.id = obj_id
    self.filter = None
    self.type = 'Box'
  
  def generate_filter(self):
    state = np.array([self.x, self.y, self.v, self.a, self.orientation, self.yaw_rate, self.l, self.w])
    variance = np.diag([0.5, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
    transition_matrix = np.eye(state.shape[0])
    observation_matrix = np.eye(state.shape[0])
    control_matrix = 0

    process_noise = np.diag([0.5, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
    observation_noise = np.diag([4.0, 4.0, 1.5, 1.5, 1.0, 1.0, 1.0, 1.0])
    
    self.filter = KalmanFilter(x_prior=state, \
                        P_prior=variance, \
                        mtx_transition=transition_matrix, \
                        mtx_observation=observation_matrix, \
                        mtx_control=control_matrix, \
                        noise_process=process_noise, \
                        noise_observation=observation_noise)

  def generate_observation(self, target_type='Box'):
    if target_type == self.type:
      return np.array([self.x, self.y, self.v, self.a, self.orientation, self.yaw_rate, self.l, self.w ])
    elif target_type == 'point':
      theta_cos = np.cos(self.orientation)
      theta_sin = np.sin(self.orientation)
      return np.array([self.x, self.y, self.v*theta_cos, self.v*theta_sin, self.a*theta_cos, self.a*theta_sin])
  
  def predict(self, dt):
    self.update_mtx_transition(dt)
    self.filter.predict(dt)
  
  def update(self, z):
    self.filter.update(z)
  
  def update_mtx_transition(self, dt):
    theta = self.filter.x_post[4]
    v = self.filter.x_post[2]
    theta_cos = math.cos(theta)
    theta_sin = math.sin(theta)
    t_cos = dt * theta_cos
    t_sin = dt * theta_sin

    matrix = np.array([[1, 0, t_cos, t_cos * dt / 2, -v * t_sin, -v * t_sin * dt / 2, 0, 0],
                       [0, 1, t_sin, t_sin * dt / 2,  v * t_cos,  v * t_cos * dt / 2, 0, 0],
                       [0, 0,     1,             dt,          0,                   0, 0, 0], 
                       [0, 0,     0,              1,          0,                   0, 0, 0],
                       [0, 0,     0,              0,          1,                  dt, 0, 0],
                       [0, 0,     0,              0,          0,                   1, 0, 0], 
                       [0, 0,     0,              0,          0,                   0, 1, 0], 
                       [0, 0,     0,              0,          0,                   0, 0, 1]])
    self.filter.mtx_transition = matrix
  
  def get_orientation(self):
    orientation = self.orientation
    return orientation
  
  def viz(self):
    outline = get_box_outline(self.x, self.y, self.orientation, self.l, self.w)
    for line in outline:
      plt.plot(line[0], line[1], c='b')

# functions


# main
def main():
  pass

if __name__ == "__main__":
  main()