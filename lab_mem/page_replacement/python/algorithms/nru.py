# This is the file where you must implement the NRU algorithm

# This file will be imported from the main code. The PhysicalMemory class
# will be instantiated with the algorithm received from the input. You may edit
# this file as you wish

# NOTE: there may be methods you don't need to modify, you must decide what
# you need...

class NRU:

  def __init__(self):
    self.frames = {}

  def put(self, frameId):  
    if not self.frames.has_key(frameId):
      self.frames[frameId] = [0,0]
  
  def evict(self):
    actLowestPrio = 4
    evictFrame = -1
    for key in self.frames.keys():
      act = self.frames[key]
      if act[0]*2 + act[1] <= actLowestPrio:
        actLowestPrio = act[0]*2 + act[1]
        evictFrame = key
    if self.frames.has_key(evictFrame):
      self.frames.pop(evictFrame)
    return evictFrame
  
  def clock(self):
    for key in self.frames.keys():
      self.frames[key] = [0,self.frames[key][1]]
  
  def access(self, frameId, isWrite):
    if self.frames.has_key(frameId):
      if isWrite: 
        self.frames[frameId] = [1,1]
      else:
        self.frames[frameId] = [1, self.frames[frameId][1]]

