import pyautogui as auto
import mouse
from time import sleep 

class App:
  x = 700
  y = 180
  count_action = 0
  action = 'right'

  def clickTarget(self):
    self.count_action += 1
    auto.click(self.x, self.y, duration = 0.5)
    sleep(1)
    print(f'click {self.count_action}')

  def right_move_mouse(self):
    self.x += 20
    self.action = 'right'
    self.clickTarget()

  def left_move_mouse(self):
    self.x -= 20
    self.action = 'left'
    self.clickTarget()

  def start(self, delay):
    print('Start!')
    while True:
      self.clickTarget()
      self.clickTarget()
      # if self.action == 'left':
      #   self.right_move_mouse()
      # elif self.action == 'right':
      #   self.left_move_mouse()
    
      sleep(delay)

application = App()
application.start(59)