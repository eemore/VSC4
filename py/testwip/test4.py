import sys, csv, glob, webbrowser
#import pyautogui
#import os

if len(sys.argv)==0:
    upassword=input("Enter New Password:")
    #upassword= pyautogui.password(text='', title='Get Password', default='', mask='*')
else:
    upassword=sys.argv[1]



#1. longer than 8
#2. has a digit
#3. has at least one uppercase character
hasDigit=False
hasUpper=False
if len(upassword)>= 8:
    for i in upassword:
        if not hasDigit and i.isdigit():
            hasDigit = True
        if not hasUpper and i.isupper():
            hasUpper = True
        if hasUpper and hasDigit:
            break
#print(upassword)
if hasDigit and hasUpper:
    print("Password is Valid")
else:
    print("Password is Invalid")