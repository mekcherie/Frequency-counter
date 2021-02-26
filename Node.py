class Node:

  def __init__(self, key, value):
    self.data = (key, value)
    self.next = None

  def get_title(self):
    return self.data

  
  # TODO: Create a setter method for the next_song attribute, called set_title. Make sure titles are type cased to strings and are Title Cased.
  def set_title(self, key, value):
    self.data = (key, value)


  # TODO: Create a getter method for the next_song attribute, called get_next_song
  def get_next_song(self):
    return self.next


  # TODO: Create a setter method for the next_song attribute, called set_next_song
  def set_next_song(self, next_title):
    self.next = next_title