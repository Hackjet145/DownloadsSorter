import os 
import shutil
import pathlib




class sorter:
    user=os.getlogin()
    old_path = f"C:/Users/{user}/Downloads"
    new_path = "D:/Downloads Sorted"

#checking folder
    def check_folder(new_path):
        checkfolder = os.path.isdir(new_path)
        if checkfolder is True:
            print("Directory Set")
        else:
            print("Setting Up Directory")
            os.mkdir(new_path)
            print(".........\nDirectory's Setting Done")

        folderfolder = os.path.isdir(new_path+"/"+"Folder")

        if folderfolder is True:
            print("All neccesary folders Present")
        else:
            os.mkdir(new_path+"/"+"Folder")
            print("All neccesary folders created")
    check_folder(new_path)

#List Directory And Get Extension And Copying Function
    def list_make(new_path,old_path): 
        files = os.listdir(old_path)
        for x in range(0,len(files)):
            file_extension = pathlib.Path(files[x]).suffix
            path = os.path.join(new_path,file_extension)
            is_exist = os.path.exists(path)
            folder_check = os.path.isdir(old_path+"/"+files[x])
            if folder_check is True:
                shutil.move(old_path +"/"+files[x],new_path+"/"+"Folder")
            else:
                if is_exist is True:
                    shutil.move(old_path +"/"+files[x],new_path+"/"+file_extension)
                else:
                    os.mkdir(path)
                    shutil.move(old_path +"/"+files[x],new_path+"/"+file_extension)

    list_make(new_path,old_path)             
