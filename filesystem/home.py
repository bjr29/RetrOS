import os, subprocess

def run():
    command = input("\033[1;31;40mHome>\033[0;37;40m")

    if(command[-3] == ".py"):
        subprocess.call(command, shell = True)
    else:
        subprocess.call(command+".py", shell = True)
    
    run()
