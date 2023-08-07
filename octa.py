#!/usr/bin/env python3



import time
import os

print("""

░█████╗░░█████╗░████████╗░█████╗░██╗░░░██╗███████╗░░░░░░░█████╗░░██████╗
██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██║░░░██║██╔════╝░░░░░░██╔══██╗██╔════╝
██║░░██║██║░░╚═╝░░░██║░░░███████║╚██╗░██╔╝█████╗░░█████╗██║░░██║╚█████╗░
██║░░██║██║░░██╗░░░██║░░░██╔══██║░╚████╔╝░██╔══╝░░╚════╝██║░░██║░╚═══██╗
╚█████╔╝╚█████╔╝░░░██║░░░██║░░██║░░╚██╔╝░░███████╗░░░░░░╚█████╔╝██████╔╝
░╚════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝░░░░░░░╚════╝░╚═════╝░
""")
print("""
[1] Continue with Setup
[2] I have already done Setup
""") 
setup = input("[?]:")
if setup == '1':
    name = input(str("Please enter your User Name to be Displayed: "))
    pas = input(str("Please enter your Password to Login: "))

    
    with open('user/username.txt','w') as f:
        f.writelines(name)
    
    
    with open('user/password.txt','w') as f:
        f.writelines(pas)
    print("Setup Complete !!")
    input("Please Enter to close Window: ")
    os.system("python octa.py")

if setup == '2':
    login_pass = open('user/password.txt')
    login_name = open('user/username.txt')
    l_p = login_pass.read()
    l_n = login_name.read()

    while True:
        login = input(str("Please Enter the Password to "+l_n+": "))
        if login == l_p:
            os.system("python home.py")
            break
        else:
            print("Wrong Password!")