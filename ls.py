#! /usr/bin/env python

"""

import os


def main():
    os.system("ls -l")


if __name__ == "__main__":
    main()

"""


import subprocess

class RunCmd(object):
    def cmd_run(self, cmd):
        self.cmd = cmd
        subprocess.call(self.cmd, shell=True)

#Sample usage

a = RunCmd()
a.cmd_run('cat cmd.py')