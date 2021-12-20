# GBoard Dictionary Maker GUI
import tkinter as tk
from tkinter import messagebox, filedialog
import os
import datetime
from zipfile import ZipFile

system = os.name


def check_dir():
    input_path = str(user_entry_box.get())
    if input_path in ["", " "]:
        if system == "nt":
            input_path = "c:\\"
        elif system == "posix":
            input_path = os.getenv("HOME")
        messagebox.showinfo('(!) Default Folder Selected (!)',
                            "The Folder has been created at:-\n'{}'".format(input_path))
        new_root.destroy()
        with open('folder_path.txt', 'w') as file:
            file.writelines("{}".format(input_path))
        file.close()
        new_path = os.path.join(input_path, 'Gboard-Shortcuts')
        os.mkdir(new_path)
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


def check_folder(system):
    """ Checks if the Folder exists in the default directory """
    if system == 'nt':
        # Windows
        with open('folder_path.txt', 'r') as file:
            file_contents = file.readline(1)
        path = str(file_contents)
        file.close()
        isdir = os.path.isdir(path)
        if not isdir:
            messagebox.showinfo("(!) No Folder Found (!)",
                                "No Folder Found! Enter the path to make one\nor leave it blank to save it in default path.\ndefault path = 'c:\\gboard_shortcuts'")
            gui_root.destroy()
            new_folder()

    elif system == 'posix':
        # Linux
        with open('folder_path.txt', 'r') as file:
            file_contents = file.readline(2)
        path = str(file_contents)
        file.close()
        isdir = os.path.isdir(path)
        if not isdir:
            messagebox.showinfo("(!) No Folder Found (!)",
                                "No Folder Found! Enter the path to make one\nor leave it blank to save it in default path.\ndefault path = '$HOME/gboard_shortcuts'")
            gui_root.destroy()
            new_folder()
    else:
        # Android , the lowest possible directory an app can access is /data/data/<data partition of that app> without root access )
        path = os.path.join(os.environ['HOME'], "gboard_shortcuts")
        if "/data" == path[
                      0:5]:  # for android (in android , the lowest possible directory an app can access is /data/data/<data partition of that app> without root access )
            path = "/storage/emulated/0/gboard_shortcuts"
        print(f"(default is {path} )")


def folder_run():
    check_folder(system)


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

    add_button = tk.Button(gui_canvas, text="Add", bg="#093240", padx=40, pady=30, fg='white')
    gui_canvas.create_window(400, 380, window=add_button)

    exit_button = tk.Button(gui_canvas, text="Exit", bg="#093240", padx=40, pady=30, fg='white')
    gui_canvas.create_window(400, 520, window=exit_button)

    gui_root.mainloop()


if __name__ == '__main__':
    main_gui()
