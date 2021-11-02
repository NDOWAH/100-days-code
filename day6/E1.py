# NB functions like turn_left and move are in built for the case of reeborg.ca
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def navigate():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
      
for i in range(6):
    navigate()