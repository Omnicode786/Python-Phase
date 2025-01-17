import sys
import re

logfile = "module4\processlog\logs.txt"
username = {}
with open(logfile) as f:
  for line in f:
    if "CRON" not in line:
      continue
    pattern = r"\((\w+)\)"
    result = re.search(pattern, line)
    lines = line.strip()
    withoutspace = "".join(lines.split()) 
    print(withoutspace) # the split function removes alll white spaves
    name = result.group(1)
    username[name] = username.get(name, 0) +1
    print(f"User: {result.group(1)}")
# In regular expressions, when you define a pattern with parentheses (e.g., (\w+)), you're telling Python that you want to capture a specific portion of the string. This is often referred to as a capture group. A capture group stores a part of the matched string that you can later reference or extract.
print(username)

# The strip() function in Python is used to remove leading and trailing whitespace characters from a string