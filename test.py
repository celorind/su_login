#! /usr/bin/python3

import requests
from sys import exit
from getpass import getpass

def main():
    # input params
    # id = input("ID: ")
    # passwd = getpass("Password: ")
    payload = {'uid': input("ID: "), 'pwd': getpass("Password: ")}

    try:
        print("Attempting Login ACSU Network...")
        r = requests.post("https://login.shinshu-u.ac.jp/cgi-bin/Login.cgi", data=payload, timeout=3)
        with open("response.log", "wb") as f:
            f.write(r.content)
    except requests.exceptions.Timeout as e:
        print("Timed out:", e)
    except Exception as e:
        print(e)
        exit(-1)


if __name__ == "__main__":
    main()
