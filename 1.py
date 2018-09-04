url=["www.annauniv.edu","www.google.com","www.ndtv.com","www.website.org","www.bis.org.in","www.rbi.org.in"]
dom=[]
urls=[]
for i in url:
    str=i.split('.')
    dom.append(str[-1])
dom.sort()
for j in dom:
    for k in url:
        str1=k.split('.')
        if (j==str1[-1] and k not in urls):
            urls.append(k)
        else:
            continue
print "The sorted list based on the domain is:",urls
        
       
        
        
    

