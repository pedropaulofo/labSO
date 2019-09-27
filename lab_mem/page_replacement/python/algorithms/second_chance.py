# This is the file where you must implement the Second Chance algorithm

# This file will be imported from the main code. The PhysicalMemory class
# will be instantiated with the algorithm received from the input. You may edit
# this file as you wish

# NOTE: there may be methods you don't need to modify, you must decide what
# you need...

class SecondChance:

  def __init__(self):
    self.allocatedFrames = [] #frames
    self.second_chance = []   #boolean list
    self.pointer = 0

  def put(self, frameId):
    if(frameId not in self.allocatedFrames)
      self.allocatedFrames.append(frameId)
      self.second_chance.append(False)
    else:
      pos = self.allocatedFrames.index(frameId)
      self.second_chance[pos] = True


  def evict(self):
    pass

  def clock(self):
    pass

  def access(self, frameId, isWrite):
    pass
