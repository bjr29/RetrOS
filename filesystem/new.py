def pythonFile(Name):
    f = open(Name+".py", "w+")
    f.write('print("Hello World!")')
    f.close()

name = input("Name of file: ")
pythonFile(name)
