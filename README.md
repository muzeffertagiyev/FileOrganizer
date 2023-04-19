# File organizer app

# 

It organize files as per their type in the given directory.

# Introduction Video of the App


https://user-images.githubusercontent.com/75939608/232980869-c99f8ede-3205-42d9-9154-004ba323a58c.mov


## Tech Stack

**Backend technologies:** 

- Python v3.10.x or higher,

- Libraries

    - tkinter
    - tkinter.messagebox
    - os
    - shutil
    

## About application

The project is divided to :

- GUI section :

    aims to create a GUI by containing label,entry field and confirm button.When user adds path and clicks confirm button it starts to organize file in the added directory. 

    - we create root variable for tkinter library for getting Tk() class
    - then we make a app name using root.title method
    - we adjust our GUI window by using geometry method 700 means width, 100 means height
    - We use Label method for creating a text in the top of GUI window for showing what app does.
    - We create entry field using Entry method and we adjust it is place by using pack method.
    - then we created confirm button by using Button method  and as a command when click this button it will call organize_files function
    - In the last we used root.mainloop() to make our window open till we close it

- File organizer section :

    Inside organize_files function we use os and shutil modules for creating folders as per data type and move our files into these folders.
    - we used try and except method for catching when if there is not any file for organizing it shows error by help of tkinter.messagebox.showerror
    - we create path variable for getting path from user's entry into entry field
    - we get all the files' (folders too) names as a list using os.listdir(path) 
    - we used for method for iterating all files from files list
    - we try to check if objects are file or folder by using os.path.isfile(os.path.join(path,file)) method and it will ignore all folders in our directory.
    - we try to split file name and its extension by using split method and name them as variables.
    - There is sometimes hidden files like DS_Store file,therefore we create if statement for ignoring this files by returning continue.
    - then we try to check if our folder name exist with extension name or not,if yes then we move files into folders as per their extensions using shutil method.If not then we use os.makedirs method for creating folders as per extension names and then move files into the folders again.
    - in the last we just used tkinter.messagebox.showinfo method to show if files were organized or not as a success message
