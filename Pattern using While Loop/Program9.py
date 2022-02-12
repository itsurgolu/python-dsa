"""
    1
   22
  333
 4444
55555
 where n =5
"""

n=int(input())
r=1
while r<=n:
    sp=1
    while sp<=n-r:
        print(end=" ")
        sp+=1
    st=1
    while st<=r:
        print(st,end="")
        st+=1
    print()
    r+=1
