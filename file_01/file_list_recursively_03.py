import os

def change_directory():
    os.chdir("../")

def top_down_walk():
    for dirpath, dirnames, files in os.walk("Documents"):
        print("Directory: ", dirpath)
        print("the list of directories")
        for dirname in dirnames:
            print(dirname)
        print("the list of files")
        for file in files:
            print(file)
        print()



if __name__ == "__main__":
    change_directory()
    top_down_walk()
