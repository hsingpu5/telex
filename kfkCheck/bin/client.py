#!/usr/bin/env python3
import os
import sys

ret = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ret)
print(ret)


if __name__ == '__main__':

    os.environ['USER_SETTINGS'] = 'conf.settings'
    print(os.environ)
    from src.script import run

    run()
