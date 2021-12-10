# create a gboard dictionary interactively
# code will be compatible to <python3.6 if f prefixes are replaced with some conventional formatting methods !

from functions import *

choices = {"New": "to create a new gboard dictionary", "Add": "to add more shortcuts into existing dictionary ",
               "Exit": "to exit"}
while True:
    print("\n")
    for i in choices: print(f"enter '{i}' {choices[i]}")
    choice = input("Enter : ").lower()
    system=os.name
    if choice in ["new","add"]:
        store_path=getpath(system)
        if choice=="new":
            dict_create(store_path,choice)
        else:dict_add(store_path,None)
    elif choice == "exit":print("Thank you for using the program \n Exiting...... ");break
    else:print("invalid option : please try again ");continue
 


