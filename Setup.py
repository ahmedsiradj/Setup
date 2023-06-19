#!/usr/bin/python

import subprocess


def installer():
    with open('resourses/go.txt','r') as file:
        links = file.readlines()
        for link in links:
            subprocess.run(['go','install','-v',link],shell=True)

    print("[+] Tools have been successfully installed")

installer()