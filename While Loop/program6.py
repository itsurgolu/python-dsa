#Display Fibonacci series up to 10 terms
a=int(input("Enter a value of a"))
b=int(input("Enter a value of b"))
end=int(input("enter a end value"))
i=a
fibbo=0
while(i<=end):
    print(fibbo)
    fibbo=a+b
    a=b
    b=fibbo

    i+=1
