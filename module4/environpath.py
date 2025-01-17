# echo $PATH
# /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
# cat variables.py
#!/usr/bin/env python3
import os
print("HOME: " + os.environ.get("HOME", ""))
print("SHELL: " + os.environ.get("SHELL", ""))
print("FRUIT: " + os.environ.get("FRUIT", ""))
# ./variables.py 
# export FRUIT=Pineapple
# ./variables.py 

#  this is to be run on below terminal

#  envi vairables are simply anpotjher source of informatonenv
