from wyliodrin import *
from movement import *
from monster import *


SER = 0
SRCLCK = 2
RCLCK = 1


W = 6
H = 2

# complete this vector

FRIENDS = [
  
]

initCommunication()

"""

sendMessage('andysstef@yahoo.com', 'l', json.dumps('Test'))

def myFunction(__sender, __channel, __error, __message):
  global message, d
  d = __sender
  message = json.loads(__message)
  sendSignal('', 0)

openConnection('label', myFunction)

"""

pinMode(SER, OUTPUT)
pinMode(RCLCK, OUTPUT)
pinMode(SRCLCK, OUTPUT)

def clear(v):
  global SER, SRCLCK, RCLCK, W, H
  
  digitalWrite(RCLCK, LOW)

  for j in range(H - 1, -1, -1):
    digitalWrite(SER, v)

    for i in range(W - 1, -1, -1):
      digitalWrite(SRCLCK, LOW)
      digitalWrite(SRCLCK, HIGH)

  digitalWrite(RCLCK, HIGH)
  

def draw_map(x, y):
  global SER, SRCLCK, RCLCK, W, H

  digitalWrite(RCLCK, LOW)
  
  for j in range(H - 1, -1, -1):
    for i in range(W - 1, -1, -1):
      flag = False
      
      for it in range(len(x)):
        if x[it] == i and y[it] == j:
          digitalWrite(SER, HIGH)
          flag = True
          break

      if flag == False:
        digitalWrite(SER, LOW)
      
      digitalWrite(SRCLCK, LOW)
      digitalWrite(SRCLCK, HIGH)

  digitalWrite(RCLCK, HIGH)

def main():
  global SER, SRCLCK, RCLCK, W, H, FRIENDS

  # def __init__(self, rate_press, rate_hold, w, h, pl, pd, pu, pr):
  player = Movement(1, 0, 6, 2, 11, 10, 9, 8)
  # def __init__(self, x, y, w, h, rate):
  monster = Monster(W - 1, H - 1, W, H, 1)

  s = raw_input("single/multi ?\n")
  if s == "single":
    print "Starting singleplayer. Enjoy :)"
    ct = 0
    while True:
      clear(LOW)
      player.Update()
      if ct >= 100:
        ct = 0
        monster.Update(player.x, player.y)
      
      draw_map([player.x, monster.x], [player.y, monster.y])
      ct = ct + 1
  
      if player.x == monster.x and player.y == monster.y:
        clear(HIGH)
        delay(3000)
  
        for i in range(3):
          clear(LOW)
          delay(500)
          clear(HIGH)
          delay(500)
        
        monster.x = W - 1
        monster.y = H - 1
        player.x = 0
        player.y = 0
      delay(10)
  else:
    print "Starting multiplayer"
    i = raw_input("master/slave?\n")
    
    if i == "master":
      pass
    else:
      pass
    
    
    while True:
      pass
    
if __name__ == "__main__":
  main()