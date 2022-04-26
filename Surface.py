from Rectangle import Rectangle

class Surface:
  def __init__(self,file,x,y,h,w):
    self.image=file
    self.rect=Rectangle(x,y,h,w)

  def getRect(self):
    return self.rect