#Write a program to display all prime numbers within a range
s=int(input("enter a no"))
e=int(input("enter a no"))
i=2
while i<=e:
    if s%i==0:
        break
    else:
        print(s)
