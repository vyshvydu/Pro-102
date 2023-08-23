import os
import shutil

from_dir="C:\Users\vasan\OneDrive\Desktop\PRO-102"
to_dir="C:\Users\vasan\OneDrive\Desktop\Documents Files"

list_of_files=os.listdir(from_dir)
print(list_of_files)
for file_name in list_of_files:

    name, extension = os.path.splitext(file_name)
    #print(name)
    #print(extension)

    if extension == '':
        continue
    if extension in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:

        path1 = from_dir + '/' + file_name                       # Example path1 : Downloads/ImageName1.jpg        
        path2 = to_dir + '/' + "Image_Files"                     # Example path2 : D:/My Files/Image_Files      
        path3 = to_dir + '/' + "Image_Files" + '/' + file_name   
        if os.path.exists(path2)
        print("Moving"+file_name+"....")

        shutil.move(path1,path3)

        else:
            os.makedirs(path2)
            print("Moving"+file_name+"....")
            shutil.move(path1,path3)