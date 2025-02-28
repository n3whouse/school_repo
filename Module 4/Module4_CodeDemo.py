
import random

answer = random.randint(1,10)
print (answer)
counter = 1
guess = int(input('Enter number in range 1..10: '))
while guess != answer:
  if guess > answer:
    print('Too high')
  else:
    print('Too low')
  counter = counter + 1
  guess = int(input('Enter number in range 1..10: '))

if counter == 1:
  print('Correct, it took you 1 try!')
else:
  print('Correct, it took you', counter, 'tries')