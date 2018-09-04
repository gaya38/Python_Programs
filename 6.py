bookstore={"New Arrivals":{"COOKING":["Everyday Italian","Giada De Laurentiis","2005","30.00"],"CHILDREN":["Harry Potter","J K.Rowling","2005","29.99"],"WEB":["Learning XML","Erik T.Ray","2003","39.95"]}}
a=bookstore["New Arrivals"]
b=a['WEB']
b=b+a['COOKING']
b=b+a['CHILDREN']
print b


