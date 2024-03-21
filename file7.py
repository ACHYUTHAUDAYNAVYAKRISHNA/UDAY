# 18-03-24


#-----> aeesment

#1). dict1 = {'ten': 10,'twenty': 20,'thirty': 30}
#2). dict2 =  {'thirt':30,'fourty': 40,'fifty':50}
'''
d1 = {'ten': 10,'twenty': 20,'thirty': 30}
d2 =  {'thirt':30,'fourty': 40,'fifty':50}
d1.update(d2)
print(d1)
'''

#2) python program to determine if
# the given sets are disjoint
# or not with out using inbuilt-in functions

'''
set1 = {'python','java','Data science'}
set2 = {'ML','AI','R Language','python'}
set3 = {'Data Analytics','Robotics','Deep Learning'}

c =0
flag=0
for val in range(3):
    c=c+1
    if c==1:
       for val in set1:
           if val in set2 or val in set3:
               flag=1
               break
    if c==2:
        for val in set2:
            if val in set1 or val in set3:
                flag=1
                break
    if c==3:
if flag==0:
    print("disjoint")
else:
    print("joint")
'''



#3).
'''
l3 =[]
list1 = ["M","na","i","ke"]
list2 = ["y","me","s","lly"]
for val in range (len(list1)):
    ans= list1[val]+list2[val]
    13.append(ans)
print(l3)

'''
#   or
'''
list1 = ["M","na","i","ke"]
list2 = ["y","me","s","lly"]
i=0
while i<len(list1):
    l3.append(list1[i]+list2[i])
    i+=1
print(l3)
'''
# Hacker rank---> caesar cipher 

# functions 
#DEF
'''
*fumction is a block of code which is used to perfom a specific functionality
*Function can be created using def keyword
'''
# Generally fumction has 3 three parts
'''
*function decleration
*function defination
*function call
'''


##--> eg  : 1
'''
def greet ():# function defanition
    print("greeting User!!")

greet()
greet()
greet()
greet()   # function calling 
'''

#   eg: 2
# Function with parameter
'''
def greting(name):
    print("Welcome",name)

for val in range(3):
    username = input("Enter the name:")
    greeting(username)# uesrname is argument

'''
def profile(name,age,place):
    print(name,age,place)
profile("uday",20,"AP")
    



#  Eg : 3















