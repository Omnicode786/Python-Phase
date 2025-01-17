# Capturing Output: To work with the output of a system command within your Python script, you need to instruct the run function to capture it. This is done by setting the capture_output parameter to True.
# Storing Output: The output is stored within a CompletedProcess instance, which you typically assign to a variable (e.g., result = subprocess.run(["ls", "-l"], capture_output=True)).
# Accessing Output: The captured output is accessible through the stdout attribute of the CompletedProcess instance (e.g., print(result.stdout)).
# Byte Arrays: Initially, the captured output is a byte array, not a regular Python string. This is indicated by the b prefix before the output.
# Decoding Output: To convert the byte array into a usable string, you can use the decode() method with the appropriate encoding (UTF-8 is common). For example: output_string = result.stdout.decode("utf-8").
# Standard Error: The stderr attribute captures any error messages written to the standard error stream during command execution.


import subprocess
result = subprocess.run(["nslookup", "8.8.8.8"],capture_output=True)
print(result)
#  the b represents that it iss in array bytes

#  it is dns to 

result = subprocess.run(["cmd","/c","del","filedoesnotexist"], capture_output=True)
# cmd is the command shell for Windows.
# /c tells cmd to execute the following command (in this case, del filedoesnotexist), and then terminate.
# capture_output=True captures both stdout and stderr so you can see the output and any errors.

print(result)
print(result.returncode)
print(result.stderr)
print(result.stdout)



