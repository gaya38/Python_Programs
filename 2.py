a=input("Enter the list:")
count=0
for i in a:
    if(len(i)>=2 and i[0]==i[-1]):
        count = count+1        
print "the count as per the requirement is:",count
