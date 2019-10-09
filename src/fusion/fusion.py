""" the Multi Sensor Fusion class

Author: Henry Zhang
Date:August 23, 2019
"""

# module
from matplotlib import pyplot as plt

from src.fusion.tracker import Tracker
from src.fusion.point import Point2D
from src.fusion.box import Box2D
from src.fusion.proposal import Proposal
from src.sensor.lidar_proc import LidarProc

# parameters


# classes
class Fusion():

  def __init__(self):
    pass
  
  def estimate(self, observations):
    pass
  
class MultiSensorFusion(Fusion):
  
  def __init__(self, mode='sequential', fig_name=None):
    print('sequential fusion has the assumption that data come in this batch are of same time stamp, \
      thus make a prediction forward to the same time.')
    super(MultiSensorFusion, self).__init__()
    self.mode = mode
    self.trackers = []
    self.proposals = []
    self.new_proposals = []
    self.estimations = []
    self.max_forget_time = 0.1
    self.fig_name = fig_name
    
  
  def estimate(self, observations, time_acc):
    ''' given the sensor data and time stamp, return the estimation

    param:
      observations: a list of sensor data
      time_acc: accumulated simulation time as a time stamp
    return:
      estimations: estimated states of the objects
    '''
    proposals = self.sensing_module(observations)
    estimations = self.fusion_module(proposals)

    self.clean_track(time_acc)
    self.merge_trackers()
    self.viz()

    return estimations
  
  def sensing_module(self, observations):
    ''' generate proposals from observations '''
    proposals = []

    for single_sensor_observations in observations:
      if single_sensor_observations.type == 'Lidar':
        continue
      single_sensor_proposals = self.generate_proposal(single_sensor_observations)
      for proposal in single_sensor_proposals:
        proposals.append(proposal)

    self.proposals = proposals
    return proposals
  
  def generate_proposal(self, observations):
    ''' Create models from given proposals. '''
    proposals = []

    if observations.type == 'Radar':
      for obs in observations.data:
        proposal = Proposal(observations.time, [Point2D(obs.x, obs.y, obs.vx, obs.vy, obs.id)])
        proposals.append(proposal)
    elif observations.type == 'Lidar':
      for obs in observations.data:
        models = LidarProc.find_models(observations.time, obs)
        proposal = Proposal(observations.time, models)
        proposals.append(proposal)
    elif observations.type == 'Camera':
      raise NotImplementedError
    else:
      raise NotImplementedError

    return proposals


  def fusion_module(self, proposals):
    ''' Fuse proposals and trackes. '''
    if (self.mode == 'sequential'):
      self.sequential_fusion(proposals)
    elif (self.mode == 'group'):
      self.group_fusion(proposals)
    elif (self.mode == 'information'):
      self.information_fusion(proposals)
    else:
      raise NotImplementedError

    return self.update_estimation()
  
  def group_fusion(self, proposals):
    raise NotImplementedError
  
  def information_fusion(self, proposals):
    raise NotImplementedError

  def update_estimation(self):
    estimations = []

    for tracker in self.trackers:
      estimations.append(tracker.estimate)
    
    self.estimations = estimations
    return estimations
  
  def sequential_fusion(self, proposals):
    self.predict(proposals)
    matched_pairs, new_proposals = self.associate(proposals)
    self.update(matched_pairs)
    self.initialize(new_proposals)
  
  def predict(self, proposals):
    ''' Make a prediction to the time of observation '''
    for tracker in self.trackers:
      tracker.predict(proposals[0].time)
  
  def associate(self, proposals):
    new_proposals = []
    matched_pairs = []
    
    for proposal in proposals:
      matched_pair = self.find_best_associate_pair(proposal)
      if len(matched_pair) > 0:
        matched_pairs.append(matched_pair)
      else:
        new_proposals.append(proposal)

    self.new_proposals = new_proposals
    return matched_pairs, new_proposals

  def find_best_associate_pair(self, proposal):
    pairs = []
    for model in proposal.models:
      for tracker in self.trackers:
        score = tracker.find_associate_score(model)
        if not score is None:
          pairs.append((score, tracker, model))
    if len(pairs) == 0:
      return []
    else:
      sorted(pairs, key=lambda x: x[0])
      return (pairs[0][1], pairs[0][2])
  
  def initialize(self, new_proposals):
    ''' create a tracker for each model from each proposal '''
    for proposal in new_proposals:
      for model in proposal.models:
        tracker = Tracker(proposal.time, model)
        self.trackers.append(tracker)
  
  def update(self, pairs):
    """for tracker in self.trackers:
      tracker.update()"""
    for pair in pairs:
      pair[0].associate(pair[1])
      pair[0].update()
  
  def clean_track(self, time_acc):
    new_trackers = []

    for tracker in self.trackers:
      print(tracker.id, time_acc, tracker.update_time, self.max_forget_time)
      if time_acc - tracker.update_time < self.max_forget_time:
        new_trackers.append(tracker)
      else:
        del tracker
    
    self.trackers = new_trackers
  
  def merge_trackers(self):
    merge_pair = []
    for tracker_i in self.trackers:
      for tracker_j in self.trackers:
        if not (tracker_i is tracker_j):
          if tracker_i.is_close(tracker_j):
            merge_pair.append((tracker_i,tracker_j))
            break
    if len(merge_pair) != 0:
      self.merge_two_trackers(merge_pair[0])
      self.merge_trackers()
    else:
      return
  
  def merge_two_trackers(self, pair):
    new_trackers = []
    
    for tracker in self.trackers:
      if (not tracker is pair[0]) and (not tracker is pair[1]):
        new_trackers.append(tracker)
    
    merged_tracker = pair[0].merge(pair[1])
    new_trackers.append(merged_tracker)

    self.trackers = new_trackers

  def viz(self):
    if self.fig_name is None:
      pass
    else:
      plt.figure(self.fig_name)
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