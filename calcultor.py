#Create a simple calculator program using pyhon

number = int(input ( "please enter number "))
operator = input("please enter an operator ")
num2 =int(input("please enter a second num2"))


if operator == "+":
              print("the sum is" , number+num2 )
if operator == "-":
     print('the difference is', number - num2)

if operator == "*":
     print("the product is", number * num2)
