""" the Point model class

Author: Henry Zhang
Date:August 23, 2019
"""

# module
import numpy as np
import matplotlib.pyplot as plt

from src.fusion.kalman_filter import KalmanFilter

# parameters


# classes
class Point2D():
  def __init__(self, x, y, vx, vy, ax=0, ay=0):
    ''' constant acceleration 2D point model '''
    self.x = x
    self.y = y
    self.vx = vx
    self.vy = vy
    self.ax = ax
    self.ay = ay
  
  def generate_filter(self):
    state = np.array([self.x, self.y, self.vx, self.vy, self.ax, self.ay])
    variance = np.diag([0.1, 0.1, 0.5, 0.5, 1.0, 1.0])
    transition_matrix = np.array([[0, 0, 1, 0, 0, 0],
                               [0, 0, 0, 1, 0, 0],
                               [0, 0, 0, 0, 1, 0], 
                               [0, 0, 0, 0, 0, 1],
                               [0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0]])
    observation_matrix = np.eye(state.shape[0])
    control_matrix = 0
    process_noise = np.diag([0.1, 0.1, 0.1, 0.1, 0.1, 0.1])
    observation_noise = np.diag([0.1, 0.1, 0.5, 0.5, 1.0, 1.0])
    
    return KalmanFilter(x_prior=state, \
                        P_prior=variance, \
                        mtx_transition=transition_matrix, \
                        mtx_observation=observation_matrix, \
                        mtx_control=control_matrix, \
                        noise_process=process_noise, \
                        noise_observation=observation_noise)
  def generate_observation(self):
    return np.array([self.x, self.y, self.vx, self.vy, self.ax, self.ay])
  
  def viz(self):
    plt.scatter(self.x, self.y, c='y', marker='o', label='proposal')
    plt.text(self.x, self.y + 1.5, 'v:({:.1f}, {:.1f})'.format(self.vx, self.vy))

# functions


# main
def main():
  pass

if __name__ == "__main__":
  main()