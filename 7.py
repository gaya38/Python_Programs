str1="Python is a widely used high-level programming language for general-purpose programming, created by Guido van Rossum and first released in 1991. An interpreted language, Python has a design philosophy which emphasizes code readability (notably using whitespace indentation to delimit code blocks rather than curly braces or keywords), and a syntax which allows programmers to express concepts in fewer lines of code than possible in languages such as C++ or Java. The language provides constructs intended to enable writing clear programs on both a small and large scale .Python features a dynamic type system and automatic memory management and supports multiple programming paradigms, including object-oriented, imperative, functional programming, and procedural styles. It has a large and comprehensive standard library. Python interpreters are available for many operating systems, allowing Python code to run on a wide variety of systems. CPython, the reference implementation of Python, is open source software and has a community-based development model, as do nearly all of its variant implementations. CPython is managed by the non-profit Python Software Foundation."
lst1=[',','.','(',')']
lst2=[]
lst3=[]
cnt=[]
for char in str1:
    if char in lst1:
         str1=str1.replace(char,'')
str2=str1.split(" ")
for i in range(len(str2)):
    count=0
    for j in range(len(str2)):
        if (str2[i]==str2[j] and str2[i] not in lst2):
            count=count+1
        else:
            continue
    lst2.append(str2[i])
    if (count>0):
        lst=[str2[i],count]
        lst3.append(lst)
dict1=dict(lst3)
print "entire string as a dictionary:"
print dict1
b=[]
c=[]
for i in lst3:
    b.append(i[-1])
b.sort()
for j in b:
    for i in lst3:
        if (j==i[-1] and i not in c):
            c.append(i)
        else:
            continue
print "the top 5 words:"
for i in range(-1,-6,-1):
    print c[i]
