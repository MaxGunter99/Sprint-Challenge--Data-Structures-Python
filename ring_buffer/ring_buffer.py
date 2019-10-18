import os
os.system( 'clear' )

class RingBuffer:
  def __init__(self, capacity):

    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    
    print( '\n' )
    
    # If storage is full
    if self.current == len( self.storage ):

      print( '--- Storage is full ---' )

      # Reset index / counter
      self.current -= len( self.storage )

      # Start popping values and replacing them with new ones ( counter / current increases )
      self.storage.pop( self.current )
      self.storage.insert( self.current , item )
      self.current += 1

    # If storage is not full
    else:

      # Start popping values and replacing them with new ones ( counter / current increases )
      print( f'Adding: { item } ' )
      self.storage.pop( self.current )
      self.storage.insert( self.current , item )
      self.current += 1

  def get(self):

    answer = []

    for i in range( len( self.storage ) ):

      if self.storage[ i ] is not None:
        answer.append( self.storage[i] )

    print( f'Returning: { answer } ' )

    return answer