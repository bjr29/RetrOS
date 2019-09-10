import users, filesystem, time, os
os.system("cls")
correct = False

print("\033[2;32;40mWelcome!\n")
print("To create a new account type in a username you'd want to use and it's password to use. This will be changed in later versions.\n")
print("\033[2;31;40mUse real password at risk, passwords are not protected!\033[2;32;40m\n")

while not correct:
    IN_accountName = str(input("\033[2;32;40mACCOUNT:\033[0;37;40m\n"))
    IN_accountPassword = str(input("\033[2;32;40mPASSWORD:\033[0;37;47m\n"))
    print("\033[0;37;40m")

    login = users.checkAccount(IN_accountName, IN_accountPassword)

    if(login == 0):
        correct = True

    elif(login == 1):
        print("Incorrect Password")

    else:
        print("\033[2;31;40mNo Account Found!\n")
        createAccount = str(input("\033[2;32;40mWould you like to create a new account? Y/N:\033[0;37;40m"))
        createAccount.lower()

        if(createAccount == "y"):
            users.createAccount(IN_accountName, IN_accountPassword)
            correct = True


os.system("cls")

import welcomeMsg
welcomeMsg.show()

filesystem.locations().home()
