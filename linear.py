def search(x, data):
  for i in range(len(data)):
    if data[i] == x:
      return i
  return -1

data = [10,20,30,40,50,60]
x = int(input('Number to be searched: '))
pos = search(x, data)
if pos >= 0:
  print('Found at position: ', pos+1)
else:
  print('Sorry, not found')
