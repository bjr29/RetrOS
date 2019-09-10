print("LOADING...")
print("LOADING: BIOS...")
# Imports
import json
print("LOADING: FILES...")
print("LOADING: subprocess")
import subprocess
print("LOADING: filesystem")
import filesystem
print("LOADING: os")
import os
print("LOADING: time")
import time
print("LOADING: sys")
import sys
print("LOADING: autorun")
import autorun

print("Loading Complete\n")


print("AUTORUN: ")
autorun.run()

time.sleep(1)
subprocess.call("welcome.py", shell = True)
