from operator import truediv

age = 19 #integer
weight = 45.78 #float
greetings = "Hello there" #string
ismammal =  True #Boolean


# Data strucures- multiple elements in one variable
fruits = ["Banana", "Mango", "Cherry"] # list-ordered and changeable
courses =["MIT", "Datascience" ,"Cybersecurity"]
cars = ( "Ford", "Mustang", "Toyota", "mazda", "G-Wagon") #Tuple -Elements and unchangeable
countries = {"Kenya", "Tanzania","Italy"} #Set-Unordered and Unchangeable
Student = {
    "FirstName" : "Jeff",
                  "Course" : "MIT",
                "Age" :17,
                "nationality" :"Kenya"
    #Dictoinary-Key Value Pair

}



print("Student is" ,age,"years old" )
print(weight)
print("is animal a mammal ?" ,ismammal)
print(fruits)
print(countries)

#Typecasting-It is converting one data type to another

print(float(age))
print(int(weight))