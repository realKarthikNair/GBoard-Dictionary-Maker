# GBoard Dictionary Maker GUI

try:
    import tkinter as tk
    from tkinter import messagebox, filedialog
except:
    try:
        if os.name()=="nt":os.system("pip install tk")
        else: os.system('''x-terminal-emulator -e "sudo apt-get install python3-tk"''')
    except:
        print("Unable to install dependencies, try manually installing tkinter !")
    
import os
import datetime
from zipfile import ZipFile

os_name = os.name
words = []
shortcuts = []


def zipper(path,filename):
    zip_name=filename[0:-4]+".zip"
    file_path=os.path.join(path,zip_name)
    with ZipFile(file_path,"w") as zip:
        for i in path_eval(path):
            if os.path.basename(i) == os.path.basename(filename) : zip.write(i, os.path.basename(i));zip.close()
        success = os.path.join(path,filename[0:-4]+".zip")
        if os.path.exists("demofile.txt"):
            os.remove("demofile.txt")

def save():
    """ Saves the Word and Shortcut Entered (if user don't want to add more words) """
    global word_input, shortcut_input, words, shortcuts, path
    words.append(str(word_entry.get()))
    shortcuts.append(str(shortcut_entry.get()))
    user_choice = messagebox.askyesno('GBOARD Dictionary Maker', 'Do you want to add more words?')
    if user_choice:
        word_input.set("")
        shortcut_input.set("")
    elif not user_choice:
        with open('folder_path.txt', 'r') as file_check:
            file_contents = file_check.readline()
            path = str(file_contents)
        file_check.close()
        if os_name == "nt":
            # Windows (Generates File Name)
            path = path + "/Gboard-Shortcuts"
            file_name = str(path) + "/shortcuts-" + datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S") + ".txt"
        else:
            # Other than Windows (Generates File Name)
            file_name = os.path.join(str(path), "shortcuts-" + datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S") + ".txt")
        with open('{}'.format(file_name), 'w') as file_save:
            for i in range(0, len(words)):
                file_save.write("{}\t{}\n".format(shortcuts[i], words[i]))
        file_save.close()
        messagebox.showinfo('(!) Saving.... (!)', "Saving file..\nFile:'{}'".format(file_name))
        word_gui.destroy()
        main_gui()


def gboarddict():
    """ GUI for Entering Word and Shortcut """
    global word_gui, word_entry, shortcut_entry, word_input, shortcut_input
    word_gui = tk.Tk()
    word_gui.title('GBOARD Dictionary Maker')
    word_gui.geometry('500x500')
    word_gui.resizable(width=False, height=False)

    word_canvas = tk.Canvas(word_gui, bg='#ba8f6a', height=500, width=500)
    word_canvas.pack()

    # Heading
    heading = tk.Label(word_canvas, text="GBOARD Dictionary Maker", fg="yellow", bg="#ba8f6a",
                       font=('helvetica', 18, 'bold underline'))
    word_canvas.create_window(250, 40, window=heading)

    word_label = tk.Label(word_canvas, text="Word: -", bg="#ba8f6a", fg="black", font=('', 14))
    word_canvas.create_window(170, 150, window=word_label)
    word_input = tk.StringVar()
    word_entry = tk.Entry(word_canvas, textvariable=word_input)
    word_canvas.create_window(320, 150, window=word_entry)

    shortcut_label = tk.Label(word_canvas, text="Shortcut: -", bg="#ba8f6a", fg="black", font=('', 14))
    word_canvas.create_window(160, 220, window=shortcut_label)
    shortcut_input = tk.StringVar()
    shortcut_entry = tk.Entry(word_canvas, textvariable=shortcut_input)
    word_canvas.create_window(320, 220, window=shortcut_entry)

    # Save Button
    save_button = tk.Button(word_canvas, text='Save', bg='#3dd46a', padx=15, pady=10, command=save)
    word_canvas.create_window(250, 350, window=save_button)

    word_gui.mainloop()


def check_dir():
    """ Checks if the users entered/selected path exist or not! And if it does it creates a Folder """
    input_path = str(user_entry_box.get())
    if input_path in ["", " "]:
        if os_name == "nt":
            input_path = "c:\\"
        elif os_name == "posix":
            input_path = os.getenv("HOME")
        messagebox.showinfo('(!) Default Folder Selected (!)',
                            "The Folder has been created at:-\n'{}'".format(input_path))
        new_root.destroy()
        with open('folder_path.txt', 'w') as file:
            file.writelines("{}".format(input_path))
        file.close()
        new_path = os.path.join(input_path, 'Gboard-Shortcuts')
        os.mkdir(new_path)
        main_gui()
    else:
        if not os.path.exists(input_path):
            messagebox.showerror('(!) No Directory Exist (!)', 'No directory exist at path:\n{}'.format(input_path))
            new_root.destroy()
            new_folder()
        else:
            messagebox.showinfo('(!) Folder Created! (!)', "The Folder has been created at:-\n'{}'".format(input_path))
            new_root.destroy()
            with open('folder_path.txt', 'w') as file:
                file.writelines("{}".format(input_path))
            file.close()
            new_path = os.path.join(input_path, 'Gboard-Shortcuts')
            os.mkdir(new_path)
            main_gui()


def browse():
    folder_selected = filedialog.askdirectory()
    folder_path.set(folder_selected)


def new_folder():
    global user_entry_box, new_root, folder_path
    """ Creates a new folder """
    # Asks user to enter the path for the folder
    new_root = tk.Tk()
    new_root.title('Enter Path')
    new_root.geometry('300x100')

    new_label = tk.Label(new_root, text="Path:")
    new_label.pack()

    folder_path = tk.StringVar()
    user_entry_box = tk.Entry(new_root, textvariable=folder_path)
    user_entry_box.pack()

    browse_button = tk.Button(new_root, text="Browse", bg="lightgreen", command=browse)
    browse_button.pack()

    select_button = tk.Button(new_root, text="Select", bg="lightgreen", command=check_dir)
    select_button.pack()

    new_root.mainloop()


def check_folder(os_name):
    """ Checks if the Folder exists in the default directory """
    if os_name == 'nt':
        # Windows
        with open('folder_path.txt', 'r') as file:
            file_contents = file.readline()
        path = str(file_contents) + "/Gboard-Shortcuts"
        file.close()
        isdir = os.path.isdir(path)
        if not isdir:
            messagebox.showinfo("(!) No Folder Found (!)",
                                "No Folder Found! Enter the path to make one\nor leave it blank to save it in default path.\ndefault path = 'c:\\gboard_shortcuts'")
            gui_root.destroy()
            new_folder()
        elif isdir:
            gui_root.destroy()
            gboarddict()

    elif os_name == 'posix':
        # Linux
        path = os.getenv("HOME")
        path = str(path) + "/Gboard-Shortcuts"
        isdir = os.path.isdir(path)
        with open('folder_path.txt', 'w') as file:
            file.write("{}".format(path))
        file.close()
        if not isdir:
            messagebox.showinfo("(!) No Folder Found (!)",
                                "No Folder Found! Enter the path to make one\nor leave it blank to save it in default path.\ndefault path = '$HOME/gboard_shortcuts'")
            gui_root.destroy()
            new_folder()
        elif isdir:
            gui_root.destroy()
            gboarddict()

    else:
        # Android , the lowest possible directory an app can access is /data/data/<data partition of that app> without root access )
        path = os.path.join(os.environ['HOME'], "gboard_shortcuts")
        if "/data" == path[
                      0:5]:  # for android (in android , the lowest possible directory an app can access is /data/data/<data partition of that app> without root access )
            path = "/storage/emulated/0/gboard_shortcuts"
        print(f"(default is {path} )")


def folder_run():
    check_folder(os_name)


def add_feature():
    messagebox.showerror('(!) Does not Exist (!)', "Coming Soon.....")


def close():
    gui_root.destroy()
    exit()


def main_gui():
    global gui_root
    """ Main Menu """
    gui_root = tk.Tk()
    gui_root.title('GBOARD Dictionary Maker')
    gui_root.geometry('800x800')
    gui_root.resizable(width=False, height=False)

    gui_canvas = tk.Canvas(gui_root, bg='#3e5fc2', height=800, width=800)
    gui_canvas.pack()

    # Heading of GUI
    head = tk.Label(gui_canvas, text="G-BOARD Dictionary\nMaker", fg='white', bg="#3e5fc2",
                    font=('helvetica', 32, 'bold underline'))
    gui_canvas.create_window(400, 60, window=head)

    # Buttons
    new_button = tk.Button(gui_canvas, text="New", bg="#093240", padx=40, pady=30, fg='white', command=folder_run)
    gui_canvas.create_window(400, 240, window=new_button)

    add_button = tk.Button(gui_canvas, text="Add", bg="#093240", padx=40, pady=30, fg='white', command=add_feature)
    gui_canvas.create_window(400, 380, window=add_button)

    exit_button = tk.Button(gui_canvas, text="Exit", bg="#093240", padx=40, pady=30, fg='white', command=close)
    gui_canvas.create_window(400, 520, window=exit_button)

    gui_root.mainloop()


# Run
if __name__ == '__main__':
    main_gui()
