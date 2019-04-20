import os

def pythonFile(Name):
    os.remove(Name)

name = input("Name of file: ")
INPUT = input("Are you sure you want to delete " + name + ".py" + " Y/N: ")

if(INPUT == "Y" or INPUT == "y"):
    pythonFile(name + ".py")
