import shutil
import psutil
import os
from time import sleep
def spaceteller(directory):
    total,used, free = shutil.disk_usage(directory)
    freepercent = (free/total)*100
    usedpercent = (used/ total)*100
    print(f"{(freepercent):.2f}")
    print(f"{(usedpercent):.2f}")
    total = total / (1024**3)
    free = free / (1024**3)
    used = used / (1024**3)
    print(f"The total space in the drive is: {total:.2f}")
    print(f"The used space in the drive is: {used:.2f}")
    print(f"The free space in the drive is: {free:.2f}")


def cpuusageteller(n):
    for i in range (0, n+1):
        print(psutil.cpu_percent(interval=0.1))
        sleep(0.5
        )
        os.system('cls')


spaceteller(r"E:\\")
input("Enter something to continue: ")
os.system('cls')
cpuusageteller(50)


'''To determine if automating a process would save labor time, use the following formula:

Time_to_automate < (time_to_perform * amount_of_times_done)

Lets break down this formula and look at an example:

# A banking company is looking to automate one of its internal processes that takes about 40 minutes each week to complete. The automation process will take 10 hours total to complete. How many weeks will it be before the banking company begins to save time on the process and automation would be worthwhile?


'''