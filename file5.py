## 15-03-2024.



### ---> common functon for list
'''
l1 = [6,7,8,9,6]
'''
#print(len(l1))
#print(max(l1))
#print(min(l1))

'''
l1 = [6,7,8,"P","u",]
print(max(l1))----- > error coz its a combination of input and string
print(min(l1))error coz its a combination of int and string



l1 = [6,7,8,9,0,5.65,-8,0.65]
print(min(l1))  # -8



l1 = [6,7,8,9,0,5.56,-5,0.78]
index() ---> to get index value of specific element
print( l1.index(9))
'''
##
'''
l1 = [6,6,6,7,8,0,8.78,-5,0.78]
count()  -- > how many num of times an element is repeated
print(l1.count(6))
'''


# some functons which is specifically used for list.
'''
insert(index_value, element)---> to add element at specific index position
l1 = [3,4,4,5,6,7,7,8,9,9,-6,6.65]
l1.insert(2, "cars")
print(l1)
'''

## to delete elment from list.

#l1 = [3,4,4,5,6,7,7,8,9,9,-6,6.65]
#pop()---> last element will be deleted
'''
l1.pop()
print()
'''

# pop(index_value) ---> used To delete element at specific index
'''
l1.pop(4) # is index value
print(l1)
'''
#remove(element) --> used to delete element directly
'''
l1.remove(8)
print(l1)
'''


#clear() ---> uesd to delete all  element .
'''
l1.clear()
print(l1)
'''

# del -> to delete the list
'''
del l1 # or del(l1)
print(l1)I
'''

#    ----> join 2 lists
'''
l1 = [9,0,8]
l2 = ["p", 'o", "t",34]
print(l1+l2)
'''
      # or

#extend()---> to combine 2 lists
'''
l1.extend(12)
print(l1)
'''
#   ---> copy ()
'''
l1 = [3,6,7,4,8,0]
l2 = l1.copy()
print(l2)
print(l1)

print(id(l1))
print(id(l2))
'''

# diff between shallow copy and deep copy
#shallow copy
# import copy
'''
l1 = [4,54,54,[5,45,5,5], [3,5,67]]
l2 = copy.copy(l1)
l1.append(890)
print(l1)
print(l2)
'''

#deep copy
#import copy

#l1 = [8,6,9,[6,8],[6,8,6]]
##print(l1[-1][1]) --- to index nested list
'''
l2 = copy.deepcopy(l1)
l1[-1).append('cars)
print(l1)
print(l2)
            
'''


#sort ---> arrange elemnets in list in ascending or decemding order
''''
l1 = [9,6,8,5,7,9,5,4,2,1]
l1.sort()  # to arrange in ascending order
print(l1)


l1.sort(revere=true) # to sort i decending order
print(l1)


l1 = ['z','i', 'o', 'p',9]
l1.sort()
print(l1)   #---- error

'''

#   ---> list constuctor
#list() ---> to conver other collecton datatype to list
'''
l3 = ((8,9,0))
print(list(l3))


l4 = (8,9)
print(list(l4))

'''


#    ---> nested list
#l1 - [8,9,[0,8,7],["p","o","Y"],[8, 't']]
'''
#print(l1[-2][1]  # --- o

#print(l1[1:4])
#print(l1[1:-1])

'''



#to delete "t" from l1
'''
l1 = [8,9,[0,8,7],["p","o","Y"],[8, 't']]

(l1[-1].remove('t')
 print(l1)
'''

 #combine these ["p","o","y"],[8,'t'] lists in l1 to ["p","o","y",8,'t'] lists in l1

#l1 = [8,9,[0,8,7],["p","o","Y"],[8, 't']]
'''
l1[-2].extend(l1[-1]
l1.pop(-1)
print(l1)              
'''



# ----> tuple
#   char of tuple

'''
1.)tuple have to be surrounded by ()
2) the elements inside tuple are not changeble
3)the elements inside tuple are indexed
4) the element will excute in order
5)it is heterogenous
6)it allow duplicate elements

'''



# eg : tuple

#t1 = (8,8,9,6,5.78,[9,0],(6,8),"hey",9+6j)
'''
print(t1)
print(type(t1))
'''

#   indexing, slicing are all smae as list





#ways to create tuple
'''
l1 = (8)
print(type(l1) # int

l1 = (8,)
print(type(l1) # tuple
'''












#to add element inside tuple ---> cannot add
#cannot delete any element from tuple
'''
join 2 tuples
t1 = (8,9,0)
t2 = (6,7,8)
print(t1+t2)

'''
# to all elements inside list and tuple
'''
sum()
l1 = (8,9,7,6)
print(sum(l1))

'''
#sort tuple
'''
t1 =(8,9,0,45,12)
print(tuple(sorted(t1)))
print(tuple(sorted(t1,reverse=gtrue)))
'''
#iterate list and tuples
'''
l1 = [8,5,6,9,0]
for i in l1:
    print(i)
'''


# iterate based in index value
'''
l1 = [9,8,0,6,5]
for i in range(0,len(l1)):
      print(l1[i])
'''

#   --- > strings .

#s1 = "o"
# print(type(s1))


s1 = "U"
#print(type(s1))


S1 = "hello world"
 ##--->  to acces the string 
 #print(s)
 #  indexing and slicing ---> same as list and tuple 

#print(s1[0:5]



#  ---> common functoins

#len(),min(),max(),index(),count()
'''
s1 = 'hello world"
print(len(S1))
print(max(s1))
print(min(s1))
'''


# ord()---> used to find the ASCII value of a charecter
# s1 = 'u'
# print(ord(s1))


# functions of string
'''
s1 = "hello world"
'''


# to convert all charecters to upper case
'''
print(s1.upper())
'''




# to convert to lower case
# s1 = "HFRDGiou"
#print(s1.lower())



# strip()---> to eliminating the space un begginging and of string.
'''
s1 = "where are you?"
print(s1.lstrip())
print(s1.rstrip())
print(s1.strip())
'''



# split() --> to spilt the words in string based on a charecter
'''
s1 = "where are you?"
print(s1.split(" "))

print(s1.count('e')
'''

# replace () --> to replace a specific chsr in tjhe string
#s1 = "HEY there"
'''      
s1= "where are you ?"
print(s1.replace('r','&&'))
'''

 # swapcase() --> to convert capital to small and to capital
'''
s1 = "HEY there"      
print(s1.swapcase())
'''
# title() --> to write the string in fprmat of title
'''
s1 = 'never giveUP'
print(s1.title())
'''
# capitalize()---> 1st char of string will be converted to capital
'''
s1 = 'never giveUP'
print(s1.capitalize())
'''


# join the string
'''
s1 = "hello"
s2 = 'world'
print(s1+s2)
'''

#s1 =
'''
how are you
iam fine
hey there
'''

# splitlines()----> used to split the string based on lines
'''
print(s1.splitlines())
'''

# find ()--->to find the index based on a charecter 
'''
s1 = "hello world "
print(s1.find('z'))
print(s1.index('z'))
'''



# join() --->

'''
l1 = ["hey", "there"]
print(" ".join(l1))
print("$".joi(l1))
'''


#s1 = "welocome to all"
'''
print(s1.endswith('1'))
print(s1.startwith("w"))
'''
'''
s1 = "67"
print(type(s1))
print(s1.isdigit())
'''

# print the string in reverse manner
'''
s1 = "welcome to all"
print(s1[::-1])
'''


# eg : 1

#wap to find the number of lower case letters
'''
s1 = "HEY there you aRE"
count = 0
for i in s1:
    if i.islower():
        count+=1
print("the total num of lower case letters: ",count)
'''


## ---- eg : 2 "$"
'''
s1 = 'restarter'
s1 = "IMAGIN"
fst = s1[0]
bal = s1[1:]
txt = bal.replace(fst,"$")
print(fst+txt)

'''

#   eg: 3

s1 = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum"

chracters = len(s1)
print(chracters)


words = s1.split(" ")
print(len(words))



sentenses = s1.split('.')
for val in sentenses:
    if val =='':

       index=(sentenses.index(''))
       sentense.pop(index)
print(len(sentenses))

space =0
for val in s1:
    if val == " ":
        space=space+1
print(space)


















