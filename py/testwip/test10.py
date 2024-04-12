import webbrowser

user_input = input("Enter a serach term: ").replace(" ","+")

webbrowser.open("https://google.com/search?q=" +user_input)