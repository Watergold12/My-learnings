import os

dir_path = r"C:\Users\HP 15-AU109NE\Desktop\AAV"  # replace with the directory you want to list

files_and_dirs = os.listdir(dir_path) # os.listdir() lists the directory

for item in files_and_dirs:
    print(item)
