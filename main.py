# create a gboard dictionary interactively
# code will be compatible to <python3.6 if f prefixes are replaced with some conventional formatting methods

from zipfile import ZipFile
import os,datetime

def getpath(system):
    print("Enter directory path for the program operations ")
    if system=="nt":path="c:\\gboard_shortcuts";print(f"(default is {path} )")
    else:
        path = os.path.join(os.environ['HOME'],"gboard_shortcuts")
        if "/data"==path[0:5]: # for android (in android , the lowest possible directory an app can access is /data/data/<data partiton of that app> without root access )
            path="/storage/emulated/0/gboard_shortcuts"
        print(f"(default is {path} )")
    try:
        if system=='posix':print(f"The home directory on your system is {os.environ['HOME']} ")
        input_path=input("Enter path : ")
        if not os.path.exists(input_path):raise Exception
        return input_path
    except:
        #if not default():print("invalid path : try again ! ");path(os.name,default=False)
        print(f"path doesnt exist (or something invalid entered ....)\n choosing directory as {path}")
        try:os.makedirs(path)
        except:pass
        return path

def path_eval(directory):
    file_paths = []
    for root, directories, files in os.walk(directory):
        for filename in files:file_paths.append(os.path.join(root, filename))
    return file_paths

def zipper(path,filename):
    zip_name=filename[0:-4]+".zip"
    file_path=os.path.join(path,zip_name)
    with ZipFile(file_path,"w") as zip:
        for i in path_eval(path):
            if os.path.basename(i) == os.path.basename(filename) : zip.write(i, os.path.basename(i));zip.close()
        return os.path.join(path,filename[0:-4]+".zip")

def shortcut_maker(status):
    if status=="new":shortcuts = ["# Gboard Dictionary version:1\n"]
    else:shortcuts=[]
    count=0
    while True:
        word = input("enter word/symbol : ");count+=1
        if word == "": return shortcuts
        shortcuts += [input("enter shortcut : ")+"\t"+word+ "\t\n"]
        print(f"successfully entered {count} shortcuts \n")
        print('hit enter on "word" inputs to stop entering and save the gboard importable zip \n')
        
def filename_generator(path,os_name):
        if os_name=="nt":
            return str(path+"\shortcuts-"+datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")+".txt")
        else:
            return str(os.path.join(path,"shortcuts-"+datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")+".txt"))
        
def dict_create(path,status,file=None,is_from_zip=None):
    file_name=filename_generator(path,os.name)
    if status=="new":
        dict_txt=open(file_name,"w")
    else:
        file_name=file
        dict_txt=open(file,"a+")
        dict_txt.seek(0)
        print(dict_txt.read())
        print("\nReady to add more shortcuts : \n")
    shortcuts=shortcut_maker(status)
    dict_txt.writelines(shortcuts);dict_txt.close()
    if is_from_zip==True:path = zipper(path,os.path.join(path,file))
    if is_from_zip!=True:path = zipper(path,os.path.join(path,file_name))
    print(f"success! saved file as {os.path.basename(path)} dictionary file in {os.path.dirname(path)} ")
    
def dict_add(path,file=None):
    if file==None:
        print("hey")
        print(f"reading files from {path} . . . . .")
        #os.path.isfile
        print("Choose the file where more shortcuts are to be added :\n");count=0
        files=[i for i in path_eval(path) if (i[-4:]==".txt" or i[-4:]==".zip")]
        for i in files:
            if os.path.isfile(i):
                print(count+1,". ",os.path.basename(i));count+=1
        print("Enter here (S.No. number of the file) (skip to choose a different directory) ")
        choice=input("Enter here : ")
        if choice=='':path=getpath(os.name);dict_create(path,None)
        dict_add(path,files[int(choice)-1])
    else:
        if file[-4:]==".txt":
            dict_create(path,"add",file)
        else:
            with ZipFile(file, 'r') as zip:
                data_list=zip.namelist()
                if len(data_list)==1 and data_list[0][-4:]==".txt":
                    zip.extractall(path);zip.close()
                    dict_create(path,"add",os.path.join(path,data_list[0]),is_from_zip=None)
    print("\nCreated updated files with No errors ! ")

                    

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
 
# Next build would contain logger replacing some prompts .... 

