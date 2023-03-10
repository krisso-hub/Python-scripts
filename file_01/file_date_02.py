from datetime import datetime
import os

def display_current_directory():
    cwd= os.getcwd()
    print("the current working directory is: ", cwd)

def change_directory_one_step_up():
    os.chdir("../")
    

def format_datetime(timestamp):
    utc_timestamp = datetime.utcfrontimestamp(timestamp)
    formated_date = utc_timestamp.strftime("%d %b %Y %H %M %S")
    return formated_date

def display_entry_in_directory(directory):
    with os.scandir(directory) as entries:
        for entry in entries:
            print("name: ", entry.name)
            info = entry.stat()
            print("Creation Time: ", info.st_ctime)
            print("Last Access Time: ", info.st_atime)
            print("Size:",info.st_size )

def display_directory(directory):
    with os.scandir(directory) as entries:
        for entry in entries: 
            if entry.is_dir():
                print("Directory Name is:  ", entry.name)

def display_flies(directory):
    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_file():
                print("File Name is: ", entry.name)


if __name__ == "__main__" :
    display_current_directory()
    change_directory_one_step_up()
    display_current_directory()
    display_entry_in_directory("aws")
    display_directory("aws")
    display_flies("aws")