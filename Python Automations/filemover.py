import os
import shutil


def moveFiles(sourceFolder,destinationFolder,searchKeyword : str):
    file_list = os.listdir(sourceFolder)
    for file_name in file_list:
        if file_name.endswith(f'{searchKeyword}'):
            file_path = os.path.join(source_folder,file_name)
            shutil.move(file_path, destinationFolder) 
    

#Define the source and destination folders

source_folder = "C:/Users/USER/Downloads/"
anime_folder = "C:/Users/USER/Desktop/Movies/Anime"
unilag_folder = "C:/Users/USER/Desktop/UNILAG"
django_tutorial_folder = "C:/Users/USER/Desktop/Coding/Django Projects/Django Tutorials"
flutter_tutorial_folder = "C:/Users/USER/Desktop/Coding/Flutter/Flutter Tutorials"
unity_tutorial_folder = "C:/Users/USER/Desktop/Coding/Unity/Unity Tutorials"

#Get a list of all files in the source folder
# file_list = os.listdir(source_folder)

# #Loop through the files and move the pictures to the picture folder
# for file_name in file_list:
#     if file_name.__contains__("Django") or file_name.__contains__("Python"):
#         file_path = os.path.join(source_folder,file_name)
#         shutil.move(file_path, django_tutorial_folder) 
try:
    moveFiles(source_folder,unity_tutorial_folder,searchKeyword='.fbx')
except:
    print("Error")    