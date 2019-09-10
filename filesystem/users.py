detailsSplit = ","
detailsStartEnd = "."

def createAccount(username, password):
    f = open("usersTxt.txt", "a")
    f.write("\n" + detailsStartEnd + username + detailsSplit + password + detailsStartEnd)
    f.close()


def checkAccount(username, password):
    f = open("usersTxt.txt", "r")
    lines = f.readlines()

    for line in lines:
        foundUsername = line.find(detailsStartEnd + username + detailsSplit)
        foundPassword = line.find(detailsSplit + password + detailsStartEnd)

        if(foundUsername != -1):
            if(foundPassword != -1):
                return 0 # Correct Username & Password
            return 1 # Incorrect Password
    return 2 # No Account
