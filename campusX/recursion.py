# def multiply(a,b):
#     result=0
#     for i in range(0,b):
#         result=result+a
#         print(result)
# multiply(3,5)

#recursion
# def multiply(a,b):
#     if b==1:
#         return a
#     else:
#         return a+multiply(a,b-1)
# print (multiply(5,6))

#factorial
# def factorial(n):
#     if n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
    
# print(factorial(6))

def fib(n):
    if n==0 or n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print(fib(36))
