from Node import Node

class LinkedList:

  def __init__(self):
    self.head = None


  def append(self, key, value):
    new_node = Node(key, value)
    new_node.next = self.head
    self.head = new_node


  def find(self,item):

    current = self.head
    found = False
    counter = 0

    while current != None and not found:
# changing the data value
      if current.data[0] == item:
        found = True
      else:
        current = current.next
        counter += 1

    if found:
      return counter
    else:
      return -1

  def length(self):
    if self.head == None:
      return 0
    else:
      counter = 1
      current = self.head
      while(current.next):
        current = current.next
        counter +=1
      return counter

  def remove_song(self, title):
    current_song = self.head

    if current_song.get_title()[0] == title: 
      item = current_song.get_title()
      self.head = current_song.get_next_song()
      return item
    else: 
      while current_song.get_title()[0] != title:
        if current_song.get_next_song().get_title()[0] == title: 
          item = current_song.get_title()
          current_song.set_next_song(current_song.get_next_song().get_next_song())
          return item
        else: 
          current_song = current_song.get_next_song()


  def print_nodes(self):
    current = self.head
    
    if current == None:
      print('The linked list is empty.')
    else:
      for i in range(self.length()):
        print(f'Node {i}: {current.data}')
        current = current.next