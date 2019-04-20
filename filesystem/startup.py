print("LOADING...")
print("LOADING: BIOS...")
# Imports
import json
print("LOADING: FILES...")
import filesystem, autorun, os, time

print("Loading Complete\n")


print("AUTORUN: ")
autorun.run()


time.sleep(2)
os.system("cls")
print(">==============================================<")
print("|                                              |")
print("|    Welcome to RetrOS 0.1 by Ben Rushworth    |")
print("|                                              |")
print(">==============================================<\n")
print("Use 'help' for commands\n")
filesystem.locations().home()
