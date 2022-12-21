database = []

while True:
    tempInp=input("Please Enter your Task: ")
    finalInp=tempInp.strip()

    match tempInp:
        case 'Add':
            database.append(input)
        case 'Show':
            for item in database:
                print(item)
        case 'edit':
            #which index 
            removeIndex= float(input('Enter the index you want to edit ')) #99/0
            #what is the alternative
            newTask=input('whaat to do you want to add there: ')
            #we replace that 
            database[removeIndex]
        case 'delete':
            database.clear()
        case 'exit' :
            break

print('Thanks')
     
           

