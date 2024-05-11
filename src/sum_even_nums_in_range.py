
def sum_even_nums_in_range(start, stop):
  list_of_even_numbers = []
  for n in range(start, stop+1):
    if n % 2 == 0:
      list_of_even_numbers.append(n)
      print(n)
  return sum(list_of_even_numbers)

