#this is a package
from random import *


#Create the list of words you want to choose from.
threeSyllables = ["I like food","Girls Who Code", "We eat food", "We have quotes", "Relaxing", "We need food", "Hue Hue Hue"]
fiveSyllables= ["I have been vacuumed", "That's plagerism","These girls are coding", "We need yoga day", "HE HE HE HE HE" ]

#Generates a random integer.
"""
if threeSyllables == 1:
    print(threSyllables[1])
print(x)
print(y)
print(x)
"""
for i in range(1):
    x = randint(0, len(threeSyllables)-1)
    print(threeSyllables[x])
    for i in range(1):
        y = randint(0, len(fiveSyllables)-1)
        print(fiveSyllables[y])
    for i in range(1):
        x = randint(0, len(threeSyllables)-1)
        print(threeSyllables[x])
