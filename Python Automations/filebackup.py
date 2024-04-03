import os
import shutil

#Define source and destination folders
source_folder = "C:/Users/User/Downloads"
backup_folder = "G:/DEK/" 

#Get a list of all files in the source folder
file_list = os.listdir(source_folder)

# Loop through the files and copy them to the backup folder
for file_name in file_list:
    if file_name.startswith("A"):
        file_path = os.path.join(source_folder,file_name)
        shutil.copy(file_path,backup_folder)