import random
import string
import re
import os
from colorama import Fore, init
import shutil
import pyperclip

init(autoreset=True)

def x1(y):
    z = 0
    if len(y) >= 8:
        z += 1
    if any(c.islower() for c in y):
        z += 1
    if any(c.isupper() for c in y):
        z += 1
    if any(c.isdigit() for c in y):
        z += 1
    if any(c in string.punctuation for c in y):
        z += 1
    
    if z == 5:
        return "Ultra Secure", Fore.CYAN
    elif z == 4:
        return "Secure", Fore.GREEN
    elif z == 3:
        return "Normal", Fore.YELLOW
    else:
        return "Insecure", Fore.RED

def y2(a=8, b=True, c=True, d=True):
    e = string.ascii_lowercase
    if b:
        e += string.ascii_uppercase
    if c:
        e += string.digits
    if d:
        e += string.punctuation
    f = ''.join(random.choices(e, k=a))
    
    print(Fore.MAGENTA + f"Generated password: {f}")  
    g, h = x1(f)
    print(h + f"Strength of this password: {g}")
    
    pyperclip.copy(f)
    print(Fore.YELLOW + "Password has been copied to the clipboard. Please paste it where needed.")
    
    print(Fore.YELLOW + "Please copy your password now before continuing.")
    
    del f

def z3(i):
    if len(i) < 8:
        print(Fore.RED + "This password is too short. The minimum recommended length is 8 characters.")
        return False
    if re.search(r'\s', i):
        print(Fore.RED + "The password should not contain spaces.")
        return False
    return True

def a4():
    j = input(">> Enter a password to check: ").strip()
    g, h = x1(j)
    print(h + f"The password '{j}' is classified as: {g}")
    input("\n>> Press Enter to return to the menu.")

def b5():
    while True:
        try:
            k = int(input(">> Password length (minimum 1, recommended 8): "))
            if k < 1:
                print(Fore.RED + "The length must be greater than 0.")
                continue
            break
        except ValueError:
            print(Fore.RED + "Please enter a valid number for the length.")

    if k < 8:
        print(Fore.YELLOW + "\n[WARNING] A short password is potentially dangerous.")
        l = input("Are you sure you want to continue? (Y/N): ").strip().lower()
        if l not in ['y', 'yes']:
            print(Fore.MAGENTA + "Password creation canceled.")
            return

    b = input(">> Include uppercase letters? (Y/N): ").strip().lower() in ['y', 'yes']
    c = input(">> Include digits? (Y/N): ").strip().lower() in ['y', 'yes']
    d = input(">> Include special characters? (Y/N): ").strip().lower() in ['y', 'yes']
    
    y2(k, b, c, d)

    input("\n>> Press Enter to return to the menu.")

def c6():
    m = input(">> Enter the password file name (.txt): ").strip()
    if not os.path.isfile(m):
        print(Fore.RED + f"[ERROR] File '{m}' not found.")
        return
    
    with open(m, 'r') as n:
        o = n.readlines()
    
    for p in o:
        p = p.strip()
        if p:
            g, h = x1(p)
            print(h + f"The password '{p}' is classified as: {g}")
    
    input("\n>> Press Enter to return to the menu.")

def d7():
    t = " MENU "
    w = shutil.get_terminal_size().columns
    wd = w if w > 50 else 50

    print(Fore.GREEN + "-" * wd)
    print(Fore.YELLOW + t.center(wd))
    print(Fore.GREEN + "-" * wd)
    
    print(Fore.CYAN + "[1] Check a password".center(wd))
    print(Fore.CYAN + "[2] Generate a password".center(wd))
    print(Fore.CYAN + "[3] Check a password file".center(wd))
    print(Fore.RED + "[Q] Quit".center(wd))
    
    print(Fore.GREEN + "-" * wd)

def e8():
    os.system('cls' if os.name == 'nt' else 'clear')

def f9():
    while True:
        e8()
        d7()
        q = input(">> Choice: ").strip().lower()
        if q == '1':
            a4()
        elif q == '2':
            b5()
        elif q == '3':
            c6()
        elif q == 'q':
            print(Fore.MAGENTA + "[INFO] Exiting the program.")
            break
        else:
            print(Fore.RED + "[ERROR] Invalid choice. Try again.")

if __name__ == "__main__":
    f9()
