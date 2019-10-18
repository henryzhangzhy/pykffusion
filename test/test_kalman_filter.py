""" test for the Kalman Filter class

Author: Henry Zhang
Date:October 18, 2019
"""

# module
import numpy as np
import os, sys
sys.path.append(os.getcwd())
from src.fusion.kalman_filter import KalmanFilter

# parameters


# classes
class Test_KalmanFilter():
  def __init__(self):
    None
  
  def test_large_covariance_init(self):
    num_max = 1e10
    x_prior1 = np.array([0.,0.]).T
    P_prior1 =  np.array([[num_max, 0.],
                         [0., num_max]])
    mtx_transition1 = np.eye(2)
    mtx_observation1 = np.array([[1., 0.]])
    mtx_control1 = np.array([[0.0, 0.0]]).T
    noise_process1 = np.eye(2)
    noise_observation1 = np.array([[1.]])
    kf1 = KalmanFilter(x_prior1,
                 P_prior1,
                 mtx_transition1,
                 mtx_observation1,
                 mtx_control1,
                 noise_process1,
                 noise_observation1)

    z = np.array([1.0])
    kf1.update(z)
    print(kf1.x_post)
    print(kf1.P_post)
  
  def test_proposal_layer(self):
    num_max = 1e10

    # set up the first filter for proposal generation
    x_prior1 = np.array([0.,0.]).T
    P_prior1 =  np.array([[num_max, 0.],
                         [0., num_max]])
    mtx_transition1 = np.eye(2)
    mtx_observation1 = np.array([[1., 0.]])
    mtx_control1 = np.array([[0.0, 0.0]]).T
    noise_process1 = np.eye(2)
    noise_observation1 = np.array([[1.]])
    kf1 = KalmanFilter(x_prior1,
                 P_prior1,
                 mtx_transition1,
                 mtx_observation1,
                 mtx_control1,
                 noise_process1,
                 noise_observation1)

    z = np.array([1.0])
    kf1.update(z)
    print(kf1.x_post)
    print(kf1.P_post)

    # set up two identical filters

    x_prior2 = np.array([5.,5.]).T
    P_prior2 =  np.array([[4, 0.],
                         [0., 4]])
    mtx_transition2 = np.eye(2)
    mtx_observation2 = np.array([[1., 0.]])
    mtx_control2 = np.array([[0.0, 0.0]]).T
    noise_process2 = np.eye(2)
    noise_observation2 = np.array([[1.]])
    kf2 = KalmanFilter(x_prior2,
                 P_prior2,
                 mtx_transition2,
                 mtx_observation2,
                 mtx_control2,
                 noise_process2,
                 noise_observation2)

    z = np.array([1.0])
    kf2.update(z)
    print("direct update:")
    print(kf2.x_post)
    print(kf2.P_post)

    x_prior3 = np.array([5.,5.]).T
    P_prior3 =  np.array([[4, 0.],
                         [0., 4]])
    mtx_transition3 = np.eye(2)
    mtx_observation3 = np.array([[1., 0.],
                                [0., 1.]])
    mtx_control3 = np.array([[0.0, 0.0]]).T
    noise_process3 = np.eye(2)
    noise_observation3 = kf1.P_post

    kf3 = KalmanFilter(x_prior3,
                 P_prior3,
                 mtx_transition3,
                 mtx_observation3,
                 mtx_control3,
                 noise_process3,
                 noise_observation3)

    z = kf1.x_post
    kf3.update(z)
    print("added proposal layer:")
    print(kf3.x_post)
    print(kf3.P_post)


    

# functions


# main
def main():
  ts = Test_KalmanFilter()
  ts.test_large_covariance_init()
  ts.test_proposal_layer()

if __name__ == "__main__":
  main()