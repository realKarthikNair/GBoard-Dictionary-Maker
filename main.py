# GBoard Dictionary Maker GUI
# Made By- Karthik Nair and Karan Arora

import os
import datetime
from zipfile import ZipFile

os_name = os.name
words = []
shortcuts = []
selected = False
entry = "None"
f = 5


def save(entry):
    """ Saves the Word and Shortcut Entered (if user don't want to add more words) """
    global words, shortcuts, path, total_words, total_shortcuts
    if entry == "new":
        words.append(str(word_entry.get()))
        shortcuts.append(str(shortcut_entry.get()))
    else:
        total_words.append(new_word_entry.get())
        total_shortcuts.append(new_shortcut_entry.get())
    # Takes the path from the folder_path.txt
    with open('folder_path.txt', 'r') as file_check:
        file_contents = file_check.readline()
        path = str(file_contents)
    file_check.close()
    if entry == "new":
        if os_name == "nt":
            # Windows (Generates File Name)
            path = path + "Gboard-Shortcuts"
            file_name = str(path) + "/shortcuts-" + datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S") + ".txt"
        else:
            # Other than Windows (Generates File Name)
            file_name = os.path.join(str(path),
                                     "shortcuts-" + datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S") + ".txt")

        # Enter the Values into an .txt file (name generated above)
        with open('{}'.format(file_name), 'w') as file_save:
            file_save.write("# Gboard Dictionary version:1\n")
            if entry == "new":
                # If running from New
                for i in range(0, len(words)):
                    file_save.write("{}\t{}\n".format(shortcuts[i], words[i]))
        file_save.close()
        # Just Create a Zip File with the same name and deletes the txt file
        file_name = file_name[:-4]
        zipObj = ZipFile('{}.zip'.format(file_name), 'w')
        zipObj.write('{}.txt'.format(file_name), str(file_name.replace(path + "/", "")) + ".txt")
        zipObj.close()
        os.remove("{}.txt".format(file_name))
        messagebox.showinfo('(!) Saving.... (!)', "Saving file..\nFile:'{}.zip'".format(file_name))
        word_gui.destroy()
        words = []
        shortcuts = []
    else:
        txt_file = open('{}.txt'.format(add_file_name[:-4]), 'a+')
        for i in range(0, len(total_words)):
            written = ("{}\t{}\n".format(total_shortcuts[i], total_words[i]))
            txt_file.writelines(written)
        txt_file.close()
        zipObj = ZipFile('{}'.format(add_file_name), 'w')
        zipObj.write('{}.txt'.format(add_file_name[:-4]), add_file_name[:-4].replace(path1 + "/", "") + ".txt")
        zipObj.close()
        os.remove("{}.txt".format(add_file_name[:-4]))
        messagebox.showinfo('(!) Saving Changes.... (!)', "Saving file..\nFile:'{}.zip'".format(add_file_name[:-4]))
        new_add_gui.destroy()
        total_words = []
        total_shortcuts = []
    main_gui()


def check_words(entry, sr):
    fwd = True
    if entry == "new":
        check_word = str(word_entry.get())
        check_shortcut = str(shortcut_entry.get())
        if sr == "save":
            if check_word in ("", " ") or check_shortcut in ("", " "):
                fwd = False
        if sr == "add_more":
            if check_word in ("", " ") or check_shortcut in ("", " "):
                fwd = False
    else:
        check_word = str(new_word_entry.get())
        check_shortcut = str(new_shortcut_entry.get())
        if sr == "save":
            if check_word in ("", " ") or check_shortcut in ("", " "):
                fwd = False
        if sr == "add_more":
            if check_word in ("", " ") or check_shortcut in ("", " "):
                fwd = False
    if fwd:
        if entry == "new" and sr == "save":
            save(entry="new")

        elif entry == "new" and sr == "add_more":
            add_more_words(entry="new")

        if entry == "add" and sr == "save":
            save(entry="add")

        elif entry == "add" and sr == "add_more":
            add_more_words(entry="add")

    else:
        messagebox.showerror("(!) ERROR (!)", "The Words and Shortcuts cannot be blank!")


def add_more_words(entry):
    """ Set Status to Add More """
    global word_input, shortcut_input, words, shortcuts, new_word, new_shortcut, total_words, total_shortcuts
    # Gets the value from the entry boxes and clear them
    if entry == "new":
        words.append(str(word_entry.get()))
        shortcuts.append(str(shortcut_entry.get()))
        word_input.set("")
        shortcut_input.set("")
    elif entry == "add":
        total_words.append(str(new_word_entry.get()))
        total_shortcuts.append(str(new_shortcut_entry.get()))
        new_word.set("")
        new_shortcut.set("")


def gboarddict():
    """ GUI for Entering Word and Shortcut (Works when New is selected!)"""
    global word_gui, word_entry, shortcut_entry, word_input, shortcut_input
    word_gui = tk.Tk()
    word_gui.title('GBOARD Dictionary Maker')
    word_gui.geometry('500x500')
    word_gui.iconbitmap(r'res/logo.ico')
    word_gui.resizable(width=False, height=False)

    word_canvas = tk.Canvas(word_gui, bg='#ba8f6a', height=500, width=500)
    word_canvas.pack()

    # Heading
    heading = tk.Label(word_canvas, text="GBOARD Dictionary Maker", fg="yellow", bg="#ba8f6a",
                       font=('helvetica', 18, 'bold underline'))
    word_canvas.create_window(250, 40, window=heading)

    # Word
    word_label = tk.Label(word_canvas, text="Word: -", bg="#ba8f6a", fg="black", font=('', 14))
    word_canvas.create_window(170, 150, window=word_label)
    word_input = tk.StringVar()
    word_entry = tk.Entry(word_canvas, textvariable=word_input)
    word_canvas.create_window(320, 150, window=word_entry)

    # Shortcut
    shortcut_label = tk.Label(word_canvas, text="Shortcut: -", bg="#ba8f6a", fg="black", font=('', 14))
    word_canvas.create_window(160, 220, window=shortcut_label)
    shortcut_input = tk.StringVar()
    shortcut_entry = tk.Entry(word_canvas, textvariable=shortcut_input)
    word_canvas.create_window(320, 220, window=shortcut_entry)

    # Save Button
    save_button = tk.Button(word_canvas, text='Save', bg='#3dd46a', padx=15, pady=10,
                            command=lambda: (check_words(entry="new", sr="save")))
    word_canvas.create_window(300, 350, window=save_button)

    # Add More Button
    add_more_button = tk.Button(word_canvas, text="Add More", bg="yellow", padx=15, pady=10,
                                command=lambda: (check_words(entry="new", sr="add_more")))
    word_canvas.create_window(200, 350, window=add_more_button)

    # Back Button
    add_more_button = tk.Button(word_canvas, text="Back", bg="red", fg="white", padx=5, pady=5,
                                command=lambda: (go_back(back="new")))
    word_canvas.create_window(40, 60, window=add_more_button)

    word_gui.mainloop()


def check_dir():
    """ Checks if the users entered/selected path exist or not! And if it does it creates a Folder """
    input_path = str(user_entry_box.get())
    # if the user doesn't enter anything it is selected as default folder defined below
    if input_path in ["", " "]:
        if os_name == "nt":
            input_path = "C:/"
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
    # If user selects or enters their own path
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
    """ Enables user to select folder! """
    global folder_selected
    folder_selected = filedialog.askdirectory()
    folder_path.set(folder_selected)


def new_folder():
    """ Creates a new folder (Works when New is selected)"""
    global user_entry_box, new_root, folder_path
    # Asks user to enter the path for the folder
    new_root = tk.Tk()
    new_root.title('Enter Path')
    new_root.iconbitmap(r'res/logo.ico')
    new_root.geometry('300x150')
    new_root.resizable(width=False, height=False)

    new_label = tk.Label(new_root, text="Path:")
    new_label.pack()

    folder_path = tk.StringVar()
    user_entry_box = tk.Entry(new_root, textvariable=folder_path)
    user_entry_box.pack()

    browse_button = tk.Button(new_root, text="Browse", bg="lightgreen", command=browse)
    browse_button.pack()

    select_button = tk.Button(new_root, text="Select", bg="lightgreen", command=check_dir)
    select_button.pack()

    back_button = tk.Button(new_root, text="Back", bg="red", command=lambda: (go_back(back="new_folder")))
    back_button.pack()

    new_root.mainloop()


def check_folder(os_name):
    """ Checks if the Folder exists in the default directory (if not then it redirects to new_folder() function to create a folder) """
    global path
    if os_name == 'nt':
        # Windows
        with open('folder_path.txt', 'r') as file:
            file_contents = file.readline()
        path = str(file_contents) + "Gboard-Shortcuts"
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


def folder_run():
    """ Just Set the status to save which helps in Save() fn and also runs check_folder() fn"""
    global status
    status = "save"
    check_folder(os_name)


def choose():
    """ Let User select a Zip File! """
    global add_file_name, selected, path1, temp_path, folder_selected
    with open('folder_path.txt', 'r') as file_check:
        file_contents = file_check.readline()
        path1 = str(file_contents)
        temp_path = path1
    file_check.close()
    if os_name == "nt":
        # Windows (Generates File Name)
        path1 = path1 + "Gboard-Shortcuts"
    elif os_name == "posix":
        path1 = os.getenv("HOME")
        path1 = str(path) + "/Gboard-Shortcuts"
    folder_selected = filedialog.askopenfilename(initialdir=path1)
    add_file_name = folder_selected
    selected = True


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?\n(No Effect will take place!)"):
        new_add_gui.destroy()
        os.remove("{}.txt".format(add_file_name[:-4]))


def open_file():
    """ Open the Selected File and Let's User add More words (connected to file_choose() fn) """
    global new_add_gui, new_word_entry, new_shortcut_entry, new_word, new_shortcut, selected, total_words, total_shortcuts
    total_words = []
    total_shortcuts = []
    run = 1
    if selected:
        # Works only when user has selected a File
        selected = False
        add_gui.destroy()

        new_add_gui = tk.Tk()
        new_add_gui.title('{}.txt'.format(add_file_name[:-4]))
        new_add_gui.geometry('500x400')
        new_add_gui.iconbitmap(r'res/logo.ico')
        new_add_gui.resizable(width=False, height=False)

        new_add_gui_can = tk.Canvas(new_add_gui, bg="#ba8f6a", height=400, width=500)
        new_add_gui_can.pack()

        # Heading
        heading = tk.Label(new_add_gui_can, text="ADD", bg="#ba8f6a", fg="yellow",
                           font=('helvetica', 20, 'bold underline'))
        new_add_gui_can.create_window(250, 40, window=heading)

        new_frame = tk.Frame(new_add_gui, bg="#ba8f6a")
        new_add_gui_can.create_window(170, 150, window=new_frame)

        scroll_bar = tk.Scrollbar(new_frame)
        scroll_bar.pack(side="right", fill="y")

        dictionary = tk.Listbox(new_frame, yscrollcommand=scroll_bar.set, width=40)

        # Extract the .txt from Zip (add_file_name = zip selected by the user)
        with ZipFile(add_file_name, 'r') as zip_files:
            zip_files.extractall(path=path1)

        if os_name == "nt":
            a_file = open("{}.txt".format(add_file_name[:-4]), 'r')

        else:
            # If this doesn't work on linux change this
            a_file = open("{}.txt".format(add_file_name[:-4]), "r")

        for file_words in a_file:
            temp_words = (file_words.replace("\r\n", "")).replace("\t", "    ")
            dictionary.insert("end", temp_words)
        a_file.close()

        # Scrollbar related
        scroll_bar.config(command=dictionary.yview)
        dictionary.pack()

        # GUI related
        new_word = tk.StringVar()
        new_word_l = tk.Label(new_add_gui_can, text="Word: -", bg="#ba8f6a", fg="yellow")
        new_add_gui_can.create_window(400, 100, window=new_word_l)
        new_word_entry = tk.Entry(new_add_gui_can, textvariable=new_word)
        new_add_gui_can.create_window(400, 120, window=new_word_entry)

        new_shortcut = tk.StringVar()
        new_short_l = tk.Label(new_add_gui_can, text="Shortcut: -", bg="#ba8f6a", fg="yellow")
        new_add_gui_can.create_window(400, 180, window=new_short_l)
        new_shortcut_entry = tk.Entry(new_add_gui_can, textvariable=new_shortcut)
        new_add_gui_can.create_window(400, 200, window=new_shortcut_entry)

        add_more_button = tk.Button(new_add_gui_can, text="Add More", bg="yellow", padx=15, pady=10,
                                    command=lambda: (check_words(entry="add", sr="add_more")))
        new_add_gui_can.create_window(200, 300, window=add_more_button)

        save_button = tk.Button(new_add_gui_can, text="Save", bg="lime", padx=15, pady=10,
                                command=lambda: (check_words(entry="add", sr="save")))
        new_add_gui_can.create_window(300, 300, window=save_button)

        back_button = tk.Button(new_add_gui_can, text="Back", bg="red", padx=5, pady=5, command=lambda: (go_back(back="add")))
        new_add_gui_can.create_window(40, 40, window=back_button)

        new_add_gui.protocol("WM_DELETE_WINDOW", on_closing)
        new_add_gui.mainloop()

    else:
        messagebox.showerror('(!) Error (!)', "Choose A File!!")


def go_back(back):
    """ To Go Back (Functional back button) """
    global words, shortcuts, total_words, total_shortcuts, folder_selected
    if back == "file_choose":
        folder_selected = ""
        add_gui.destroy()
        main_gui()
    elif back == "add":
        if len(total_words) != 0 and len(total_shortcuts) != 0:
            ans = messagebox.askokcancel("Going Back...", "You will lost your progress!")
            if ans:
                total_words = []
                total_shortcuts = []
                os.remove("{}.txt".format(add_file_name[:-4]))
                new_add_gui.destroy()
                main_gui()
        else:
            os.remove("{}.txt".format(add_file_name[:-4]))
            new_add_gui.destroy()
            main_gui()
    elif back == "new":
        if len(words) != 0 and len(shortcuts) != 0:
            ans = messagebox.askokcancel("Going Back...", "You will lost your progress!")
            if ans:
                words = []
                shortcuts = []
                word_gui.destroy()
                main_gui()
        else:
            word_gui.destroy()
            main_gui()
    elif back == "new_folder":
        folder_selected = ""
        new_root.destroy()
        main_gui()


def file_choose():
    """ GUI for choosing file (Works when ADD is selected) """
    global add_gui, add_file_name, add_label, choose_button, open_button
    # GUI
    gui_root.destroy()

    add_gui = tk.Tk()
    add_gui.title('Choose File')
    add_gui.geometry('300x100')
    add_gui.iconbitmap(r'res/logo.ico')
    add_gui.resizable(width=False, height=False)

    add_label = tk.Label(add_gui, text="Select A File:")
    add_label.pack()

    choose_button = tk.Button(add_gui, text="Browse", bg="yellow", command=choose)
    choose_button.pack()

    open_button = tk.Button(add_gui, text="Open", bg="lightgreen", command=open_file)
    open_button.pack()

    # In-Case someone has no existing file
    back_button = tk.Button(add_gui, text="Back", bg="red", fg="white", command=lambda: (go_back(back="file_choose")))
    back_button.pack()

    add_gui.mainloop()


def close():
    """ Closes the Program (Works when Exit Button is Pressed!)"""
    gui_root.destroy()
    exit()


def main_gui():
    """ Main Screen or GUI """
    global gui_root
    """ Main Menu """
    gui_root = tk.Tk()
    gui_root.title('GBOARD Dictionary Maker')
    gui_root.geometry('800x800')
    gui_root.iconbitmap(r'res/logo.ico')
    gui_root.resizable(width=False, height=False)

    gui_canvas = tk.Canvas(gui_root, bg="#ccbcaf", height=800, width=800)
    gui_canvas.pack()

    # LOGO
    logo = tk.PhotoImage(file="res/logo.png")
    gui_canvas.create_image(420, 210, image=logo)

    # Heading of GUI
    head = tk.Label(gui_canvas, text="G-BOARD Dictionary Maker", fg='#cbecf2', bg="#ccbcaf", font=('', 32, 'bold underline'))
    gui_canvas.create_window(400, 60, window=head)

    # Buttons
    new_button = tk.Button(gui_canvas, text="New", font=('', 12, 'bold'), bg="#7953ad", padx=35, pady=25, fg='white', command=folder_run)
    gui_canvas.create_window(400, 400, window=new_button)

    add_button = tk.Button(gui_canvas, text="Add", font=('', 12, 'bold'), bg="#7953ad", padx=35, pady=25, fg='white', command=file_choose)
    gui_canvas.create_window(400, 540, window=add_button)

    exit_button = tk.Button(gui_canvas, text="Exit", font=('', 12, 'bold'), bg="#7953ad", padx=35, pady=25, fg='white', command=close)
    gui_canvas.create_window(400, 680, window=exit_button)

    gui_root.mainloop()


# Run
if __name__ == '__main__':
    try:
        # Tries to import tkinter if installed already
        import tkinter as tk
        from tkinter import messagebox, filedialog
    # if tkinter is not installed then first it check the OS and then tries to install it
    except:
        try:
            if os_name == "nt":
                # Windows
                os.system("pip install tk")
            else:
                # Linux
                os.system('''x-terminal-emulator -e "sudo apt-get install python3-tk"''')
        except:
            print("Unable to install dependencies, Try manually installing tkinter!")
    main_gui()
