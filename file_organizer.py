import tkinter as tk
import tkinter.messagebox as msgb
import os 
import shutil
import filecmp

root = tk.Tk()
root.title('File Organizer App')
root.geometry("700x100")

def organize_files():
    
    try:
        path = entry_field.get()
        files = os.listdir(path)
        for file in files:
            if os.path.isfile(os.path.join(path,file)):
                name, extension = os.path.splitext(file)
                if extension.lower() in ['.ds_store', '.ini']:
                    continue
                dest_dir = os.path.join(path, extension[1:].lower())
                if not os.path.exists(dest_dir):
                    os.makedirs(dest_dir)
                dest_file = os.path.join(dest_dir, file)
                if not os.path.exists(dest_file) or not filecmp.cmp(os.path.join(path, file), dest_file):    #filecmp.cmp check if the same file name exists or not in the organized folder 
                    shutil.move(os.path.join(path, file), dest_file)
        msgb.showinfo(title='Success', message="All the files inside the added folder were organized")
    except ValueError:
        msgb.showerror(title='Error', message="There are not any file for organizing. Please make sure that you have added right path")

label = tk.Label(root,text='Please add a folder path where you want to organize files into folders')
label.pack()

entry_field = tk.Entry(root)
entry_field.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

confirm_button = tk.Button(root,text='Confirm', command=organize_files)
confirm_button.pack()

root.mainloop()

