import glob
import os

def change_directory_one_step():
    os.chdir("../")

def display_current_directory():
    cwd = os.getcwd()
    print("my current directory is: ", cwd)

def display_all_pdf():
    pdf_files = glob.glob("*.pdf")
    print(pdf_files)

def find_files_with_coverName():
    filter_items = glob.glob("*cover*")
    print(filter_items)

def find_files_in_subdir():
    for files in glob.iglob("**/*cover*", recursive = True):
         print(files)


if __name__ == "__main__":
    change_directory_one_step()
    display_current_directory()
    # display_all_pdf()
    # find_files_with_coverName()
    find_files_in_subdir()
    