i=1
j=0
l=0
k=input("enter the number to find the steps:")
while(j!=k):
    if((j+i)<=k):
        j=j+i
    else:
        j=j-i
    l=l+1
    i=i+1
print l
