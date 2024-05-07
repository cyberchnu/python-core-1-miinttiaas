def int_within_bounds(number, lower_bound, upper_bound):
  if type(number) != int:
    return False
  if number < lower_bound or number >= upper_bound:
    return False
  else:
    return True
