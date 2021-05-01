# create a gboard dictionary interactively
# code will be compatible to <python3.6 if f prefixes are replaced with some conventional formatting methods

from zipfile import ZipFile
import os,datetime

def path(system):
    #give one more parameter to make sure that the default path is to be taken or not
    print("Enter directory path for the program operations ")
    if system=="nt":
        path="c:\\gboard_shortcuts"
        print(f"(default is {path} )")
    else: #for non-nt (posix ; macos not included)"
        path = os.path.join(os.environ['HOME'],"gboard_shortcuts")
        print(path[0:4])
        if "/data" in path[0:5]: #if android
            path="/storage/emulated/0/gboard_shortcuts"
        print(f"(default is {path} )")
    try:
        input_path = input("Enter here : ")
        if not os.path.exists(input_path):raise Exception
        path=input_path
        return path
    except:
        #if not default():print("invalid path : try again ! ");path(os.name,default=False)
        print(f"invalid path ....\n choosing directory as {path}")
        try:os.makedirs(path)
        except:pass
        return path,system

def path_eval(directory):
    file_paths = []
    for root, directories, files in os.walk(directory):
        for filename in files:file_paths.append(os.path.join(root, filename))
    return file_paths

def zipper(path,filename,status):
    if status.lower()=="new":mode="w"
    #elif status.lower()=="add":mode="a"
    file_path=os.path.join(path,f"{filename[0:-4]}.zip")
    with ZipFile(file_path,mode) as zip:
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
        if path[1]=="nt":
            file_name=path[0]+"\shortcuts-"+datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")+".txt"
        else:
            file_name=os.path.join(path[0],"\shortcuts-"+datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")+".txt")
        dict_txt=open(file_name,"w")
        ###############################################################################################################
############################################################
#    if status.lower()=="add":
#        print(f"reading files from {path} . . . . .")
#        #os.path.isfile
#        print("Choose the shortcut file to be edited : ");count=0
#        files=path_eval(path)
#        for i in files:
#            if os.path.isfile(i):
#                print(count+1,". ",os.path.basename(i);count+=1
#        print("Enter here (S.No. number of the file) (skip to choose a different directory) ")
#        choice=int(input("Enter here : "))
#        if choice=='':path=path(os.name);
#        
        ###############################################################################################################
    dict_txt.writelines(shortcuts);dict_txt.close()
    path = zipper(path[0],os.path.basename(file_name),status)
    print(f"success! saved file as {os.path.basename(path)} dictionary file in {os.path.dirname(path)} ")




choices = {"New": "to create a new gboard dictionary", "Add": "to add more shortcuts into existing dictionary ",
               "Exit": "to exit"}
while True:
    print()
    for i in choices: print(f"enter '{i}' {choices[i]}")
    choice = input("Enter : ")
    system=os.name
    if choice.lower() in ["new","add"]:
        store_path=path(system)
        if choice.lower()=="add":print("This feature will be added soon (preferrably in the next release) ")
        else:dict_create(store_path, shortcut_maker(choice), choice)
    elif choice.lower() == "exit":print("Thank you for using the program \n Exiting...... ");break
    else:print("invalid option : please try again ");continue

