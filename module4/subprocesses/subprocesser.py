# # Title: Using Subprocesses to Run System Commands in Python

# # Now, let's break down the video into key points. I'll guide you.  

# # The video starts by talking about how Python interacts with the operating system. What examples are used?
# # Next, the video introduces the subprocess module. What is its purpose?
# # The video demonstrates the subprocess.run function. What does this function do, and what kind of object does it return?
# # Can you tell me more about the CompletedProcess object? What information does it hold?


# Subprocesses are a way to call and run other applications from within Python
# Python subprocess can launch processes to: 

# Open multiple data files in a folder simultaneously. 

# Run external programs. 

# Connect to input, output, and error pipes and get return codes.



# subprocess.run()
# The .run() command is the recommended approach to invoking subprocesses. It runs the command, waits for it to complete, then returns a CompletedProcess instance that contains information about the process.

# Purpose: This function is the core of the subprocess module. It allows you to run system commands directly from your Python code. Think of it as a bridge between your Python script and your operating system's command line.
# How it works: You provide the command you want to run as a list to the function. The first item in the list is the command itself (like 'date' or 'sleep'), and any following items are arguments for that command.
# What it returns: It returns a CompletedProcess object, which holds information about the command's execution.
# CompletedProcess Object

# Purpose: This object is like a report card for the command you ran. It tells you if the command was successful and gives you details about the execution.
# Key Attributes:
# returncode: This attribute tells you if the command was successful (0 usually means success) or if there were errors (non-zero values represent different error codes).



import subprocess

# Use /T to display the date without prompting for input
result = subprocess.run(["date", "/T"], capture_output=True, text=True, shell=True)

# Print the command output
print("Command Output:")
print(result.stdout)

# Print the return code
print("\nReturn Code:", result.returncode)


# result = subprocess.run(["sleep", "2"], capture_output=True, text=True, shell=True)
result = subprocess.run(["timeout", "2"], capture_output=True, text=True, shell=True)

print(result)

#  these are system commands and not python modules etc mind you so sleep above does not work as it is from unx etc
#  basicallty the run function runs the inside function let's say if it was sleep then it would run that first and then run the parent function and give us the result