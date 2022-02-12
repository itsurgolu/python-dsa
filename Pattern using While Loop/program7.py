""" WAP to Print
   *
  **
 ***
****
where n =4
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
        print("*",end="")
        st+=1
    print()
    r+=1

