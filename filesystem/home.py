print("LOADING...")
import os, time, sys, subprocess
os.system("cls")

def run():
    command = str(input("\033[1;31;40mHome>\033[0;37;40m"))

    if(command == "shutdown"):
        sys.exit()
        
    elif(command == "reboot")or(command == "restart"): # Quick commands
        subprocess.call("startup.py", shell = True)
        
    elif(command == "signout"):
        subprocess.call("welcome.py", shell = True)
        

    else: # Run other Files
        subprocess.call(command + ".py", shell = True)

    run()
