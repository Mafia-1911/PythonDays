# myList = ['a', 'b','c']             
# myList.__setitem__(0,'z')             myList[2]='z'
# print(myList)                         print(myList)


# ranking = ['John', 'Sen', 'Lisa']
# # input the rank number 
# index= int(input("Enter which position you would wanna see: "))
# if index<=3:
#     print(ranking[index-1])
# else:
#     print("Sir we didnt rank them ")
    

# the enumerate function gives you access to both index and items 
array= [7,4,3,24,5]
for index,list in enumerate(array):
    print(f"{index}{list}")
