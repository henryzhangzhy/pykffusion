""" the logger class

Author: Henry Zhang
Date:August 24, 2019
"""

# module
from matplotlib import pyplot as plt

# parameters


# classes
class Logger():
  def __init__(self):
    self.unique_data = {}
    self.timed_data = {}
  
  def add_unique(self, dic):
    for key, value in dic.items():
      self.unique_data[key] = value
  
  def add_timed(self, time, dic):
    for key, value in dic.items():
      # print(key)
      if not key in self.timed_data:
        self.timed_data[key] = {}
        # print('created for {}, now in {}'.format(key, key in dic))
      self.timed_data[key][time] = value

  def viz(self):
    pass
  
  def write(self):
    pass
# functions


# main
def main():
  pass

if __name__ == "__main__":
  main()