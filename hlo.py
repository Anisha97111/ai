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
