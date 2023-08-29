import math
size="s" #s,m,l
add_pepparoni=True
extra_cheese=True

total_bill=0;
small_price=15;medium_price=20;large_price=25;
peparroni_small=2;peparroni_others=3;

if size=="s":
    total_bill==small_price
if size=="m":
    total_bill=medium_price
if size=="l":
    total_bill=large_price    
    
if add_pepparoni and size=='s':
    total_bill=total_bill+peparroni_small;
else:
    total_bill+=peparroni_others


#/////Functions
def greet(name):
    print(f"hello there {name}")    
greet("Nushan")
#////////Making a calculator 
# def subtract(x,y):
#     print(x-y)
def multiply(x,y):
     print(x*y)
# def division(x,y):
#     print(x/y)
# def add(x,y):
#     print(x+y)
# user_num1=4;
# user_num2=7;
# user_operation="7"
# if user_operation=="+":
#     add(user_num1,user_num2)
# elif user_operation=="-":
#     subtract(user_num1,user_num2)
# elif user_operation=="*":
#     multiply(user_num1,user_num2)
# elif user_operation=="/"
#     division(user_num1,user_num2)
# else:
#     print("Give a valid Operation")
    
    
    
#//////Paint wall problem
# test_h=45;
# test_w=32;
# coverage=5


def paint_calc(test_h,test_w,coverage):
    numberOfCans=test_h*test_w/coverage;
    print(math.ceil(numberOfCans));
    
#paint_calc(2,4,5) 
#paint_calc(2,4,5) 
def listsAsArgument(list):
    print(list)

listsAsArgument([2,3,4,5,6,7])
 #///////Building our own List methods 
 
def list_sum(list):#[2,6,9]
    sum=0;
    for i in list:
        sum += i;
    print(sum)
list_sum([3,4,5,7])

def list_min(list):
    minV=999;
    for i in list:
        if i<minV:
            minV=i;
    print(minV)
list_min([4,5,6,7,8,1])
    
def list_max(list):
    maxV=0;
    for i in list:
        if i>maxV:
            maxV=i
    print(maxV)
list_max([3,4,5,99,32])
    
#////Leap Year or not 
def isLeapYear(year):
    if year%4==0:
        if year%100 != 0:
            if year%400 == 0:
                print("Leap Year")
            else:
                print("Not a leap Year")
        else: 
            print("Leap Year")
    else:
        print("Not a leap year ")
            
    #first check if divisible by 4 and 400 
    
    if year%400 == 0:
        if year%4==0 and year%100!=0:
            print("Its a leap year ")
        else:
            print("Its not a leap year")

def nameFormat(name):
    return [name.title()]

#/////Dictionary 
user1090={
    "email":"mushtasin.ahmed11@gmail.com",
    "password":(hashVal="siqu392842cew"),
}

#we can create instances from object but not from dictionaries 
