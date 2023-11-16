#! /usr/bin/python3

import requests
from sys import exit
from getpass import getpass

SUCESS_TEXT = "Login Success"

def main():
    try:
        payload = {'uid': input("ID: "), 'pwd': getpass("Password: ")}

        print("Attempting Login to ACSU Network...")
        r = requests.post("https://login.shinshu-u.ac.jp/cgi-bin/Login.cgi", data=payload, timeout=3)
        if SUCESS_TEXT in r.text:
            print("Login Success!")
            exit()
        else:
            print("Login Failed!")
            exit(1)
            print("Incorrect ID or password!.")
    
    except requests.exceptions.ConnectionError as e:
        print("Login Failed!")
        print("HTTP connection error.")
        exit(2)

    except requests.exceptions.Timeout as e:
        print("Login Failed!")
        print("HTTP request timed out.")
        exit(3)

    except KeyboardInterrupt as e:
        print("\nAbort")
        exit(0)

    except Exception as e:
        print("Login Failed!")
        print(e)
        exit(-1)


if __name__ == "__main__":
    main()
