def showEmployee(empname , salary=5000):

    print("Your name is " + empname + " and your salary is " + str(salary))


name = input("Enter your name : ")
sal = input("Enter you salary : ")

if not sal:
    showEmployee(name)
else:
    showEmployee(name,int(sal))
