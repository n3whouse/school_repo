
class Box:
  # initialize class with self reference and LWH default values of 1, then have LWH refer to address calling class
  def __init__(self, length=1, width=1, height=1):
    self.length = length
    self.width = width
    self.height = height

  # accessors (getters)

  def get_length(self):
    return self.length
  def get_width(self):
    return self.width
  def get_height(self):
    return self.height
  
  # mutators (setters)
  def set_length(self, length):
    self.length = length

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height 

  def __repr__(self):
    return f"Box({self.length}x{self.width}x{self.height})"
  
  # make equal to avoid repetition
  __str__ = __repr__

  # define equality conditions. takes in self and other and compares LWH with strict AND so self and other can be compared with ==
  def __eq__(self, other):
    if not isinstance(other, Box):
      return False
    return (self.length == other.length and
              self.width == other.width and
              self.height == other.height)
  # find surface area
  def surface_area(self):
    return 2 * (self.length * self.width + 
                self.length * self.height + 
                self.width * self.height)
  # find volume
  def volume(self):
    return self.length * self.width * self.height