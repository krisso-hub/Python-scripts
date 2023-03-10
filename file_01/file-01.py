
import os
def display_cwd():
    cwd = os.getcwd()
    print("the current working directory is", cwd)

def change_dir_up_one_level():
    os.chdir("../")

def display_entry_in_directory(directory):
    with os.scandir(directory) as entries:
        for entry in entries:
            print(entry.name)



if __name__ == "__main__" :
    change_dir_up_one_level()
    display_cwd()
    display_entry_in_directory("files/")
    
