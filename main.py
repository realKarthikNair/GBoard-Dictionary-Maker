# create a gboard dictionary interactively
# code will be compatible to <python3.6 if f prefixes are replaced with some conventional formatting methods

from zipfile import ZipFile
import os,datetime

def path():
    print("Enter directory path where the file is to be stored. ")
    print("(default is C:\\gboard_shortcuts )")
    try:
        path = input("Enter here : ")
        if not os.path.exists(path):raise Exception
        return path
    except:
        path = "C:\\gboard_shortcuts"
        print(f"input path doesnt exist.... \n choosing directory as {path}")
        try:os.makedirs(path)
        except:pass
        return path

def path_eval(directory):
    file_paths = []
    for root, directories, files in os.walk(directory):
        for filename in files:file_paths.append(os.path.join(root, filename))
    return file_paths

def zipper(path,filename,status):
    if status.lower()=="new":mode="w"
    #elif status.lower()=="add":mode="a"
    with ZipFile(f'{path}\\{filename[0:-4]}.zip',mode) as zip:
        for i in path_eval(path):
            if os.path.basename(i) == filename : zip.write(i, os.path.basename(i))
        return path+'\\'+filename[0:-4]+".zip"

def shortcut_maker(status):
    if status.lower()=="new":shortcuts = ["# Gboard Dictionary version:1\n"]
    else:shortcuts=[]
    count=0
    while True:
        word = input("enter word/symbol : ");count+=1
        if word == "": return shortcuts
        shortcuts += [input("enter shortcut : ")+"\t"+word+ "\t\n"]
        print(f"successfully entered {count} shortcuts \n")
        print('hit enter on "word" inputs to stop entering and save the gboard importable zip \n')

def dict_create(path,shortcuts,status):
    if status.lower()=="new":
        file_name=path+"\shortcuts-"+datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")+".txt"
        dict_txt=open(file_name,"w")
    #if status.lower()=="add":
        #print("Choose the shortcut file to be edited : ");count=0
        #files=path_eval(path)
        #for i in files:
            #print(count,". ",os.path.basename(file_name));count+=1
        #choice=int(input("Enter here (S.No. number of the file) : "))
        #dict_txt=open(files[count],"a")
    dict_txt.writelines(shortcuts);dict_txt.close()
    path = zipper(path,os.path.basename(file_name),status) #
    print(f"success! saved file as {os.path.basename(path)} dictionary file in {os.path.dirname(path)} ")



choices = {"New": "to create a new gboard dictionary", "Add": "to add more shortcuts into existing dictionary ",
               "Exit": "to exit"}
while True:
    print()
    for i in choices: print(f"enter '{i}' {choices[i]}")
    choice = input("Enter : ")
    if choice.lower() in ["new","add"]:
        if choice.lower()=="add":print("This feature will be added in the next release. ")
        else:dict_create(path(), shortcut_maker(choice), choice)
    elif choice.lower() == "exit":print("Thank you for using the program \n Exiting...... ");break
    else:print("invalid option : please try again ");continue

