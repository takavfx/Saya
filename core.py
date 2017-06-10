import os
import subprocess

_CURRENTPATH = os.path.dirname(os.path.realpath(__file__))


def launch(cmds):
    proc = subprocess.Popen(cmds)
    proc.communicate()