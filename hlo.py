a="hello  all"
print (a)
print (len(a))

a="hello all"
print(a[2:7])

a="hii i am annu"
print ("am" in a)
print ("hlo" in a)
if "hii" in a:
    print ("yes,'hii' in a string")
else :
    print("no,'hii' in a string")

message="i am annu rao"
print(message[3:5])
print (message[-5:-3])
print (a.lower())
print(message.replace('annu','anisha'))


a="annu"
b="rao"
c=a+""+b
print(c)
#concantinate


a="annu"
print(a[2])
#indexing

a="hii annu "
print(a[3:7])
#slicing


a="hello"
print(a.upper())
#upper()

a="RIGHT"
print(a.lower())
#lower()

a="   hii annu    "
print(a.strip())
#strip=remove space

a="my name is annu"
print(a.replace("annu","anisha"))
#replace()

a="annu anisha anny"
print(a.split())
#split()=convert string to list

a="hlo my name is annu rao"
print(a.find("name"))
#find()

a="hlooooooooooo"
print(len(a))
#len()

a="hii i am annu"
print(a.title())
#title=first letter of each word capital



x=10 #global variable
def mess ():
    print(x)
mess ()
print(x)


def text():
    y=20 #local variable
    print(y)
text()



x=10 #global variable
def mess():
    y=20 #local variable
    print("Global:",x)
    print("local:",y)
mess()  
print("global outside function",x) 





#list_name=["annu","anisha","anny"]
fruits=["apple","banana","cherry"]
print(fruits)


#append()=add an item to the end of the list
a=["apple","banana","cherry"]
a.append("orange")
print(a)

#insert()=add an item at the specified index
a=["apple","banana","cherry"]
a.insert(1,"orange")
print(a)

#remove()=remove the specified item
a=["apple","banana","cherry"]
a.remove("banana")
print(a)

#pop()=remove the specified index
a=["apple","banana","cherry"]
a.pop(1)
print(a)

#delete()=remove the specified index
a=["apple","banana","cherry"]
del a[0]
print(a)

#CLEAR()=remove all the items from the list
a=["apple","banana","cherry"]
a.clear()
print(a)


#SLICE()=return a part of the list
a=["apple","banana","cherry","orange","kiwi","melon","mango"]
print(a[2:5])


#replace()=replace the specified item with the new item
a=["apple","banana","cherry"]
a[1]="orange"
print(a)


#reverse()=reverse the order of the list
a=["apple","banana","cherry"]
a.reverse()
print(a)


#sort()=sort the list
a=["apple","banana","cherry"]
a.sort()
print(a)


#copy()=copy the list
a=["apple","banana","cherry"]
b=a.copy()
print(b)


#count()=return the number of times the specified item appears in the list
a=["apple","banana","cherry","apple"]
print(a.count("apple"))


#count()=return the number of times the specified item appears in the list
a=["apple","banana","cherry","apple"]
print(a.count("apple"))



#index()=return the index of the first occurrence of the specified item
a=["apple","banana","cherry"]
print(a.index("banana"))



#list length
a=["apple","banana","cherry"]
print(len(a))



#nested list
a=["apple","banana","cherry",["kiwi","melon","mango"]]
print(a)


#list concatenation
a=["apple","banana","cherry"]
b=["orange","grape","mango"]
c=a+b
print(c)


#loop through a list
a=["apple","banana","cherry"]
for x in a:
    print(x)