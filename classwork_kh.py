### Problem 1:
# Create a function that will ask the user for a number. Use the function to get two numbers from the user, then pass the two numbers to a function. Add, subtract, multiple, and divide the numbers.


def askUser(num1,num2):
    
    userResults(num1,num2)
def userResults(num1,num2):
    total = num1 - num2
    total1 = num1+num2
    total2 = num1*num2
    total3 = num1/num2
    print(f'subtraction: {ask1} - {ask2} = {total}')
    print(f'addition: {ask1} + {ask2} = {total1}')
    print(f'multiplication: {ask1} x {ask2} = {total2}')
    print(f'division: {ask1} / {ask2} = {total3}')

ask1 = int(input("Enter a number "))
ask2 = int(input("Enter another number "))
askUser(ask1,ask2)
