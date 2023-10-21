from art import logo
from art import vs
from game_data import data
import random
import os

def printKeys(data,str):
  if str == 'A':
    print('Compare A:')
  else:
    print(vs)
    print('Against B:')
  for keys in data:
    if keys != 'follower_count':
      print(f'My {keys} is {data[keys]},')

print(logo)
points = 0
win_and_continue = True

def compare(data1, data2):
  first = data1['follower_count']
  second = data2['follower_count']
  if first > second:
    return 'A'
  else :
    return 'B'


while win_and_continue:
  randomData1 = random.choice(data)
  randomData2 = random.choice(data)
  printKeys(randomData1,'A')
  printKeys(randomData2,'B')
  userGuess = input('\nWho has more followers?: ')
  correctAnswer = compare(randomData1,randomData2)
  if userGuess == correctAnswer:
    points += 1
    os.system('clear')
    print(f'CORRECT! +1 point! Your score is now {points}\n')
  else:
    win_and_continue = False
    print('Incorrect')

if points < 3:
  print(f"Thats all you can do? You ONLY scored {points} points.")
elif points >= 3 and points <= 6:
  print(f"Average people score between 3 and 6. You scored {points} points.")
else :
  print(f"Fantastic! You scored {points} points.")