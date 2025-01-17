import os
import sys

filename = sys.argv[1]

if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("The file is now created")
else:
    print("Error the file already exists")
    sys.exit(404)
    # in order to check the exit status we can use $LASTEXITCODE 


