#print("Enter a todo:")


todos = []
while True:
    user_choice = input("Enter add, show or exit:")
    match(user_choice):
        case 'add':
            todo = input("Enter a todo:")
            todos.append(todo)
        case 'show':
            #print(todos)
            for item in todos:
                print(item)
        case 'exit':
            break

print("Bye")

