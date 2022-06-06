import random
random_num = random.randint(0, 100)
print(random_num)

rand = random.random()
print(rand)

lst = ["star","tv9","sony","aaj"]
choice = random.choice(lst)
print(choice)

import datetime
print("The time is:",datetime.datetime.now())

import pyperclip
pyperclip.copy("Hello World.")
pyperclip.paste()
"""
from emoji import emojize
print(emojize(":thumbs_up:"))
print(emojize(":laugh:"))
"""

