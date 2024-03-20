#print("Enter a todo:")
filename='files/todo.txt'
file=open(filename,'r')
todos = file.readlines()
file.close()


while True:
    user_choice = input("Enter add, show, edit, save or exit:")
    user_choice = user_choice.strip().lower()

    match(user_choice):
        case 'add'| '':
            todo = input("Enter a todo:")+'\n'
            todos.append(todo)
        case 'show' | 'display':
            #print(todos)
            for index, item in enumerate(todos):
                print(f'{index+1}.{item.replace("\n","")}')
        case 'edit':
            n=int(input("Item number to Edit. 0 to exit: "))
            if n==0:
                break
            if n > len(todos):
                print('Invalid Number Entered')  
            else:              
                todo=input("enter replacement for '"+ todos[n-1]+"': ")
                todos[n-1]=todo
        case 'save':
            file=open(filename,'w')
            file.writelines(todos)
            file.close()
        case 'exit':
            break
        case _:
            print("Hey you entered an unknown command")
    


print("Bye")

