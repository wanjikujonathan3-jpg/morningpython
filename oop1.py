class Employee :

    #attribute
    def __init__(self,fullname,position,status,age):
        self.fullname = fullname
        self.position = position
        self.status = status
        self.age = age

    def work(self):
        print (self.fullname,"is working")


employee1 = Employee("Ken","MD","Married",43)
print(employee1.fullname,employee1.position,employee1.status,employee1.age)
employee1.work()
employee2 =Employee("Jean","Technical manager","Married",33)
employee3 =Employee("Mark job"," manager","single",26)