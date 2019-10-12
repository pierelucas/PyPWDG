# PyPWDG - Random Password Generator
#
# Creation:    12.10.2019
# Last Update: 12.10.2019
#
#
# MIT License
#
# Copyright (c) 2019 by PiereLucas
# https://github.com/pierelucas
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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
