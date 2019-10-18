import os
os.system( 'clear' )

class Node:
  def __init__(self, value=None, next_node=None):

    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):

    return self.value

  def get_next(self):

    return self.next_node

  def set_next(self, new_next):

    # set this node's next_node reference to the passed in node
    self.next_node = new_next


class LinkedList:

  def __init__(self):

    # reference to the head of the list
    self.head = None

  def add_to_head(self, value):

    print( value )

    node = Node(value)

    if self.head is not None:
      node.set_next(self.head)
    
    self.head = node

  def contains(self, value):

    if not self.head:
      return False

    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head

    # check to see if we're at a valid node 
    while current:

      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True

      # update our current node to the current node's next node
      current = current.get_next()

    # if we've gotten here, then the target node isn't in our list
    return False

  def reverse_list(self):

    # TO BE COMPLETED

    if not self.head:
      return None

    else:

      head = self.head
      bloop = []
      max_depth = []

      if bloop == []:
        if self.head:
          bloop.append( self.head.value )
          max_depth.append( self.head )

      if not self.head.next_node:
        print( 'NOOOO' )

      if self.head.next_node:

        max_depth.append( head.next_node )

        if head.next_node.next_node:

          max_depth.append( head.next_node.next_node )

          if head.next_node.next_node.next_node:

            max_depth.append( head.next_node.next_node.next_node )

            if head.next_node.next_node.next_node.next_node:

              max_depth.append( head.next_node.next_node.next_node.next_node )

              if head.next_node.next_node.next_node.next_node.next_node:

                max_depth.append( head.next_node.next_node.next_node.next_node.next_node )

              else:
                print( 'Max depth exceeded' , max_depth)
            else:
              print( 'Max depth exceeded' , max_depth)
          else:
            print( 'Max depth exceeded' , max_depth)
        else:
          print( 'Max depth exceeded' )
      else:
        print( 'Max depth exceeded' , max_depth )


      answer = []

      for i in range( len( max_depth ) ):

        if answer == []:
          answer.append( max_depth[i].value )
        else:
          answer.insert( len( answer ) , max_depth[i].value )

      print( answer )

      for i in range( len( answer ) ):
        LinkedList.add_to_head( self , answer[i] )