""" the Multi Sensor Fusion class

Author: Henry Zhang
Date:August 23, 2019
"""

# module
from src.fusion.tracker import Tracker
from src.fusion.point import Point2D
from src.fusion.box import Box2D
from src.fusion.proposal import Proposal

# parameters


# classes
class Fusion():

  def __init__(self):
    pass
  
  def estimate(self, observations):
    pass
  
class MultiSensorFusion(Fusion):
  
  def __init__(self, mode='sequential'):
    print('sequential fusion has the assumption that data come in this batch are of same time stamp, \
      thus make a prediction forward to the same time.')
    super(MultiSensorFusion, self).__init__()
    self.mode = mode
    self.trackers = []
    self.proposals = []
    self.new_proposals = []
    self.estimations = []
    
  
  def estimate(self, observations):
    self.sensing_module(observations)

    self.fusion_module()

    self.viz()

    return self.estimations
  
  def sensing_module(self, observations):
    ''' generate proposals from observations '''
    proposals = []
    for single_sensor_observations in observations:
      single_sensor_proposals = self.generate_proposal(single_sensor_observations)
      for proposal in single_sensor_proposals:
        proposals.append(proposal)
    self.proposals = proposals
  
  def generate_proposal(self, observations):
    proposals = []
    if observations.type == 'Radar':
      for obs in observations.data:
        proposal = Proposal(observations.time, Point2D(obs[0], obs[1], obs[2], obs[3]))
        proposals.append(proposal)
    return proposals


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
    self.update()
    self.initialize()
  
  def predict(self):
    for tracker in self.trackers:
      tracker.predict(self.proposals[0].time)
  
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
  
  def viz(self):
    for proposal in self.proposals:
      proposal.viz()
    for tracker in self.trackers:
      tracker.viz()

  

    


# functions


# main
def main():
  pass

if __name__ == "__main__":
  main()