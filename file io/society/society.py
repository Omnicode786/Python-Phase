# our local university's Raptors fan club maintains a register of its active members on a .txt document. Every month they update the file by removing the members who are not active. You have been tasked with automating this with your Python skills.
# Given the file currentMem, Remove each member with a 'no' in their Active column. Keep track of each of the removed members and append them to the exMem file. Make sure that the format of the original files in preserved. (Hint: Do this by reading/writing whole lines and ensuring the header remains )
# Run the code block below prior to starting the exercise. The skeleton code has been provided for you. Edit only the cleanFiles function.

import os

os.chdir(r"E:\Programming\Google  Python\Python-Phase\file io")


memReg = "memREG.txt"
exReg = "exREG.txt"

def addinactive(new, old):
    with open(new, "r+") as reg:
        member = reg.readlines()
        for index,  line in enumerate(member, start=1):
            if "no" in line:
                print(f"The member on line {index} is inactive")
                with open(old, "a+") as exmem:
                    exmem.write(line)
                    print("Written succesfull")
                

def cleanFile(new):
    with open(new, "r+") as filer:
        lines = filer.readlines()
    with open(new, "w+") as filer:
        for line in lines:
            if "no" not in line:
                filer.write(line)


addinactive(memReg, exReg)
cleanFile(memReg)