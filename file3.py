# eg : 3


# Take values of length and breadth of a
# from user and check if it is sqare or not
'''
length=int(input())
breadth=int(input())
if length==bredth:
    print("its a sqare")
else:
    print("its not a sqare")
'''
# eg : 4

#python program to check whether the
#given integer is a multiple of both 5 and 7
'''
n=int(input("enter the value:"))
if n%5==0 and n%7==0:
    print("yes")
else:
    print("no")

'''
# eg : 5

'''
write a program to accept the cost price of a bike and display the
road tax to be paid
according to the folloawing criteria :

         cost price (in Rs)                     tax
         >100000                                15 % + discount 6%
         
         <10000                               5%

'''

'''
price=int(input("enter the price:"))
amount = 0
if price>=100000:
    dicount = price*(6/100)
    value = price-dicount
    amount=value*a(15/100)
    toatal=value+amont
else:
    tax = price*(5/100)
    total = price+tax
print("The onroad cost of bike is:",total)
'''


# -----> if elif else
# eg :1
'''
a = 7
b = 9
c = 32
if a>b and a>c:
    print("a is greater")
elif b>a and b>c:
    print("b is greater")
elif c>a and c>b:
    print("c is greater")
'''












'''
mark = int(input("enter the mark:"))
if mark>=80 and mark<=100:
    print("A")
elif mark>=60 and mark<80:
    print("B")
elif mark>=50 and mark<60:
    print("C")
elif mark>=40 and mark>50:
    print("D")
else:
    print("fail")
'''

'''
# --> short ha nd if else
# eg : 1
a=9
b=60
if a>b:
    print("A")
else:
    print("B")
'''

'''
-----> using short hand if else
 *rules
 1)statement inside the if condition have to be presen t at first
 2) elif cannot be used in short hand if else
 3) Always it have to end with else
'''
 
           
#print("A") if a<b else print("B")
# code to the check the given char is vowel or consonent

'''
char = input("Enter the value")
if char=="a" or char == 'e' char =='i' or char =='0'0r char =='u':
    print("is a vowel")
else:
    print("its consonent")
'''    

#        or

'''

str1 = "aeiouAEIOU"
if char in str1:
   print("vowel")
else:
    print("consonent")
     
'''



'''
# shorthand if else
char = input("Enter the char:")
str1 = "aeiouAEIOU"
print("vowels") if char in str1 else parint("constant")

'''


'''
# ---> elif ladder using short hand if else
#Eg: 1
# find greatest among 3 variables using short hand if else
a=8
b=5
c=9
print("A is grater") if a>b and a>c else print("B is grater") if b>a and b>c else print("C is the grater")
'''


#  -----> looping
# looping can be implimented using
# for loop
# while loop


#---> FOR loop
#for loop is used for iteration, if we know the number of items the loop have to run
#It is used to iterate the iterable eg(string,list,tuple, etc...)


# todo ---> syntax for loop


# for syntax in c
# for(i=0;i<10;i++){
      #printf("hello");
#}


# for syntax in python
#for userdefined_variable in range(start, end, step): default step value is 1
#     statement
#     statement
#     statement



  # eg : 1
# To print the value from 1 to 10 using for loop


#for i in range(0,10): #(n, n-1)
    # print(i)
#    print("hello")

'''
   #eg :2
for val in range(1,15,2):
    print(val)
'''

#for val in range(1,15,3):
#    print(val)


 # eg : 3
'''
to decrement the value
'''

#for val in range(10,0,-1):
#   print(val)

#for val in range(10,0,-1):
#   print(val)


#for val in range(10,0,1):
#    print(val) # no out put


'''
   eg:4
'''
# print the output of 7th multiplication table from 21 to 43
'''
for val in range(1,10+1):
    print(val*7)
'''


#for val in range(0,10+1):
 #   print("the value is ", val*7)

# method :1
'''
for val in range(1, 10+1,):
    print('7','x', val, '=',val*7)
'''

# method :2
'''
    ans="7 x {} = {}"
    print(ans.format(val,val*7))
'''
 # mewthod :3
'''
    print(f"7 x {val}={val*7}")
'''


#  eg: 5
# break ---> used to iteration the loop
'''
for val in range(1, 10):
    if val ==6:             (# here the values are print  become up to 5)
        brake
    print(val)    
'''
   # eg: 6
'''
for val in range(1, 10):
     print(val)
     if val ==6:
        brake
'''


    # eg  : 7

'''
for val in range(1, 10):
    if val ==6:
         print(val)    (# here only the print become "6")
         break
'''



   # continue statement:

   # eg: 1
'''   
for val in range(1,10):
    if val ==6:
        continue
    print(val)        #( here  skipped the vlaue 6)
'''


  # practise problems :
  # print the even number between 20 to 40



   #  even numbers 
'''
for val in range(20,40):
    if val %2==0:            (here will come even numbers )
       print(val)

'''
   # odd numbers
'''
for val in range(20,40):
    if val %2!=0:
       print(val)          ( here willl come odd numbers ) 
'''



   # ----> while loop

 # while loop id is used when we do not know the number of times the loop have to run
 # to literate the non literable elements while loop is used




 # todo syntax



 # initialisation
 # while condition
 #  statement
 #  incre or decre



 # eg: 1

# to literate number from 1 to 10

'''
i = 0
while i<11:
    print(i)
    i=i+1 # or I+=1
'''
     # eg : 2
# to decrement using while loop
'''
i = 10
while i>0:
    print(i)
    i-=1
'''
     

# for loop pracisee
# write a program to display sum of odd numbers and even
#numbers that fall between
# 12 and 37 ( including both numbers)

    
    
    






# ---> Assesment
# 1.) cats and mouse:Hacker rank
'''
def catAndMouse(x, y, z):
    dist_cat_a = abs(z - x)
    dist_cat_b = abs(z - y)
    
    if dist_cat_a < dist_cat_b:
        return "Cat A"
    elif dist_cat_b < dist_cat_a:
        return "Cat B"
    else:
        return "Mouse C"

q = int(input().strip())

for _ in range(q):
    x, y, z = map(int, input().strip().split())
    result = catAndMouse(x, y, z)
    print(result)


'''
# 2.) Print the factorla of 8 using for loop
'''
# Initialize the factorial variable to 1
factorial = 1

# Calculate the factorial of 8 using a for loop
for i in range(1, 9):
    factorial *= i

# Print the factorial of 8
print("Factorial of 8 is:", factorial)
'''
# 3.) Write a program to display sum of odd numbers and even 
# numbers that fall between
# 12 and 37(including both numbers)
'''
sum_odd = 0
sum_even = 0

# Loop through numbers from 12 to 37
for num in range(12, 37):
    if num % 2 == 0:  # Check if the number is even
        sum_even += num
    else:
        sum_odd += num

# Display the sum of odd and even numbers
print("Sum of odd numbers between 12 and 37:", sum_odd)
print("Sum of even numbers between 12 and 37:", sum_even)

'''
# 4.) Write code to print the sum of number using while loop
# n1 = 123 --> 1+2+3 = 6
'''
# Input number
n1 = 123

# Initialize variables
sum_digits = 0

# Calculate sum of digits using while loop
while n1 > 0:
    digit = n1 % 10
    sum_digits += digit
    n1 = n1 // 10

# Display the sum of digits
print("Sum of digits of the number:", sum_digits)
'''
# 5.) Prine th reverse of given number --> n1= 234 o/p --> 432
# Function to reverse a number
'''

# Function to reverse a number
def reverse_number(num):
    reverse_num = 0
    while num > 0:
        remainder = num % 10
        reverse_num = (reverse_num * 10) + remainder
        num = num // 10
    return reverse_num

# Input number
n1 = 234

# Calculate and print the reverse of the input number
reverse_n1 = reverse_number(n1)
print("Reverse of", n1, "is:", reverse_n1)

'''















 

    

    
        
      
          

          

