""" the Kalman Filter class

Author: Henry Zhang
Date:August 23, 2019
"""

# module
import numpy as np

# parameters


# classes
class KalmanFilter():
  def __init__(self, x_prior, P_prior, mtx_transition, mtx_observation, mtx_control, noise_process, noise_observation):
    self.x_prior = np.array(x_prior)
    self.x_pre = np.array(x_prior)
    self.x_post = np.array(x_prior)
    self.P_prior = np.array(P_prior)
    self.P_pre = np.array(P_prior)
    self.P_post = np.array(P_prior)
    self.mtx_transition = mtx_transition
    self.mtx_control = mtx_control
    self.mtx_observation = mtx_observation
    self.noise_process = noise_process
    self.noise_observation = noise_observation
    self.innovation = np.zeros(self.mtx_observation.shape[0])
    self.innovation_cov = np.zeros(self.noise_observation.shape)
    self.gain = None
  
  def predict(self, dt, u=0):
    self.x_pre += dt * (self.mtx_transition @ self.x_post + np.dot(self.mtx_control, u))
    self.P_pre += (dt**2) * (self.mtx_transition @ self.P_post @ self.mtx_transition.T + self.noise_process)
  
  def update(self, z):
    self.innovation = z - self.mtx_observation @ self.x_pre
    self.innovation_cov = self.noise_observation + self.mtx_observation @ self.P_pre @ self.mtx_observation.T
    self.gain = self.P_pre @ self.mtx_observation @ np.linalg.inv(self.innovation_cov)
    self.x_post = self.x_pre + self.gain @ self.innovation
    self.P_post = self.P_pre - self.gain @ self.innovation_cov @ self.gain.T

# functions


# main
def main():
  pass

if __name__ == "__main__":
  main()