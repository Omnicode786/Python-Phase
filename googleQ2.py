def pig_latin(text):
#   say = ""
  say = []
  # Separate the text into words
  words = text.split()
  for word in words:
    # Create the pig latin word and add it to the list
    # abetter approach would be to use say as a list
    # so to do that use append
    # say += word[1:] + word[0] + "ay "
    pigway = word[1:] + word[0] + "ay"
    say.append(pigway)

    # Turn the list back into a phrase
  return " ".join(say)
    
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"