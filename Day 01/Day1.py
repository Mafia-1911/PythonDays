# star='*'
# x=-1
# max=6
# while x<=max :
#     x=x+1
#     print(star*max)

# You dont need to google always 
# print(dir([]))
# print(help(str.rfind))

# Giving our program the power to think match/case
while True:
    dataBase=[]
    match(input('Please Enter either to show or add')):
        case 'show' :
            print(dataBase)
            break
        case 'add':
            tempData=input('what do you want to add')
            dataBase.append(tempData)
            print('you can check now ')
        case 'remove':
            dataBase.pop()
            
            

            
            
            
            
            
            
            
            
            
