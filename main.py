import random
import string
import sys

banner_txt = """
[+] RANDOM PASSWORD GENERATOR [+]
---------------------------------
       Coded by Pierelucas
"""

menu_txt = """
[1] Lowercase
[2] Upper and Lowercase
[3] Letters and Digits
[4] Letters and Digits and Specialchars
[Else] Exit"""

def out():
    print(banner_txt)
    print(menu_txt)
    print()

def inp():
    try:
        choice = str(input("[+] Which option Number » "))
        stringlen = int(input("[+] Password length » "))
        value = int(input("[+] How many Passwords » "))
        print()
        return choice, stringlen, value
    except ValueError:
        print("Wrong Value")
        sys.exit(0)

def rnd_lowercase(*, stringlen, value):
    for i in range(value):
        letters = string.ascii_lowercase
        s = ""
        pwd = s.join(random.choice(letters) for i in range(stringlen))
        print(pwd)

def rnd_upperandlower(*, stringlen, value):
    for i in range(value):
        letters = string.ascii_letters
        s = ""
        pwd = s.join(random.choice(letters) for i in range(stringlen))
        print(pwd)

def rnd_stringdigit(*, stringlen, value):
    for i in range(value):
        letters = string.ascii_letters + string.digits
        s = ""
        pwd = s.join(random.choice(letters) for i in range(stringlen))
        print(pwd)

def rnd_stringspecial(*, stringlen, value):
    for i in range(value):
        letters = string.ascii_letters + string.digits + string.punctuation
        s = ""
        pwd = s.join(random.choice(letters) for i in range(stringlen))
        print(pwd)

def run():
    out()
    choice, stringlen, value = inp()

    if choice == '1':
        rnd_lowercase(stringlen=stringlen, value=value)
    elif choice == '2':
        rnd_upperandlower(stringlen=stringlen, value=value)
    elif choice == '3':
        rnd_stringdigit(stringlen=stringlen, value=value)
    elif choice == '4':
        rnd_stringspecial(stringlen=stringlen, value=value)
    else:
        print("All Systems Down")
        sys.exit(0)


# TO BE CONTINUED ...
run()
