
import os 

cwd = os.getcwd()
print(cwd)
path = os.path.split(cwd)
print(path)

dir =os.path.dirname(cwd)
print(dir)

base =os.path.basename(cwd)
print(base)