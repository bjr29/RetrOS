import os

def pythonFile(Name):
    f = open(Name + ".py", "r")
    contents = f.read()
    os.system("cls")
    print(contents)

name = input("Name of file: ")
pythonFile(name)
