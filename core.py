import os
import subprocess
from multiprocessing import Process

_CURRENTPATH = os.path.dirname(os.path.realpath(__file__))


def call(cmds):
    proc = subprocess.Popen(cmds)
    proc.communicate()

def launch(cmds):
    p = Process(target=call, args=(cmds,))
    p.start()
    p.join()
