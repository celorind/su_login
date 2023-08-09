#! /usr/bin/python3

import requests
from sys import exit

def main():
    # id = input("ID? ")
    # passwd = input("Password? ")
    id = "12a3456b"
    passwd = "blahblahblah"

    payload = {'uid': id, 'pwd': passwd}
    r = requests.post("http://httpbin.org/post", params=payload)
    print(r.url)
    #print(r.json())
    if r.status_code == requests.codes.ok:
        print("Login Sucess!")
    else:
        print("Login Failed!!")
        exit(-1)

if __name__ == "__main__":
    main()
