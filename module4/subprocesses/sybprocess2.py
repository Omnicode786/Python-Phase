import subprocess

# Using Popen for asynchronous behavior: 

process = subprocess.Popen(['timeout', '5'])

message_1 = "The process is running in the background..."

# Give it a couple of seconds to demonstrate the asynchronous behavior

import time

time.sleep(2)

# Check if the process has finished

if process.poll() is None:
	
# If the process is still running, poll() returns None.
# If the process has finished, poll() returns the exit code (usually 0 for successful completion).
	message_2 = "The process is still running."

else:

	message_2 = "The process has finished."

print(message_1, message_2)
