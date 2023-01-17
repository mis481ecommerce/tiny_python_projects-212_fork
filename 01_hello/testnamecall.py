#!/usr/bin/env python3

import testname as tn

def main():
    print("in main of testnamecall")
    print(__name__)
    print("now call testname")
    tn.main()

if __name__ == '__main__':
    main()