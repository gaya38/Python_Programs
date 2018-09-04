a=input("Enter the input list:")
b=[]
c=[]
for i in a:
    if (i[0]=='x' or i[0]=='X'):
        b.append(i)
    else:
        c.append(i)
b.sort()
c.sort()
b=b+c
print b
