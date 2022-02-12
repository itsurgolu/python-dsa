"""
1
12
123
1234
12345
 where n =5
"""
n=int(input())
i=1
while(i<=n):
    j=1
    while j<=i:
        print(j,end="")
        j+=1
    print()
    i=i+1