# python -m pip install pyautogui
#pip install openpyxl
# Examples:
#pyautogui.alert('Just a notification', "Title")  # always returns "OK"
#pyautogui.confirm('Asks OK or Cancel')  # returns "OK" or "Cancel"
#mys=pyautogui.prompt('Asks for a string from user')  # returns string or None
#myp=pyautogui.password('Enter password')  # returns string or None

# Method signatures:
#   alert(text='', title='', button='OK')
#   confirm(text='', title='', buttons=['OK', 'Cancel'])
#   prompt(text='', title='' , default='')
#   password(text='', title='', default='', mask='*')

import pyautogui
# import OS module
import os 

# Get the list of all files and directories
path = "C://Users//emoree//Downloads//PD//Efe WIP//Charter"
#path = pyautogui.prompt('Enter Path', 'Title of Dialog Box' , path)
#path = input(r"Enter the path of the folder: ")
dir_list = os.listdir(path)
#print("Files and directories in '"+path+ "' :")
# prints all files
#print(dir_list)
#print(path)
# import OS module

# This is my path
#path = "C://Users//Vanshi//Desktop//gfg"

# to store files in a list
#list = []

#for file in dir_list:
#    print(file)
# dirs=directories
count=0
import os 
from os.path import join, getsize 
for root, dirs, files in os.walk(path): #for (root, dirs, file) in os.walk(path):
    print(root, "consumes ") 
    #print(sum(getsize(join(root, name))    
    for names in files:
        print(names) 
        if 'CVS' in dirs: dirs.remove('CVS') # don't visit CVS directories    
    
#count=count+1 
#for f in file:
#    if '.txt' in f:
#        print(f)

#print(count)


