import pyautogui
#print("Enter a todo:")
#filename='./files/todo.txt'
filename=r'c:\Users\emoree\Downloads\PD\VSC4\UPC\ToDo\files/todo.txt'
#file=open(filename,'r')
#todos = file.readlines()
#file.close()

def get_user_input(prompt_message, message_for_blank='', strip_lower=False):
    uc=input(prompt_message+': ')
    if uc=='' and message_for_blank != '':
        print(message_for_blank)
    if strip_lower:
        uc=uc.strip().lower()
    return uc

def edit_todo(todos2, index):
    #get the input
    itemedit=False
    todo=get_user_input("enter replacement for '"+ todos2[index-1].strip("\n")+"'",\
                    'Blank Item not stored', False)
    if todo != '':
        todos2[index-1]=todo+'\n'
        itemedit = True
    return itemedit

with open(filename,'r') as file:
    todos = file.readlines()

ListIsEdited = False

while True:
    user_choice = get_user_input("Enter add, show, edit, delete, save or exit:","Blank ToDo not Stored", True)
    #user_choice = user_choice.strip().lower()

    match(user_choice):
        case 'add':
            todo = get_user_input("Enter a todo:",'Blank Item not stored', False)
            if todo != '':
                todos.append(todo+'\n')
                ListIsEdited=True
        case 'show' | 'display' | '':
            #print(todos)
            for index, item in enumerate(todos):
                print(f'{index+1}.{item.strip("\n")}')
        case 'edit' | 'delete':
            n=int(input(f"Item number to {user_choice}. 0 to return to options: "))
            if n==0:
                pass #n=2# break do nothing
            elif n > len(todos):
                print('Invalid Number Entered')  
            else:  
                if user_choice == 'edit':  
                    ListIsEdited=edit_todo(todos, n)          
                else:
                    todos.pop(n-1)
                    ListIsEdited=True                
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
                    ListIsEdited=edit_todo(todos, n)
                else:
                    print('Invalid Number Entered')
            else:
                print("Hey you entered an unknown command")
    


print("Bye")

