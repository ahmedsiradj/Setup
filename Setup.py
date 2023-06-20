#!/usr/bin/python

import subprocess
import json

def GoInstaller():
    with open('resourses/db.json','r') as file:
        data = json.load(file)
        for link in data["GoLinks"]:
            subprocess.run(['go','install','-v',link])

    print("[+] Tools have been successfully installed")

GoInstaller()