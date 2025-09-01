#Strings
''''
print("hello world")
print('Hello World')
print("""Hello World""")
print("\n")
print("Hello"+"World")
'''

#Math
'''
print(10+10) #add
print(10-1) #substract
print(10*10) #multiply
print(10/10) #divide
print(10+10-10*10/10) #pemdas
print(10**2) #exponents
print(10%2) #remainder
print(10//2) #no remainder

'''

#variables and methods
'''
age=87
gpa=4.5
name="Allen"
age+=1
print(age)
print(int(87.4))
print(name.upper())
print(name.lower())
print(len(name))
print("My name is "+name+"and I am "+str(age)+" years old")
'''

#user input
'''
x=int(input("Give me number: "))
y=int(input("Give me a number"))
print(x+y)
'''

#function
'''
def who_am_i(name,age):
    print(F"My name is {name} and I am {age} years old")
who_am_i("adil",35)

def add(num):
    print(num+200)
add(100)

def numbers(x,y):
    print(x+y)
    print(x-y)
    print(x*y)
    print(x/y)
numbers(8,3)

def greet(name='Hello'):
    print("Hello"+name)
greet()
'''
#Boolean expressions
''''
bool1=True
bool2=False
bool3=3*3==9
print(bool1,bool2,bool3)

#relational and boolean operators

greater_then =7>5
less_than=6<3
greater_than_equal =5>=8
less_than_equal = 4<=1

print(greater_then,greater_than_equal,less_than,less_than_equal)

test_and = 5>4 and 4<5
test_or =5>6 or 4>2
test_not =not True
print(test_and,test_or,test_not)
'''

#conditional statements
'''
def drink(money):
    if money<2:
        return ("Here is your drink")
    else:
        return("Sorry for now")
print(drink(1))

def chem(age,money):
    if (age<21) and (money<=10):
        return("Immatured")
    elif (age>21) and (money<30):
        return("Not eligible")
    else:
        return("Not a girl anymore")
print(chem(22,5))
'''

#loops
'''
fruits=['apple','mango','orange']
for fruit in fruits:
    print(fruit)
#while loop
i=1
while i<10:
    print(i)
    i+=1
password=""
while password!="Adil":
    password=input("enter password")
    print("Access Granted")
'''
#building calculator
x=float(input("Give me a number: "))
o=input("Give me an operator: ")
y=float(input("Give me a number: "))

if o=="+":
    print(x+y)
elif o=="-":
    print(x-y)
elif o=="*":
    print(x*y)
elif o=="/":
    print(x/y)
elif o=="%":
    print(x%y)
else:
    print("Unknown operator")