# This is the file where you must implement the LRU algorithm

# This file will be imported from the main code. The PhysicalMemory class
# will be instantiated with the algorithm received from the input. You may edit
# this file as you wish

# NOTE: there may be methods you don't need to modify, you must decide what
# you need...

class LRU:

  def __init__(self):
    self.frames = []

  def put(self, frameId):
    self.frames.append(frameId)

  def clock(self):
    pass
  
  def evict(self):
    frameId = self.frames[0]
    self.frames.pop(0)
    return frameId
  
  def access(self, frameId, isWrite):
    for i in xrange(len(self.frames)):
      if self.frames[i] == frameId:
        actFrameId = self.frames[i]
        self.frames.pop(i)
        self.frames.append(actFrameId)
