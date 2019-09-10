import sys, os

while True:
    os.system("cls")

    file = open("notesTxt.txt", "r")
    content = file.read()

    print("== Notes ==\n\n" + content + "\n")
    lineCount = sum(1 for line in open("notesTxt.txt"))
    file.close()

    Input = str(input("(N) New note/ (WIP) (D) Delete a note/ (E) Exit the program: "))
    Input = Input.lower()


    if(Input == "n"):
        file = open("notesTxt.txt", "a")

        note = str(input("New Note: "))
        file.write(str(lineCount + 1) + ". " + note + "\n")
        file.close()


    elif(Input == "d"):
        noteIndex = int(input("Index of note: "))
        i = 1

        file = open("notesTxt.txt", "r+")
        for line in file:
            if(i != noteIndex):
                file.write(line)
            i += 1


    elif(Input == "e"):
        break
