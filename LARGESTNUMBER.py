first = int(input("enter the first number"))
second = int(input("enter the second number"))
third = int(input("enter the third number"))


if first > second > third :
    print(first, "is the greatest number")
elif second>third and second > first :
    print(second, "is the greatest number")

else:
    print(third, "is the greatest number")