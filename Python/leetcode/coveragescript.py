import os

currentDirectory = os.getcwd()

path = os.path.split(currentDirectory)
if path[len(path)-1] == "Python":
    os.chdir(currentDirectory)
else:
    os.chdir(currentDirectory+"/Python")

os.system("python -m unittest")
os.system("coverage run -m unittest")
os.system("coverage report")
os.system("coverage html")

