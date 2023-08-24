import random

choose = input(
    'What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n')
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
rps = [rock, paper, scissors]

if (int(choose) <3):
  print(rps[int(choose)])
  print("Computer chose:")

  computerChoose = random.randint(0, 2)
  
  print(rps[computerChoose])
  
  if (int(choose) == 0 and computerChoose == 2 or int(choose) == 2 and computerChoose == 1
          or int(choose) == 1 and computerChoose == 0):
      print("You win!")
  elif (int(choose) == computerChoose):
      print("It's a draw")
  elif (computerChoose > int(choose)):
      print("You lose")
  elif (choose >=3):
    print("An error occure please retry")
else:
  print("An error occure please retry")