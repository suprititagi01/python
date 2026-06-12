#Arguments
def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("well come")


greet("raja","hadimani")
## key word argument
def increment(number, by):
    return number + by

print(increment(2, 1))
#Default funcation
def increments(number, by=1):
    return number + by 

print(increments(2))

#*args,what,wait
#def multiply(*numbers):
  #  for number in numbers:
 #    print(number)

#multiply(2,1,5,6)

def multiply(*numbers):
    total = 1
    for number in numbers:
         total *= number
    return total

print(multiply(2,1,5,6))

#**args
'''def save_user(**user):
    print(user)
save_user(id=1, name="supi", age=22)'''
def save_user(**user):
    print(user["name"])
save_user(id=1, name="supi", age=22)

##Excersise upon fizz_buzz
def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input

print(fizz_buzz(7))
