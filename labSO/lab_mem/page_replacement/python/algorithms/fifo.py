# This is the file where you must implement the FIFO algorithm

# This file will be imported from the main code. The PhysicalMemory class
# will be instantiated with the algorithm received from the input. You may edit
# this file as you wish

# NOTE: there may be methods you don't need to modify, you must decide what
# you need...

class FIFO:

  def __init__(self):
    from Queue import Queue
    self.fila = Queue()

  def put(self, frameId):
    self.fila.put(frameId)

  def evict(self):
    return self.fila.get()

  def clock(self):
    # not necessary for FIFO
    pass

  def access(self, frameId, isWrite):
    # not necessary for FIFO
    pass
