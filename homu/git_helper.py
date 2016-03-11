#!/usr/bin/env python3

import sys
import os

def main():
    cfgpath = os.environ.get('HOMU_SSH_CONFIG')
    args = ['ssh', '-i', os.getenv('HOMU_GIT_KEY_PATH'), '-S', 'none']
    if cfgpath is not None:
        args.extend(['-F', cfgpath])
    args.extend(sys.argv[1:])
    os.execvp('ssh', args)


if __name__ == '__main__':
    main()
