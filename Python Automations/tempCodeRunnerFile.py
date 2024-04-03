
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
    moveFiles(source_folder,destinationFolder=django_tutorial_folder,searchKeyword='Django')
except:
    print(KeyError)    