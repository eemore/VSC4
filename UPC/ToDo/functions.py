import time

def get_user_input(prompt_message, message_for_blank='', strip_lower=False):
    print(f"Today is {time.strftime('%b %d, %Y %H:%M:%S')}")
    uc=input(prompt_message+': ')
    if uc=='' and message_for_blank != '':
        print(message_for_blank)
    if strip_lower:
        uc=uc.strip().lower()
    return uc

def todo_edit(todos2, index):
    #get the input
    itemedit=False
    todo=get_user_input("enter replacement for '"+ todos2[index-1].strip("\n")+"'",\
                    'Blank Item not stored', False)
    if todo != '':
        todos2[index-1]=todo+'\n'
        itemedit = True
        print("Item Edited!")
    return itemedit

def todo_add(todos2, todo):
    #get the input
    itemedit=False
    if todo != '':
        todos2.append(todo)
        itemedit = True
        print("Item Added!")
    return itemedit