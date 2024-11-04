##name = "Matt"
##question = "Are Mangos on sale in LIDL?"
##answer = ""
## Replaced hardcoded name & question with User Input

name = input("What is your name? ")
question = input("What question would you like to ask the Magic 8-Ball? ")

import random
random_number = random.randint(1,15)
#print(random_number)

if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good" 
elif random_number == 9:
  answer = "Very doubtful"
elif random_number == 10:
  answer = "Always"
elif random_number == 11:
  answer = "A week on Tuesday"
elif random_number == 12:
  answer = "Unclear"
elif random_number == 13:
  answer = "Of course"
elif random_number == 14:
  answer = "Absolutely not" 
elif random_number == 15:
  answer = "No."  
else:
  answer = "Error"  

#deals with no user input for name
if not name:   
   print("Question: " + question )
else:
  print(name + " asks: " + question )

#deals with no user input for question
if not question:
  print(f'You have to ask a Question {name}' )
else:
  print(f'Magic 8-Ball\'s answer: {answer}' )
