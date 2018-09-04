a=input("Enter the list:")
i=0
while(i<len(a)-1):
    if (a[i]==a[i+1]):
       a.remove(a[i])
       i=i-1
    else:
        pass
    i=i+1
print a
 
