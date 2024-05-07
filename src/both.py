def both(number1, number2):
  if number1 > 0 and number2 > 0 or number1 < 0 and number2 < 0 or number1 == 0 and number2 == 0:
    return True
  else:
    return False

# print(both(3,4))
# print(both(0,0))
# print(both(-1,0))
