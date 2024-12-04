# Write all your codes for Day 3 here.
# REMEMBER to change main.py to import this file.
# You can COMMENT out the previous task before going on to the next task
# name=input("What is your name ? ")
# title=input("What is your title? ")
# people=input("Who do you want to command? ")
# command=input("what do you want people to do? ")
# print(title + " "+ name + " wants the " + people+  " to " +command)
# num1=int(input("Enter your first number."))
# num2=int(input("Enter your second number."))
# print(num1+num2)


# num1=input("Enter your first number")
# num2=input("Enter your second number")
# ans=str(int(num1)+int(num2))
# print(num1+"+"+num2+"="+ans)

# num1=input("Enter your first number")
# num2=input("Enter your second number")
# ans=str(int(num1)-int(num2))
# print(num1+"-"+num2+"="+ans)

# num1=input("Enter your first number ")
# num2=input("Enter your second number ")
# ans=str(int(num1)*int(num2))
# print(num1+"*"+num2+"="+ans)

# num1=input("Enter your first number ")
# num2=input("Enter your second number ")
# ans=str(int(num1)/int(num2))
# print(num1+"/"+num2+"="+ans)

# num1=int(input("Enter your first number "))
# num2=int(input("Enter your second number "))
# for i in range(1,num2+1):
#     print(str(i)+"x"+str(num1)+"="+str(i*num1))


# import random
# randNum=random.randint(1,10)
# userAns=int(input("Guess a number:"))

# if userAns==randNum:
#     print("Congratulations! You have won $1 billion dollars!")
# elif userAns==randNum>randNum:
#     print("Too high lol")
# else:
#     print("Too low lol")


userAns=int(input("What is your age? "))

if userAns<5:
    print("You are below 5")
elif userAns<10:
    print("You are between 5 to 9 years old")
else:
    print("You are at least 10 years old")





