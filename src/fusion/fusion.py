""" the Multi Sensor Fusion class

Author: Henry Zhang
Date:August 23, 2019
"""

# module
from src.fusion.tracker import Tracker

# parameters


# classes
class Fusion():

  def __init__(self):
    pass
  
  def estimate(self, observations):
    pass
  
class MultiSensorFusion(Fusion):
  
  def __init__(self, mode='sequential'):
    super(MultiSensorFusion, self).__init__()
    self.mode = mode
    self.trackers = []
    self.new_proposals = []
    self.estimations = []
    
  
  def estimate(self, observations):
    self.sensing_module(observations)

    self.fusion_module()

    return self.estimation
  
  def sensing_module(self, observations):
    proposals = []
    self.proposals = proposals
  
  def fusion_module(self):
    if (self.mode == 'sequential'):
      self.sequential_fusion()
    elif (self.mode == 'group'):
      self.group_fusion()
    elif (self.mode == 'information'):
      self.information_fusion()
    else:
      raise NotImplementedError

    self.update_estimation()
  
  def group_fusion(self):
    raise NotImplementedError
  
  def information_fusion(self):
    raise NotImplementedError

  def update_estimation(self):
    estimations = []

    for tracker in self.trackers:
      estimations.append(tracker.state)
    
    self.estimations = estimations

  
  def sequential_fusion(self):
    self.predict()
    self.associate()
    self.initialize()
    self.update()
  
  def predict(self):
    for tracker in self.trackers:
      tracker.predict()
  
  def associate(self):
    new_proposals = []
    
    for proposal in self.proposals:
      matched = False
      for tracker in self.trackers:
        if tracker.associate(proposal) == True:
          matched = True
      if matched == False:
        new_proposals.append(proposal)
    
    self.new_proposals = new_proposals
  
  def initialize(self):
    for proposal in self.new_proposals:
      tracker = Tracker(proposal)
      self.trackers.append(tracker)
  
  def update(self):
    for tracker in self.trackers:
      tracker.update()
  
  def create_tracker(self, proposal):
    pass
  

    


# functions


# main
def main():
  pass

if __name__ == "__main__":
  main()