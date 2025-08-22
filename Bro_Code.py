# # This is my first Python Program
# print("I like Biryani")
# print("It's really good!")

# first_name = "Habib"
# food = "Pizza"
# email = "23cs016@students.muet.edu.pk"

# # f-string used for formatting strings
# # like concatenation in Java
# print(f"Hello {first_name}")
# print(f"you like {food}")
# print(f"your email id is {email}")

# #Integers
# age = 25
# quantity = 3
# num_of_students = 45

# print(f"you are {age} years old")
# print(f"you are buying {quantity} items")
# print(f"there are total {num_of_students} number of students in the class")

# # Float
# price=10.99
# gpa=3.42
# distance = 4.3

# print(f"price is {price}$")
# print(f"your gpa is {gpa}")
# print(f"you ran {distance} miles")

# # Booleans
# for_sale=True
# is_online=False

# if for_sale:
#     print("items is for sale")
# else:
#     print("Item is not available")

# if is_online:
#     print("You are Offline")
# else:
#     print("you are online")

# #Typecasting
# name="Habib"
# age=20
# gpa=3.5
# is_student=True

# print(type(gpa))

# age = str(age)
# age+="1"

# print(age)

# # input

# '''
#     num1 = input("Enter first number ")
#     num2 = input("Enter second number ")
#     sum=num1+num2
#     print("sum is ",sum) 
# '''
    


# # for i in range(int(2.0)):
# #         print(i, end=" ")


# # length = int(input("Enter the length: "))
# # width = int(input("Enter the width: "))
# # area=length*width
# # print(f"area of is: {area}cm²")


# def sum(a,b):
#     res=a+b
#     print(res)

# sum(5,6)


# number=2
# match number:
#     case 1:
#         print("one")
#     case 2 | 3:
#         print("either two or three")
#     case 4 | 5:
#         print("either four or five")
#     case _:
#         print("invalid number")

# a="I am global"
# print(a)

# def f():
    
#     global a
#     a="I am local"
#     print(a)

# f()
# print(a)

# username = input("Enter your username: ")

# if(len(username)) > 12:
#     print("Your username must be less than 12 characters")
# elif username.find(" ") != -1:
#     print("Your username must not spaces")
# elif not username.isalpha():
#     print("Your username must not contain numbers")
# else:
#     print(f"your username is {username}")


# import time

# my_time = int(input('Enter time in seconds: '))

# for x in range(my_time, 0, -1):
#     seconds=(x%60)
#     minutes=int(x/60)%60
#     hours=int(x/3600)
#     time.sleep(1)
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")

# print("Times UP")

# # Python quiz game
# questions= ("What is the capital city of Canada?",
#             "Which element has the chemical symbol ‘O’?",
#             "Who wrote the play Romeo and Juliet?",
#             "In computer programming, what does ‘HTML’ stand for?",
#             "What is the main function of the CPU in a computer?")

# options=(("A) Toronto", "B) Vancouver", "C) Montreal", "D) Ottawa"),
#          ("A) Gold", "B) Oxygen", "C) Osmium ", "D) Olivine"),
#          ("A) William Shakespeare", "B) Charles Dickens", "C) Jane Austen", "D) Leo Tolstoy"),
#          ("A) HyperText Machine Language", "B) Hyper Trainer Marking Language", "C) HyperText Markup Language", "D) HighText Modern Language"),
#          ("A) Storing data permanently", "B) Managing power supply", "C) Processing data and instructions", "D) Displaying graphics"))

# answers=("D","B","A","C","C")
# guesses=[]
# score=0
# question_num=0


# for question in questions:
#     print("----------------------")
#     print (question)
#     for option in options[question_num]:
#         print(option)
#     guess=input("Enter (A, B, C, D): ").upper()
#     guesses.append(guess)
#     if(answers[question_num]==guess):
#         score+=1
#         # print("CORRECT")
#     # else:
#     #     # print("INCORRECT")
#     #     # print(f"{answers[question_num]} is the correct answer")
#     question_num+=1


# print("-----------------------------")
# print("          RESULT             ")
# print("-----------------------------")
# print("answers: ", end=" ")
# for answer in answers:
#     print(answer, end=" ")
# print()

# print("guesses :", end= " ")
# for guess in guesses:
#     print(guess, end=" ")
# print()

# print(f"Your score out of 5 is {score}")

# def f(**kwargs):
#     for k, v in kwargs.items():
#         print("%s == %s" %(k,v), end = " ")


# f(s1='Hello', s2='MotherFucker 🤦‍♂️', s3='How was your sunday')

# class Book:

#     def __init__(self, title, author, num_pages):
#         self.title=title
#         self.author=author
#         self.num_pages=num_pages

#     def __str__(self):
#         return f"{self.title} by {self.author}"

# book1=Book("The Hobbit", "J.R.R. Tolkien",310)
# book2=Book("Harry POtter and the Philosopher Stone", "J.K. Rolling", 250)
# book3=Book("The Lion, the Witch and the Wardrobe", "C.S. Lewis", 160)

# print(book1)


import json

employee = {
    "name":"Habib",
    "age":20,
    "job":"Janitor"
}

file_path = "E:/python/output.json"

try:
    with open(file_path, "w") as file:
        json.dump(employee,file,indent=4)
        print(f"json file '{file_path}' was created")
except FileExistsError:
    print("That file already exist")






