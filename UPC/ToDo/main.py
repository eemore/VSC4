import pyautogui
from functions import *
#import functions #then we use functions.xxx

#print("Enter a todo:")
#filename='./files/todo.txt'
filename=r'c:\Users\emoree\Downloads\PD\VSC4\UPC\ToDo\files/todo.txt'
#file=open(filename,'r')
#todos = file.readlines()
#file.close()


with open(filename,'r') as file:
    todos = file.readlines()

ListIsEdited = False

while True:
    user_choice = get_user_input("Enter add, show, edit, delete, save or exit:","", True)
    #user_choice = user_choice.strip().lower()
    uccommands = user_choice.split()
    no_of_commands = len(uccommands)
    if no_of_commands==0:
        pass
    else:
        user_choice = uccommands[0]
        uccommands.pop(0)
        todo = " ".join(uccommands)


    match(user_choice):
        case 'add' | 'new':
            if no_of_commands==1:
                todo = get_user_input("Enter a todo:",'Blank Item not stored', False)                
            else:
                pass
                #n=1
                #while n< no_of_commands:
                #    #print(n,no_of_commands,uccommands)
                #    todo_add(todos, uccommands[n])
                #    n += 1
                #ListIsEdited=True
            ListIsEdited = todo_add(todos, todo)
        case 'show' | 'display' | '':
            #print(todos)
            for index, item in enumerate(todos):
                print(f'{index+1}.{item.strip("\n")}')
        case 'edit' | 'delete':
            if no_of_commands==1:
                ui=input(f"Item number to {user_choice}. 0 to return to options: ")
            else:
                if todo.isdigit():
                    n=int(todo)
                    if n<0 or n > len(todos):
                        print('Invalid Number Entered')
                        continue
                    else:
                        ui=todo
                else:
                    print("Invalid Number format")                        
                    continue
            if ui=="":
                n=0
            elif not ui.isdigit():
                print('Invalid Number Entered')
            else:
                n=int(ui)
            if n==0:
                pass #n=2# break do nothing
            elif n > len(todos):
                print('Invalid Number Entered')  
            else:  
                if user_choice == 'edit':  
                    ListIsEdited=todo_edit(todos, n)          
                else:
                    #print("before pop of delete")
                    todos.pop(n-1)
                    ListIsEdited=True   
                    print('Item Deleted')             
        case 'save':
            with open(filename,'w') as file:
                file.writelines(todos)
            print('Todo List Saved!')
            ListIsEdited=False
        case 'exit':
            if ListIsEdited and \
                input('List Has Been Changed. Enter OK to Exit Without Saving: ').strip().lower() == "ok":
                ListIsEdited = False
            if not ListIsEdited:
                break
        case _:            
            if user_choice.isdigit():
                n = int(user_choice)
                if n > 0 and n <= len(todos):
                    print(f'switching to editing {n}')
                    ListIsEdited=todo_edit(todos, n)
                else:
                    print('Invalid Number Entered')
            else:
                print("Hey you entered an unknown command")
    


print("Bye")

