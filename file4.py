#Date : 14-03-2024


# ---> while loop
# --> breake using while loop


# eg : 1
# iterate from 20 to 30 and break the loop in 27
'''
i = 20
while i<31:
    if i ==27:
       break
    print(i)
    i+=1
'''
#
'''
i = 20
while i<31:
     print(i)
     i+=1
     if i ==27:
       break
'''
#
'''
i = 20
while i<31:
     print(i)
     if i ==27:
       break
     i+=1
''' 
#
'''
i = 20
while i<31:
     if i ==27:
        print(i) ------>here will become 27
        break
     i+=1
'''


# ------> cintinue
'''
i = 20
while i<31:
    if i ==27:
       continue
    print(i)
    i=i+1
'''


#
'''
i = 20
while i<31:
    i=i+1
    if i ==27:
       continue
    print(i)   (here  qwill become print the expt 27)
'''


#  eg  : 5
#   wwhile to iterate from 12 to 22
#   find the sum of all numbers
'''
i = 12
sum = 0
while i<23:
    sum  =sum+i
    i+=1
print(sum)

'''


# eg :6
# find the average of value from 20  to 30
'''
i = 20
sum = 0
while i<25:
    sum  = sum+i
    i+=1
print(sum/6)
'''
   
    ##
'''
i = 20
sum = 0
count = 0
while i<=30:
    sum  = sum+i
    count+=1
    i+=1
print(sum/count)

'''
   # -----> Nested for loop


   # eg : 1
'''
for i in  range (1,3+1):
    for j in range (1,4+1):
        print(i,j)
'''      
###
'''
for row in  range (1,3+1):
    for col in range (1,4+1):
        print(row,col)
'''


  #  eg : 2

'''
* * * *
* * * * 
* * * * 
* * * *
'''
'''
for row in range(4):
    for col in range(4):
        print("*", end="")
'''
###
'''
for row in range(4):
    for col in range(4):
        print("*", end="")
    print()
'''
'''
rows =int(input("enter the rows:"))
cols =int(input("enter the cols:"))
for row in range(rows):
    for col in range(cols):
          print("*", end="")
    print()
'''      
  ###
'''
    
for row in range(4):
    for col in range(4):
        print("*", end="")
    print()
'''
###


'''
sum = 0
for row in range(4):
    for col in range(4):
        sum = sum+1
        print(sum, end=" ")
    print()
        
'''

  ## TO Print stars in right angled triangle .
'''
for row in range(0,6-1):
    for col in range(0,row+1):
        print("*", end="")
    print()
'''
####
'''
for row in range(0,6):
    for col in range(row,6):
        print("*", end="")
    print()
'''
####
'''
* * * * *
*       *
*       *
*       *
* * * * *
'''
'''
for row in range(5):
    for col in range(5):
        if col==0 or col==5-1 or row == 0 or row ==5-1:
           print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''
####

'''    
           *          
         * * *
        * * * * 
       * * * * *
'''



###

'''
for row in range(0,5):
    for col in  range(0,6):
        if ((row==0 and col==3) or (row==1 and (col>=2 and col<=4)) or (row==2 and (col>=1 and col<=5))):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

'''



#### ----->List


## ----->Datatypes 
'''
* primary data type
'''
# number ---> int, float complex
# * string
# *  Boolean
# * None

'''
# collection
'''
# * list
# * tuple
# * set
# * dictionary



##  -------> LIST
  # 1) if the collection of elements arensorounded by sqare brackets, it is considersd to be list .

#   eg :

   #l1 = [4,7,9,9.89, "hello",7+9j, [8,9,0]]



#  charecterstics of list
# 1) it is have to be sorounded by []
# 2) it is mutable (the elements in the list are changeble)
# 3) evry element inside list is indexd
# 4) the elements inside list will be ordered fomat
# 5) it can hold duplicate valyues
# 6) its heterogenous




# tO ACCCES THE elments in list
l1= [1,2,3,4,4,5,5,5,5,7,5,5,6,76.8, "p", "i"]
#print(l1)
 


## -->  indexing

#in the collection data types like list ,tuple , string , the elements will be alloted
#with pre defined uniqe value caaled index value



# we have 2 types of indexing
# positive indexing --> starts with 0 from left hand side
# negative indexing ---> starts with -1 from right hand side


#   positive indexing
'''
print(l1[0])
print(l1[4])
print(l1[20])----> error
'''

##------> Negative indexing

'''
l1 = [1,4,34,64.4,54,"P", "i"]
print(l1[-1])
print(l1[-5])

'''


## -----> slicing.
#l1 = [1,4,34,64.4,54,"P", "i"]
#l1[start_index:end_index:step)
'''
print(l1[0:4])
print(l1[6:8])
print(l1[3:6])
print(l1[:5])
print(l1[3:])
print(l1[:])



print(l1[0:7:1])  # l1[0:7]----> both are same
print(l1[0:7:2])
'''
l1 = [1,4,34,64.4,54,"P", "i"]
#print(l1[-4:-1])
#print(l1[-1:-4])------> []
#print(l1[-7:-1])
#print(l1[-7:-1:2])



## to print ot add element inside list

# append()---> usedd to add elemnet at last position of list
l1 = [9,8,0,6]
l1.append("krish")
print(l1)




















