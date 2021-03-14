num=int(input("Enter Number: "))
factorial=1
if num<1:
    print("Factorial is not available for negative number:")

elif num==0:
    print("factorial of 1 is zero: ")

else:
    for i in range(1,num+1):
        factorial=factorial*i
    print("factorial of",num,"is",factorial)