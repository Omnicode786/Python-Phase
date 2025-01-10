import os
import itertools
pasword = input("Enter your pasword: ")
keys = [ 
 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
 'u', 'v', 'w', 'x', 'y', 'z']

found = False
atempts = 0
print("Attacking...")

for length in range(1,len(pasword)+1):
    for guess in itertools.product(keys,repeat=length):
        guessedpass = "".join(guess)
        atempts +=1
        if guessedpass == pasword:
            found = True
            print(f"\nPassword found: {guessedpass} in {atempts} attempts.")
            break
    if found:
        break

# If the password was not found after all attempts
if not found:
    print("\nPassword not found.")
