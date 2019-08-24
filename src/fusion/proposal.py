""" the proposal class

Author: Henry Zhang
Date:August 23, 2019
"""

# module


# parameters


# classes
class Proposal():
  def __init__(self, time, model):
    self.time = time
    self.model = model
  
  def generate_filter(self):
    fter = self.model.generate_filter()
    fter.update_time = self.time
    return fter

  def viz(self):
    self.model.viz()
# functions


# main
def main():
  pass

if __name__ == "__main__":
  main()