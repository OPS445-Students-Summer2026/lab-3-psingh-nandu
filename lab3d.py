#!/usr/bin/env python3

import subprocess

# Author ID: psingh-nandu

def free_space():

    p = subprocess.Popen(
        ['df', '-h', '/'],
        stdout=subprocess.PIPE,
        stdin=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    output = p.communicate()

    stdout = output[0].decode('utf-8').splitlines()

    return stdout[1].split()[3]


if __name__ == '__main__':
    print(free_space())