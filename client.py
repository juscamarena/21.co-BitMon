from random import randint
from two1.wallet import Wallet
from two1.bitrequests import BitTransferRequests
import hashlib
from getpass import getpass
from requests import get

wallet = Wallet()
requests = BitTransferRequests(wallet)

srv = "http://21.browntech.space:8383/"
print("Welcome to BitMon, Bit-Sized Monsters!")
answer = int(input("Would you like to login[1] or register[2]?: "))
ipaddr = get('https://api.ipify.org').text

if answer == 1:
    user = input("User name: ").lower()
    password = getpass("Password: ").encode()
    password = hashlib.md5(password).hexdigest()
    srv += 'login?user={0}&pass={1}&ipaddr={2}'.format(user,password,ipaddr)
    response = requests.get(url=srv)
    print(response.text)

if answer == 2:
    user = input("User name: ").lower()
    if not user.isalnum() or not 6 <= len(user) <= 12:
        print("Please enter only numbers and letters, between 6 and 12 characters.")
        exit() 
    password = getpass("Password: ")
    if not password.isalnum() or not 8<= len(password) <= 40:
        print("Please enter only numbers and letters, between 8 and 40 characters.")
        exit()
    confirm = getpass("Re-type Password: ")
    if not confirm == password:
        print("Passwords do not match!")
        exit()
    password = password.encode()
    password = hashlib.md5(password).hexdigest()
    srv += 'register?user={0}&pass={1}&ipaddr={2}'.format(user,password,ipaddr)
    response = requests.get(url=srv)
    print(response.text)
    exit()


while True:
    srv = "http://21.browntech.space:8383/"
    print("What would you like to do?")
    choice = int(input('''
==============================
-----------Main Menu----------
==============================
1 - Select Starter
2 - Log out
==============================

Your choice: 
'''))
    if choice == 1:
        while True:
            starter_select = int(input('''
========================================================
-----------------Choose a starter-----------------------
========================================================
Stats    |  [1]Yursba   |  [2]Grumsden |  [3]Hermyle
--------------------------------------------------------
Type     | Nova         | Wind         | Earth
Attack   | 17           | 15           | 20
Defense  | 12           | 13           | 5
========================================================
Your choice: 
'''))
            if starter_select == 1:
                srv = 'http://21.browntech.space:8383/selectstarter?user={0}&pass={1}&ipaddr={2}&starter=Yursba'.format(user,password,ipaddr)
                response = requests.get(url=srv)
                print(response.text)
                break
            if starter_select == 2:
                srv = 'http://21.browntech.space:8383/selectstarter?user={0}&pass={1}&ipaddr={2}&starter=Grumsden'.format(user,password,ipaddr)
                response = requests.get(url=srv)
                print(response.text)
                break
            if starter_select == 3:
                srv = 'http://21.browntech.space:8383/selectstarter?user={0}&pass={1}&ipaddr={2}&starter=Hermyle'.format(user,password,ipaddr)
                response = requests.get(url=srv)
                print(response.text)
                break
            else:
                print("Please make a valid choice!\n")
    if choice == 2:
        print("Goodbye!")
        exit()
