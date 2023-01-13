#ЗАДАНИЕ 5

for N in range(516): 
  b='{N:b}'
  if N%2 == 0:
    b+= '10'
  else:
      b = '1' + b + '01'
  if int (b,2) > 516:
    print(N)
    break

#ЗАДАНИЕ 8

l='44040'
s=int(l,5)
print (s)
