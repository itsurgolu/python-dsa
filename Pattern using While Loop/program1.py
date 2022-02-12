'''print the pattern :-
*****
*****
*****
*****
where n =5'''

n=int(input("enter a no")) #5
r=1
while r<=n: #row r<=n
    c=1
    while c<=n:
        print("*" , end=" ")
        c+=1
    print()
    r+=1