""" the proposal class

Author: Henry Zhang
Date:August 23, 2019
"""

# module


# parameters


# classes
class Proposal():
  def __init__(self, time, models):
    self.time = time
    self.models = models

  def viz(self):
    for model in self.models:
      model.viz()
# functions


# main
def main():
  pass

if __name__ == "__main__":
  main()