import os, sys
os.system("cls")

INPUT = input("Are you sure you want to shut down? Y/N")
if(INPUT == "Y" or INPUT == "y"):
    print("SHUTTING DOWN...")
    sys.exit()
else:
    print("Shutdown Stopped")
