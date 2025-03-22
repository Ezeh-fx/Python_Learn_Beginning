# print("Hello, world!")

# # Variable

# # strings
name = "John"

# # numbers
age = 30

# # float
height = 1.75

# # boolean
is_game = True

print("Name: " + name)
print("Age:", age)  # ✅ Works without str()
print("Height: ",height)
print("Is Game: ",is_game)

# Input
name = input("Enter your name: ")
print("Welcome, " + name + "!")

# Mathematics
x = 10
y = 20
print(x + y)  # 30
print(y - x)  # 10
print(x * y)  # 200
print(y / x)  # 2.0
print(y // x)  # 2
print(y % x)  # 0
print(y ** x) # 10240000000000

# Decision if ,Eilf ,Else
age = int(input("Enter your age: "))
if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")


# Loop Repeating Action

# while
count = 0
while count < 5:
    print("Count is, " , count) 
    count = count + 1

# for
vidoe_Game = ["Game", "Game2", "Game3"]
for game in vidoe_Game:
    print(game)


# list
print(vidoe_Game [0])

vidoe_Game.append("Game4")

vidoe_Game[1] = "Game5"
print(vidoe_Game)

# functions
def say_hello(person_name):
    print("Hello , " + person_name + " from the very first function")


say_hello("Emma")

def multiply(a,b):
    return a *b

result = multiply(3,15)
print("result" , result)