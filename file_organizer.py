import tkinter as tk
import tkinter.messagebox as msgb
import os 
import shutil


root = tk.Tk()
root.title('File Organizer App')
root.geometry("700x100")

def organize_files():
    
    try:
        path = entry_field.get()
        files = os.listdir(path)
        for file in files:
            
            if os.path.isfile(os.path.join(path,file)):
                name, extension = file.split('.')
                if extension == 'DS_Store':
                    continue
                if os.path.exists(f"{path}/{extension}"):
                    shutil.move(f"{path}/{file}",f"{path}/{extension}/{file}")
                else:
                    os.makedirs(f"{path}/{extension}")
                    shutil.move(f"{path}/{file}",f"{path}/{extension}/{file}")
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