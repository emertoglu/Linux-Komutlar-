#! /usr/bin/env python

import subprocess

def runBash(cmd):
    p=subprocess.Popen(cmd, shell=True , stdout=subprocess.PIPE)
    out=p.stdout.read().strip()
    return out.split('\n')


def changeName(oldName, newNameBase):
    tempp=oldName.split('.')
    newname=newNameBase+'.'+tempp[1]+ '.' +tempp[2]
    subprocess.call("mv", oldName,newname)


def changeAllName(oldNameBase, newNameBase):
    files=runBash("ls")

    for afile in files:
        if afile.split('.'[0]==oldNameBase):
            changeName(afile,newNameBase)


changeAllName("test","new")

