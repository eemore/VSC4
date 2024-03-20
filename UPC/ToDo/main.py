#print("Enter a todo:")
filename='./files/todo.txt'
#file=open(filename,'r')
#todos = file.readlines()
#file.close()

with open(filename,'r') as file:
    todos = file.readlines()

while True:
    user_choice = input("Enter add, show, edit, delete, save or exit:")
    user_choice = user_choice.strip().lower()

    match(user_choice):
        case 'add'| '':
            todo = input("Enter a todo:")+'\n'
            todos.append(todo)
        case 'show' | 'display':
            #print(todos)
            for index, item in enumerate(todos):
                print(f'{index+1}.{item.strip("\n")}')
        case 'edit' | 'delete':
            n=int(input(f"Item number to {user_choice}. 0 to exit: "))
            if n==0:
                break
            if n > len(todos):
                print('Invalid Number Entered')  
            else:  
                if user_choice == 'edit':            
                    todo=input("enter replacement for '"+ todos[n-1].strip("\n")+"': ")+'\n'
                    todos[n-1]=todo
                else:
                    todos.pop(n-1)
        case 'save':
            with open(filename,'w') as file:
                file.writelines(todos)
            print('Todo List Saved!')
        case 'exit':
            break
        case _:
            print("Hey you entered an unknown command")
    


print("Bye")

