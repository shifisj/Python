pos = -1
list = [10,20,30,40,50,60]
n = int(input('Number to be searched: '))
for i in range(len(list)):
      if list[i] == n:
           globals()['pos'] = i
           print('Found at position: ',pos+1)
           break
else:
        print('Sorry, not found')