class Rectangle:


 def __init__(self, x, y, h, w):
   self.x=max(0,x)
   self.y=max(0,y)
   self.height=max(0,h)
   self.width=max(0,w)
   
 def __str__(self):
    s="(x: {}, y: {}) height: {}, width: {}"
    return s.format(self.x, self.y, self.height, self.width)