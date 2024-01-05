import random
choices=['rock','paper','scissors']
comp_win=0
user_win=0
game=int(input("enter the number of times uh want to play"))
for i in range(game) :
    user=input("enter your choice('rock','paper','scissors'):")
    comp=random.choice(choices)
    print(comp)
    if user==comp:
        print("tie")
    elif ((user=="rock" and comp=="scissors") 
          or(user=="paper" and comp=="rock")
          or(user=="scissors" and comp=="paper")):
              print("you win")
              user_win+=1
    else:
        print("you loss")
print("final score:")
print(comp_win)
print(user_win)
