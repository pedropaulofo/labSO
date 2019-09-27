# This is the file where you must implement the LRU algorithm

# This file will be imported from the main code. The PhysicalMemory class
# will be instantiated with the algorithm received from the input. You may edit
# this file as you wish

# NOTE: there may be methods you don't need to modify, you must decide what
# you need...

class LRU:

  def __init__(self):
    self.allocatedFrames = []
    self.lastUse = []

  def put(self, frameId):
    self.lastUse = [use + 1 for use in self.lastUse]
    if(frameId not in self.allocatedFrames)
      self.allocatedFrames.append(frameId)
      self.lastUse.append(0)
    else:
      pos = self.allocatedFrames.index(frameId)
      self.lastUse[pos] = 0

  def evict(self):
    pass

  def clock(self):
    pass

  def access(self, frameId, isWrite):
    pass
