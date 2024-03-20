#print("Enter a todo:")


todos = []
while True:
    user_choice = input("Enter add, show, edit or exit:")
    user_choice = user_choice.strip().lower()

    match(user_choice):
        case 'add'| '':
            todo = input("Enter a todo:")
            todos.append(todo)
        case 'show' | 'display':
            #print(todos)
            for item in todos:
                print(item)
        case 'edit':
            n=int(input("Item number to Edit. 0 to exit: "))
            if n==0:
                break
            todo=input("enter replacement for '"+ todos[n-1]+"': ")
            todos[n-1]=todo
        case 'exit':
            break
        case _:
            print("Hey you entered an unknown command")
    


print("Bye")

