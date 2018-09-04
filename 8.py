str1="Python is a widely used high-level programming language for general-purpose programming, created by Guido van Rossum and first released in 1991. An interpreted language, Python has a design philosophy which emphasizes code readability (notably using whitespace indentation to delimit code blocks rather than curly braces or keywords), and a syntax which allows programmers to express concepts in fewer lines of code than possible in languages such as C++ or Java. The language provides constructs intended to enable writing clear programs on both a small and large scale .Python features a dynamic type system and automatic memory management and supports multiple programming paradigms, including object-oriented, imperative, functional programming, and procedural styles. It has a large and comprehensive standard library. Python interpreters are available for many operating systems, allowing Python code to run on a wide variety of systems. CPython, the reference implementation of Python, is open source software and has a community-based development model, as do nearly all of its variant implementations. CPython is managed by the non-profit Python Software Foundation."
word="Python"
lst1=[',','.','(',')']
for char in str1:
    if char in lst1:
         str1=str1.replace(char,'')
str2=str1.split(" ")
m=dict()
key=word
m.setdefault(key,[])
for i in range(len(str2)):
    if (str2[i]==word):
        m[word].append(str2[i+1])
    else:
        continue
print "The dictionary with the paticular word and following values:"
print m
word2=input("Enter the word to print the likely words:")
print "print the likely words:"
for i in range(len(str2)):
    if (str2[i]==word2):
        print str2[i+1]
    else:
        continue


