#! /usr/bin/python3

import requests
from sys import exit

def main():
    id = input("ID? ")
    passwd = input("Password? ")

    payload = {'uid': id, 'pwd': passwd}
    r = requests.post("https://login.shinshu-u.ac.jp/cgi-bin/Login.cgi", params=payload)
    print(r.url)
    if r.status_code == requests.codes.ok:
        print("Login Sucess!")
    else:
        print("Login Failed!!")
        exit(-1)

if __name__ == "__main__":
    main()
