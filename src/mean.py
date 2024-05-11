def mean(number):
  number = str(number)
  l = list()
  for i in number:
    i = int(i)
    l.append(i)
  return int(sum(l)/len(l))

