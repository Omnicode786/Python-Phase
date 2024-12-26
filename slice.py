name = "Muzammil"

print(name[1:7])
print(name[1:9])
print(name[1:8])
print(name[-1:])
print(name[-8:])
print(name[-8:-2])


# If your index is negative, Python counts back from the end of the string instead of the beginning.

for n in range(10):
  print(n+n)
for n in range(0,18+1,2):
  print(n*2)
for n in range(18+1):
  print(n**2)
for n in range(19):
    if n % 2 == 0:
        print(n)