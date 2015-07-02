from wyliodrin import *


class Button:
  
  
  def __init__(self, pin,):
    pinMode(pin, INPUT)
    self.pin = pin
    self.pressed = False

  def Update(self, *args, **kwargs):
    v = digitalRead(self.pin)
    if v and not self.pressed:
      self.pressed = True

    elif not v and self.pressed:
      self.pressed = False

      
  def IsPressed(self):
    return self.pressed
