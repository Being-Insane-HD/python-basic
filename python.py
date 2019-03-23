#printing or writing a sentence
print("hello world")

#if else condition
x=2
if x!=1:
    print("x is not 1")
else:
    print("x is 1")

#printing floating and integer values    
myint=int(7.01)	#will print integer values
print(myint)
myfloat=float(5/4)		#will print floating values
print(myfloat)


#printing a string
stringz="neural network begins"
print(stringz)

#arithmetic operations
a=5
b=6
c=a+b
d=a/b
e=a-b
f=a*b
g=a%b
print(c,d,e,f,g)

# joining two or more sentences
h1="Neural"
h2="Network"
h3="is great!!"
h=h1+" "+h2+" "+h3
print(h)

#assigning values to variables in sequence
a,b=3,4
print(a,b)	#will print 3 4, because in sequence of a,b 3&4 are arranged, hence a is assigned 3, b is assigned 4

#making list (similar to array)
l1=[]
l1.append(1)
l1.append(2)
l1.append(3)

for x in l1:
    print(x)

#string list
names = ["John", "Eric", "Jessica"]
second_name = "Eric"
print("The second name on the names list is %s" % second_name)

#two simultaneous * operator acts as 'to the power' operator
square=7**2
cube=5**3
print(square,cube)

#printing string repeatedly
lon="Hello World "*3
print(lon)

#combining different lists
l1=[1,3,5,7]
l2=[2,4,6,8]
l3=l1+l2
print(l3)

#printing a list multiple times
print([1,2,3]*3)

#printing a string in variables format
name = "nn"
age = 10
print("%s is %d years old." % (name, age))

#printing list in variable form
mylist = [1,2,3]
print("A list: %s" % mylist)

#string operations
astring = "welcome everyone."
print(len(astring))		#length
print(astring.index("a"))	#position of a certain character
print(astring[4:10])	#printing characters within the given positions
print(astring[2:10:2]) 	#(start,stop,step) code for skipping letters
print(astring[::-1]) 		#string reverse
print(astring.upper())	#uppercase
print(astring.lower())	#lowercase
print(astring.startswith("Neural")) 	#checks whether string starts with 'neural'
print(astring.endswith("aft")) 	#checks whether string ends with 'aft'
print(astring.split(" "))	#splits string by a certain character

#checking condition is true or not
x = 2
print(x == 2) 	# prints out True
print(x == 3) 	# prints out False
print(x < 3) 	# prints out True

#using and & or in conditions
name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")

name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")

#if elif else condition
x =1
if x == 2:
    print("x equals two!")
elif x==1:
    print("x equals to one!")
else:
    print("x does not equal to one or two.")

#Unlike the double equals operator "==", the "is" operator does
#not match the values of the variables, but the instances
#themselves

#not functions
print(not False) # Prints out True

#using for loop in list
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)
print(" ")

#using for loop for intervals
for x in range(3, 8, 2):    #(start,stop,step)
    print(x)                # Prints out 3,5,7
print(" ")

#while loop
# Prints out 0,1,2,3,4
count = 0
while count < 5:
    print(count)
    count += 1
print(" ")

#break function
# Prints out 0,1,2,3,4
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break
print(" ")

#continue function
# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)
print(" ")