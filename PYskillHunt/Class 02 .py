#print even numbers
# number=20
# for i in range(2,number+1,2):
#     print(i);
    
# i=0
# while(i<=100):
#     i+=1;
#     print(i)

#check number is even or not 
# i=1;
# while(i<100):
#     i +=1 ;
# print(i+1);

# we shall use for loop if the range is given 
# we shall use while loop if the condition is given 

#////////////   FizzBuzz
input=20;

# for j in range(0,input):
#     if j%3==0 and j%5==0:
#         print("Fizz Buzz")
#     elif(j%3==0):
#         print("Fizz")
#     elif(j%5==0):
#         print("Buzz")
#     else:
#         print(j);

# i=1;
# while(i<=input):
#     if(i%3==0 and i%5==0):
#         print("Fizz Buzz")
#     elif i%3==0:
#         print("fizz")
#     elif i%5==0:
#         print("Buzz")
#     else:
#         print(i)
#     i+=1;

import random
#print(random.randint(1,2))
#print(random.randrange(0,70,5))
# diceRoll=random.randint(1,6)
# if diceRoll==6:
    #print("Chokkha")
#print(diceRoll)

#///lists 
#/////// find the average 
nlist=[1,2,4,6,9,10]
        #counting the number of elements 
count=0;
for i in nlist: #number of iterations is the length of array
    count+=1
#print(count)
        #finding the sum 
sum=0;
for i in nlist:
    sum=sum+i;
average=sum/count
#print(average)    

#///////Finding the maximum-minimumm among the list 
# marks=[222,30,45,50,75,3,23,59,5]
# maximum=0;
# for i in marks:
#     if i>maximum:
#         maximum=i
# print(maximum)

# minimum=marks[-1];#for minimum take a value greater than the values of array or take the last element as the minimum  

# for i in marks:
#     if i<minimum:
#         minimum=i
# print(minimum)
    
    
#Append, POP , Remove
newArr=[2,3,4,5,"a",6]
newArr.remove("a")
#print(newArr)
    
#///////Password Generator 

# take number of letters,numbers ,symbols 
#input - 3,4,1  output- s/s/s2313
list_of_char=["a","b","c","d","e","f","g","h","i","j"]
list_of_symbols=['/',']',"|","{","*"]
list_of_numbers=[1,2,3,4,5,6,7,8,9,10]
import random

no_of_char=4;
no_of_symbols=7;
no_of_numbers=5;
final_char=[]
final_num=[]
final_symbol=[];
for i in range(0,no_of_char):
    final_char.append(random.choice(list_of_char))
print(final_char)
for i in range(0,no_of_numbers):
    final_num.append(random.choice(list_of_numbers))
print(final_num)
for i in range(0,no_of_symbols):
    final_symbol.append(random.choice(list_of_symbols))
print(final_symbol)
password=final_symbol+final_char+final_num
print(password)
#getting rid of the list 
for i in password:
    print(i,end="")#prints in the same line 
    
#///////Who pays the bill 
#taking input and keeping them in list 
#randomly pick one from the list 

# new_list=input("Please enter the names").split(', ')
# print(new_list)
# x=random.choice(new_list)


#///////Rock pape Scissor 
# user gives a input , computer give another then compare it to win
# o=rock 1=paper 2=scissor 
# user_move=0
# coputer_move=random.randint(0,2)
# rock paper scissor 
# if user_move<computer_move:
#     print('User won')
# elif 

    
