# GBOARD-DICTIONARY-MAKER
# MADE BY:- KARAN ARORA AND KARTHIK NAIR

import os
import tkinter as tk
from tkinter import messagebox, filedialog
import datetime
from zipfile import ZipFile

os_name = os.name


def do_exit():
    """ Exit Command """
    home_gui.destroy()
    exit()


def go_back(entry):
    """ When Back Button is pressed """
    global file_name1
    if entry == "new_folder":
        new_root.destroy()
        main_gui()
    elif entry == "new":
        if str(word_entry.get()) not in ["", " "] or str(shortcut_entry.get()) not in ["", " "]:
            asK_user = messagebox.askokcancel("Are you sure?", "Are you sure you want to go back?\nNo Progress will be saved!")
            if asK_user:
                os.remove("{}".format(file_name1))
                word_gui.destroy()
                main_gui()
        else:
            asK_user = messagebox.askokcancel("Are you sure?", "Are you sure you want to go back?\nNo Progress will be saved!")
            if asK_user:
                os.remove("{}".format(file_name1))
                word_gui.destroy()
                main_gui()
    elif entry == "choose_file":
        choose_gui.destroy()
        main_gui()
    elif entry == "add":
        if str(new_word_entry.get()) not in ["", " "] or str(new_shortcut_entry.get()) not in ["", " "]:
            asK_user = messagebox.askokcancel("Are you sure?", "Are you sure you want to go back?\nNo Progress will be saved!")
            if asK_user:
                os.remove("{}.txt".format(add_file_name[:-4]))
                new_add_gui.destroy()
                main_gui()
        else:
            asK_user = messagebox.askokcancel("Are you sure?",
                                              "Are you sure you want to go back?\nNo Progress will be saved!")
            if asK_user:
                os.remove("{}.txt".format(add_file_name[:-4]))
                new_add_gui.destroy()
                main_gui()


def file_generate():
    """ Generates Filename and File """
    global path
    with open('folder_path.txt', 'r') as file_read:
        file_contents = file_read.readline()
        path = os.path.join(file_contents, "Gboard-Shortcuts")
        file_read.close()
    filename = str(path) + "/shortcuts-" + datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S") + ".txt"
    with open(filename, 'w') as new_file:
        new_file.write("# Gboard Dictionary version:1\n")
        new_file.close()
    return filename


def save(entry, filename):
    """ Saves the File when 'Save' button is pressed """
    global path, add_file_name
    with open('folder_path.txt', 'r') as file_read:
        file_contents = file_read.readline()
        path = os.path.join(file_contents, "Gboard-Shortcuts")
        file_read.close()
        if entry == "new" and ' ' in str(shortcut_entry.get()):  # Saves only when shortcut is one word
            messagebox.showerror("(!) Shortcut (!)", "Shortcut can't be more than one word!")
        elif entry == "add" and ' ' in str(new_shortcut_entry.get()):
            messagebox.showerror("(!) Shortcut (!)", "Shortcut can't be more than one word!")
        else:
            if entry == "new" or entry == "add":  # If the User doesn't use Add more fn
                if entry == "new":
                    word = str(word_entry.get())
                    shortcut = str(shortcut_entry.get())
                    word_input.set("")
                    shortcut_input.set("")
                else:
                    word = str(new_word_entry.get())
                    shortcut = str(new_shortcut_entry.get())
                    new_word.set("")
                    new_shortcut.set("")
                txt_file = open('{}.txt'.format(filename), 'a+')
                to_write = "{}\t{}\t\n".format(shortcut, word)
                txt_file.write(to_write)
                txt_file.close()
            # Zip the file and Deletes the .txt file
            if entry == "new":
                zipObj = ZipFile('{}.zip'.format(filename), 'w')
                zipObj.write('{}.txt'.format(filename), str(filename.replace(path + "/", "")) + ".txt")
                zipObj.close()
                os.remove("{}.txt".format(filename))
                messagebox.showinfo('(!) Saving.... (!)', "Saving file..\nFile:'{}.zip'".format(filename))
                word_gui.destroy()
                main_gui()
            elif entry == "add":
                zipObj = ZipFile('{}.zip'.format(filename), 'w')
                zipObj.write('{}.txt'.format(filename), str(filename.replace(path + "/", "")) + ".txt")
                zipObj.close()
                os.remove("{}.txt".format(filename))
                messagebox.showinfo('(!) Saving Changes.... (!)', "Saving file..\nFile:'{}.zip'".format(filename))
                add_file_name = ""
                new_add_gui.destroy()
                main_gui()


def add_more_words(entry, filename):
    """ When Add More Button if Pressed """
    global word_input, shortcut_input, new_word, new_shortcut
    if entry == "new" and ' ' in str(shortcut_entry.get()):  # Saves only when shortcut is one word
        messagebox.showerror("(!) Shortcut (!)", "Shortcut can't be more than one word!")
    elif entry == "add" and ' ' in str(new_shortcut_entry.get()):
        messagebox.showerror("(!) Shortcut (!)", "Shortcut can't be more than one word!")
    else:
        if entry == "new":  # When pressed from New Window
            word = str(word_entry.get())
            shortcut = str(shortcut_entry.get())
            word_input.set("")
            shortcut_input.set("")
            with open(filename, 'a+') as file_write:
                file_write.write("{}\t{}\t\n".format(shortcut, word))
                file_write.close()
        elif entry == "add":  # When pressed from Add Window
            new_words = str(new_word_entry.get())
            new_shortcuts = str(new_shortcut_entry.get())
            new_word.set("")
            new_shortcut.set("")
            with open(filename+".txt", 'a+') as file_write:
                file_write.write("{}\t{}\t\n".format(new_shortcuts, new_words))
                file_write.close()


def add_window(file):
    """ Add Words Gui """
    global new_add_gui, new_word, new_shortcut, new_word_entry, new_shortcut_entry
    with open('folder_path.txt', 'r') as file_read:
        path1 = str(file_read.readline())
        file_read.close()
    if os.path.exists(file):
        choose_gui.destroy()

        new_add_gui = tk.Tk()
        new_add_gui.title('{}.txt'.format(add_file_name[:-4]))
        new_add_gui.geometry('600x500')
        new_add_gui.resizable(width=False, height=False)

        new_add_gui_can = tk.Canvas(new_add_gui, bg="#ba8f6a", height=500, width=600)
        new_add_gui_can.pack()

        heading = tk.Label(new_add_gui_can, text="ADD", bg="#ba8f6a", fg="yellow",
                           font=('helvetica', 24, 'bold underline'))
        new_add_gui_can.create_window(300, 40, window=heading)

        new_frame = tk.Frame(new_add_gui, bg="#ba8f6a")
        new_add_gui_can.create_window(190, 180, window=new_frame)

        scroll_bar = tk.Scrollbar(new_frame)
        scroll_bar.pack(side="right", fill="y")

        dictionary = tk.Listbox(new_frame, yscrollcommand=scroll_bar.set, width=40)
        # Extract the .txt from Zip (add_file_name = zip selected by the user)
        with ZipFile(add_file_name, 'r') as zip_files:
            zip_files.extractall(path=os.path.join(path1, 'Gboard-Shortcuts'))
        a_file = open("{}.txt".format(add_file_name[:-4]), 'r')
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
        new_add_gui_can.create_window(470, 100, window=new_word_l)
        new_word_entry = tk.Entry(new_add_gui_can, textvariable=new_word)
        new_add_gui_can.create_window(470, 120, window=new_word_entry)

        new_shortcut = tk.StringVar()
        new_short_l = tk.Label(new_add_gui_can, text="Shortcut: -", bg="#ba8f6a", fg="yellow")
        new_add_gui_can.create_window(470, 180, window=new_short_l)
        new_shortcut_entry = tk.Entry(new_add_gui_can, textvariable=new_shortcut)
        new_add_gui_can.create_window(470, 200, window=new_shortcut_entry)

        add_more_button = tk.Button(new_add_gui_can, text="Add More", bg="skyblue", padx=15, pady=10,
                                    command=lambda: (add_more_words("add", add_file_name[:-4])))
        new_add_gui_can.create_window(240, 400, window=add_more_button)

        save_button = tk.Button(new_add_gui_can, text="Save", bg="lime", padx=15, pady=10,
                                command=lambda: (save("add", add_file_name[:-4])))
        new_add_gui_can.create_window(340, 400, window=save_button)

        back_button = tk.Button(new_add_gui_can, text="Back", bg="yellow", padx=5, pady=5, command=lambda: (go_back("add")))
        new_add_gui_can.create_window(40, 40, window=back_button)

        new_add_gui.mainloop()


def browse_file():
    """ Let User select a Zip File! """
    global file_selected, add_file_name, path, new_filename
    with open('folder_path.txt', 'r') as file_read:
        temp_path = os.path.join(str(file_read.readline()), 'Gboard-Shortcuts')
        file_read.close()
    file_selected = filedialog.askopenfilename(initialdir=temp_path, filetypes=[("zip", "*.zip")])
    add_file_name = file_selected
    new_filename = str(add_file_name[:-4]).replace(temp_path + '/', "")


def choose_file():
    """ User Can select which file to open """
    global choose_gui
    if check_folder("add"):
        home_gui.destroy()
        choose_gui = tk.Tk()
        choose_gui.title('Choose File')
        choose_gui.geometry('300x100')
        choose_gui.resizable(width=False, height=False)

        choose_label = tk.Label(choose_gui, text="Select A File:")
        choose_label.pack()

        browse_button = tk.Button(choose_gui, text="Browse", bg="skyblue", command=browse_file)
        browse_button.pack()

        open_button = tk.Button(choose_gui, text="Open", bg="lightgreen", command=lambda: (add_window(add_file_name)))
        open_button.pack()

        # In-Case someone has no existing file
        back_button = tk.Button(choose_gui, text="Back", bg="yellow", command=lambda: (go_back("choose_file")))
        back_button.pack()

        choose_gui.mainloop()


def new_window(fn):
    """ New Words Gui """
    global word_gui, word_input, shortcut_input, word_entry, shortcut_entry

    home_gui.destroy()
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
                            command=lambda: (save("new", fn[:-4])))
    word_canvas.create_window(300, 350, window=save_button)

    # Add More Button
    add_more_button = tk.Button(word_canvas, text="Add More", bg="skyblue", padx=15, pady=10,
                                command=lambda: (add_more_words("new", fn)))
    word_canvas.create_window(200, 350, window=add_more_button)

    # Back Button
    back_button = tk.Button(word_canvas, text="Back", bg="yellow", padx=5, pady=5, command=lambda: (go_back("new")))
    word_canvas.create_window(40, 60, window=back_button)

    word_gui.mainloop()


def browse(selected):
    """ Let the user select path to make the folder (connected to new_folder()) """
    if not selected:
        folder_selected = filedialog.askdirectory()
        folder_path.set(folder_selected)
    if selected and str(entry_box.get()) in ['', ' ']:  # If user doesn't select a directory
        if os_name == "nt":
            default = "C:/"
        else:
            default = os.getenv('HOME')
        messagebox.showinfo("Default Directory Selected!", "Folder Created at:- {}".format(default))
        new_path = os.path.join(default, 'Gboard-Shortcuts')
        os.mkdir(new_path)
        with open('folder_path.txt', 'w') as file2:
            file2.write(default)
            file2.close()
        new_root.destroy()
        main_gui()
    if (not selected and str(entry_box.get()) not in ['', ' ']) or (selected and str(entry_box.get()) not in ['', ' ']):  # If user enters or selects directory
        check_dir = os.path.exists(str(entry_box.get()))
        if check_dir:
            messagebox.showinfo("Folder Created Successfully!", "Folder Created at:- {}".format(str(entry_box.get())))
            with open('folder_path.txt', 'w') as file2:
                file2.write(str(entry_box.get()))
                file2.close()
            new_path = os.path.join(str(entry_box.get()), 'Gboard-Shortcuts')
            os.mkdir(new_path)
            new_root.destroy()
            main_gui()
        else:
            messagebox.showerror("(!) Error (!)", "Directory Doesn't Exist!")


def new_folder():
    """ Creates a New Folder if one doesn't exists """
    global new_root, folder_path, path_selected, entry_box
    home_gui.destroy()
    path_selected = False
    new_root = tk.Tk()
    new_root.title('Enter Path')
    new_root.geometry('300x150')
    new_root.resizable(width=False, height=False)

    new_label = tk.Label(new_root, text="Path:")
    new_label.pack()

    folder_path = tk.StringVar()
    entry_box = tk.Entry(new_root, textvariable=folder_path)
    entry_box.pack()

    browse_button = tk.Button(new_root, text="Browse", bg="skyblue", command=lambda: (browse(False)))
    browse_button.pack()

    select_button = tk.Button(new_root, text="Select", bg="lightgreen", command=lambda: (browse(True)))
    select_button.pack()

    back_button = tk.Button(new_root, text="Back", bg="yellow", command=lambda: (go_back("new_folder")))
    back_button.pack()

    new_root.mainloop()


def check_folder(entry):
    """ Checks if the Folder exist at path mentioned in folder_path.txt! """
    global file_name1
    with open("folder_path.txt", "r") as file:
        file_content = file.readline()
        file.close()
    if file_content in ['', ' ']:  # Checks if the file is empty
        if os_name == "nt":
            to_write = "C:/"
            name = "Windows"
        elif os_name == "posix":
            to_write = str(os.getenv("HOME"))
            name = "Linux"
        else:
            to_write, name = ["", ""]
        with open("folder_path.txt", 'w') as file1:
            file1.write(to_write)  # Write the default directory to folder_path.txt
            file1.close()
        messagebox.showinfo("(!) {} Detected! (!)".format(name), "(!) Updating Path... (!)")
    elif file_content not in ['', ' ']:  # If the file is not empty
        temp_path = os.path.join(file_content, "Gboard-Shortcuts")
        isdir = os.path.isdir(temp_path)
        if isdir:  # if folder exist
            if entry == "new":
                fn = file_generate()
                file_name1 = fn
                new_window(fn)
            else:
                return True
        else:  # if folder doesn't exist
            messagebox.showinfo("Folder Doesn't Exist",
                                "Select/Enter Path or Click on\nleave it blank! It will select\nDefault Directory!")
            new_folder()


def main_gui():
    """ HOME GUI """
    global home_gui
    home_gui = tk.Tk()
    home_gui.title("G BOARD DICTIONARY")
    home_gui.geometry('800x800')
    home_gui.resizable(width=False, height=False)

    home_canvas = tk.Canvas(home_gui, bg="#ccbcaf", height=800, width=800)
    home_canvas.pack()

    # LOGO
    logo = tk.PhotoImage(file="res/logo.png")
    home_canvas.create_image(420, 210, image=logo)

    # Heading of GUI
    head = tk.Label(home_canvas, text="G-BOARD Dictionary Maker", fg='#cbecf2', bg="#ccbcaf",
                    font=('', 32, 'bold underline'))
    home_canvas.create_window(400, 60, window=head)

    # Buttons
    new_button = tk.Button(home_canvas, text="New", font=('', 12, 'bold'), bg="#7953ad", padx=35, pady=25, fg='white',
                           command=lambda: (check_folder("new")))
    home_canvas.create_window(400, 400, window=new_button)

    add_button = tk.Button(home_canvas, text="Add", font=('', 12, 'bold'), bg="#7953ad", padx=35, pady=25, fg='white',
                           command=choose_file)
    home_canvas.create_window(400, 540, window=add_button)

    exit_button = tk.Button(home_canvas, text="Exit", font=('', 12, 'bold'), bg="#7953ad", padx=35, pady=25, fg='white',
                            command=do_exit)
    home_canvas.create_window(400, 680, window=exit_button)

    home_gui.mainloop()


# Run
if __name__ == '__main__':
    check = os.path.isfile('folder_path.txt')
    if check:
        main_gui()
    else:
        with open('folder_path.txt', 'w') as check_file:
            check_file.close()
        main_gui()
