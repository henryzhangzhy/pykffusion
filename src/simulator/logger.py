""" the logger class

Author: Henry Zhang
Date:August 24, 2019
"""

# module
from matplotlib import pyplot as plt
import math
from copy import deepcopy
import numpy as np

# parameters


# classes
class Logger():
  def __init__(self, fig_name=None):
    self.unique_data = {}
    self.timed_data = {}
    self.fig_name = fig_name
  
  def add_unique(self, dic):
    for key, value in dic.items():
      self.unique_data[key] = value
  
  def add_timed(self, time, dic):
    for key, value in dic.items():
      if not key in self.timed_data:
        self.timed_data[key] = {}
      self.timed_data[key][time] = deepcopy(value)

  def plot_error(self):
    if (not 'objs' in self.timed_data) or (not 'estimation' in self.timed_data):
      return
    else:
      time_list = []
      error_list = []
      innovation_list = []
      
      for time, estimates in self.timed_data['estimation'].items():
        if time in self.timed_data['objs']:
          
          error_time = []
          innovation_time = []
          objs = self.timed_data['objs'][time]
          
          for estimate in estimates:
            for obj in objs:
              if estimate.id == obj.id:
                error = math.hypot(estimate.state[0,0] - obj.pos[0], \
                                   estimate.state[1,0] - obj.pos[1])
                error_time.append(error)
                innovation_time.append(math.hypot(estimate.innovation[0], estimate.innovation[1]))
          
          if len(error_time) > 0:
            time_list.append(time)
            error_list.append( sum(error_time) / len(error_time))
            innovation_list.append( sum(innovation_time) / len(innovation_time))
      
      plt.scatter(time_list, error_list, c='r', label='error')
      plt.scatter(time_list, innovation_list, c='g', label='innovation')

      matrix = np.vstack([np.array(error_list), np.array(innovation_list)])
      print(np.corrcoef(matrix))


                


  def viz(self):
    if self.fig_name is None:
      pass
    else:
      plt.figure(self.fig_name)
      plt.title('logger visualization')
      self.plot_error()

      plt.legend()
    
    


  
  def write(self):
    pass
# functions


# main
def main():
  pass

if __name__ == "__main__":
  main()