# “r”  open for reading (default)

# “w”  open for writing, truncating the file first

# “x”  open for exclusive creation, failing if the file already exists

# “a”  open for writing, appending to the end of the file if it exists

# “+”  open for both reading and writing


# by default python uses uft-8 encoding but best practice is to declare them


# One thing to be aware of is that Python treats text and binary files differently. Because Python is cross-platform, it tries to automatically handle different ASCII line endings. If you’re processing a binary file, make sure to open it in binary mode so Python doesn’t try to “fix” newlines in a binary file.