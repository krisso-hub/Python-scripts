# file_path = "fib.py"
# open_file = open(file_path, "r")
# text = open_file.readlines()
# print(len(text))
# open_file.close()

# with open(file_path, "r") as open_file:
#     text = open_file.read()
#     print(len(text))

# text = '''export stage=prod
# export Table_Id=Token_storage
# '''
# with open(".envrc","w") as opened_file:
#     opened_file.write(text)

import pathlib

path = pathlib.Path("\Users\nd\OneDrive\Documents\Python Scripts\learning python\fib.py")
print(path.read_text)
