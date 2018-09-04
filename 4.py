a=input("Enter the list should be in the format of [(x,y,..),(x,y,..),...]:")
b=[]
c=[]
for i in a:
    b.append(i[-1])
b.sort()
for j in b:
    for i in a:
        if (j==i[-1] and i not in c):
            c.append(i)
        else:
            continue
print c
            

   
