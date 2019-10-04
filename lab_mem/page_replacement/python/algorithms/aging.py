# This is the file where you must implement the Aging algorithm

# This file will be imported from the main code. The PhysicalMemory class
# will be instantiated with the algorithm received from the input. You may edit
# this file as you whish

# NOTE: there may be methods you don't need to modify, you must decide what
# you need...

ALGORITHM_AGING_NBITS = 8
"""How many bits to use for the Aging algorithm"""

class Aging:
  def __init__(self):
    self.recentlyReferenced = {}
    self.minPrioBits = ALGORITHM_AGING_NBITS * 8
    self.allFrames = []

  def put(self, frameId):
    startingPrio = 1<<self.minPrioBits
    self.allFrames.append([frameId, startingPrio])
  
  def evict(self): 
    minPrio = 1 << (self.minPrioBits + 1)
    for frameId, prio in self.allFrames:
      if prio < minPrio:
        minPrio = prio
    for i in range(len(self.allFrames)):
      if(self.allFrames[i][1] == minPrio):
        returnValue = self.allFrames[i][0]
        self.allFrames.pop(i)
        return returnValue
    return - 1
    

  def clock(self):
    for i in self.allFrames:
      frameId,prio = i
      bitAux = 0
      if self.recentlyReferenced.has_key(frameId):
        bitAux = 1
      prio = (prio >> 1) + (bitAux << self.minPrioBits)
      i[1] = prio
    self.recentlyReferenced = {}

  def access(self, frameId, isWrite):
    self.recentlyReferenced[frameId] = 1
