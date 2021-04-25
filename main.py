import pyautogui as auto
from time import sleep 

class App:
  x = 200
  y = 900
  action = 'right'

  def right_move_mouse(self):
    self.x += 100
    self.action = 'right'
    auto.moveTo(self.x, self.y)
    auto.mouseDown()
    auto.mouseUp()

  def left_move_mouse(self):
    self.x -= 100
    self.action = 'left'
    auto.moveTo(self.x, self.y)
    auto.mouseDown()
    auto.mouseUp()

  def start(self, delay):
    while True:
      if self.action == 'left':
        self.right_move_mouse()
      elif self.action == 'right':
        self.left_move_mouse()
    
      sleep(delay)

application = App()
application.start(5)