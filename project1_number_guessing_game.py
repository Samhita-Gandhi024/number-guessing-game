def line():
    print()
    print("-"*50)
    print()
line()
print("WELCOME TO NUMBER GUESSING GAME")
line()
print("Rules for this game:")
print("1.You have to guess a number")
print("2.For correct guess you will earn +1 point")
print("3.For wrong guess your point will be deducted by 1")
print("4.You have to guess within the given range only otherwise your point will not be considered")
print("5.There will be total 5 attempts")
line()
print("ALL THE BEST")
line()
n=int(input("Enter your guess between 1 to 10="))
c={1,2,3,4,5,6,7,8,9,10}
c=list(c)
import random as r
e=0
for i in range(1,6):
    d=r.choice(c)
    print(d)
    if n==d:
        print("Correct")
        e=e+1
    if n!=d:
        print("Wrong")
        e=e-1
    if n>10:
        print("Outside the range")

    if i==5:
        break
    else:
        n=int(input("Enter your guess between 1 to 10="))
line()
print("total score=",e)
if e==5:
    print("Excellent")
elif e==4:
    print("Good job")
elif e==3:
    print("Well tried")
else:
    print("Better luck next time")
line()
print("THANKYOU")