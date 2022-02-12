"""
1
22
333
4444
55555
where n =5
"""


n=int(input())
i=1
while(i<=n):
    j=1
    while j<=i:
        print(i,end="")
        j+=1
    print()
    i=i+1