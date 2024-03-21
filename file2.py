# variables.





#a=7,8
#print(a)
#print(type(a))


#a,b,c = 9,8,7,8
#print(a, b, c)


#a, b=c=7, 8
#print(a)
#print(b)
#print(c)

#a=b, c=4,2
#print(a,b,c)


# ----> swapping of variables
a = 7
b = 5

#example : 1
'''
temp=a #temp=7
a=b    #a=5
b=temp #b=7
'''

#a=5, b=7
#print(a,b)


# Example :2
'''
a=a+b #a=12
b=a-b #b=12-7=5
a=a-b #a=12-5=7

print(a,b)
a, b=b, a  # only in python
#print(a,b)

'''
'''
a=a*b  #a=35
b=a/b  #b=35/7 =5.0
a=a/b  #a=35/5=7.0
print(int(a), int(b))
'''
# id()---> used to find the memory address of the variable
#a=7
#b=8
#print(id(a))
#print(id(b))


#------>  key words
#keywords are reserved words provides special meaning to
# compiler or interpretor


'''
import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))
print(type(keyword.kwlist))

'''


# to check if the string is keyword or not
#print(keyword.iskeyword("sid"))#false


# if = 8
# print(if) # error coz if is a keyword

#  ! ----> literals
'''
*literal is the constant value assigned to a variable
*A variableis consider to be constant when it is dines 
*in caps
'''
#a= 78 # a is variable
#A=78 # A is constant

#hash()---> it creates a hash value for constant datatypes and
#provides error for non constant datatypes
#n1 = 89+7j
#print(hash(n1))


#f1 = [7,8,9]
#print(hash(f1) # error ---> list is non constant or mutable datatype
      
#a = 9
#b = 90
#print(id(a))
#print(id(b))




# ! ----> operators
# operators are sybols which is used to perform various operation
 # between 2 or more operands
#assignment
 #logical
#relational or comparison
#bitwise
#identification
#membership


 # todo ---> Arithemetic  ---> +,-,*,/,%,//,**

      #Eg : 1
      #a=8
      #b=6
      #c=9
      #print(a+b+c)
      
# input()---> used to get the runtime input
# eval() --> used to get the runtime values of all datatype
#n1 = eval(input("enter the value:"))
#print(type(n1))


#a = 4
#b = 2
#print(a/b) # is used to get the quotient value
#print(a%b) # is used to get the remainder value


# ! //---> floor devision


#a= 765433
#b= 19
#print(a/b) # -> the output will be in integer & the output will be 
#based on floor value

#!**--> used for power of a number
# print(2**4)  # --> 16


# assignment ---> +-=,-=,/=,*=,//=,**=,&=,|=,%=
#a=8
#a+=2
#print(a)




# ! comaparison --> ==, < ,!=,,=,>=
#a=8
#b=5
#print(a==b)



# ! Bitwise operator --> &,|,^,~,<<,>>

#a=7
#b=4
#print(ab)
# and
# A B A&B



#2^4 2^3 2^2 2^1 2^0
# 8   4   2    1



# 0 1 1 1 # --> 7
# 0 1 1 0 # --> 6
#-------------------
# 0 1 1 1




 #   ~---->
 # a = 9864
 # print(~a)




 #a= 9

 # 128 64 16 32 16 8 4 2 1
 # 0    0  0  0  0 1 0 0 1 # -->  9

 #1     1  1  1  1 0 1 1 0--->10


 # 1 1 1 1 0 1 0 1 -->1ST COMPLIMENT of 10
 #             # 1 -->2s compliment
 # ----------------------
 #1 1 1 1 0 1 1 0--> -10



'''
 LEFT SHIFT AND RIGHT SHIFT OPERATORES #<<,>>

'''
 # 256 128 64 32 16 8 4 2 1
 #  0   0   0  0  0 0 1 0 1   3<
 #  0   0   0  1  0 1 0 0 0   -->40
 
 # 107


 # <<,>>
 # print(5>>1)
 # 16 > 4


 # ! logical --> used to compare the expressions

 # and, or ,not
 # a=6
 # print(a>3 and a<10)
 #print(a>7 or a<30)
 #print(not(a>8 and a<10))



 # identity  operator
 #it is used to compare the memory location that the values is ,is not 
 # is, is not
 #a=8
 #b=8
 # print(a is b)
 # print(a==b)


# a= [1,2,3]
# b= [1,2,3]
# print(a is  not b)


'''
     MEMBERSHIP OPERATOR
'''

 # in, not in


 # l1 = [7,8,9,0,6,5]
 # num  = 55
 # print(num in l1)
 # print (num not in l1)


 # num = 678
 # print ( 8 in num ) # error



'''
     conditional statement
'''

 # if, elif, else


 # Eg :1
 # if (condition){
 #     statement
 #     statement
 #     statement
 # statement

 # eg: a=6
 #if a :
 #   print(hello)

 # eg : 2

# a=6
# if a>3:
#    print("hey)
#else:
#    print("no")

    # eg :3

#if 7>8:
#      print("hello")

# print("no")

   # eg :4
# a=0
# a=none
# a=false
# a=""
# if a:
#     print("yes")
#else:
#    print("no")


'''
 a number is even or odd

n = int(input("enter the number:"))
if n %2==0:
     print(n, "is even")
else:
     print(n, "is odd")
'''
# name,age,natinality
# 18 above , indian
'''
age=int(input("enter the age:"))
name=input("enter the name:")
nationality=input("enter the nationality:")
if age>18 and nationality=="india":
    print("he is eligible for vote:")
'''

 







      





















