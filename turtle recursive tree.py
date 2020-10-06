import turtle
import random

'''branch_count = 5
TURN_ANGLE = 30
branch_size = 100
SHRINK_FACTOR = 0.8

speed = 10
up = 90

def tree(size, depth=0):
  if depth <= branch_count:
    turt.forward(size)
    turt.right(TURN_ANGLE)
    tree(size*SHRINK_FACTOR, depth+1)
    turt.left(2*TURN_ANGLE)
    tree(size*SHRINK_FACTOR, depth+1)
    turt.right(TURN_ANGLE)
    turt.backward(size)

if __name__ == '__main__':
  turt = turtle.Turtle()
  turt.setheading(up)
  turt.width(4)
  turt.speed(SPEED)

  tree(branch_size)
  turtle.done()'''

BRANCH_COUNT = 7
TURN_ANGLE = 10
SHRINK_FACTOR = 0.8

def tree(size, depth):
  if depth >= 1:
    if random.random() > 0.39:
      turt.width(depth)
      turt.color(get_color(depth))
      turt.forward(size)
      turt.right(TURN_ANGLE)
      tree(size*SHRINK_FACTOR, depth-1)
      turt.right(TURN_ANGLE)
      tree(size*SHRINK_FACTOR, depth-1)
      turt.left(3*TURN_ANGLE)
      tree(size*SHRINK_FACTOR, depth-1)
      turt.left(TURN_ANGLE)
      tree(size*SHRINK_FACTOR, depth-1)
      turt.right(2*TURN_ANGLE)
      turt.color(get_color(depth))
      turt.backward(size)

def get_color(depth):
  if BRANCH_COUNT - depth < 2.5:
    return 'brown'
  else:
    return 'chartreuse'

if __name__ == '__main__':
  
  turt = turtle.Turtle()
  turt.setheading(90)
  turt.speed(1000)
  turtle.colormode(255)
  tree(30, BRANCH_COUNT)
  turtle.done()