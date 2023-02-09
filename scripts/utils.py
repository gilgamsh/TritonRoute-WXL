import os

def run(command):
    print(command)
    os.system('/bin/bash -c \'{0}\''.format(command))