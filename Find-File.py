import os, shutil

def lookandcopy(filetofind):
    for root, dirs, files in os.walk('.'):
        for filename in files:
            if filetofind in filename:
                print ("File Found!: ")
                try:
                    shutil.copy(os.path.abspath(root + '/' + filename), './')
                except shutil.SameFileError:
                    pass

search = input("Enter Filename To Find: ")
lookandcopy(search)           
input("Press Enter to Exit")