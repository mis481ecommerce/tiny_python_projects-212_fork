#!/usr/bin/env python3
"""
Author : zshi <zshi@localhost>
Date   : 2023-01-16
Purpose: Say Hello
"""

import argparse


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='hello project',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--name',
                        help='A named string argument',
                        metavar='name',
                        type=str,
                        default='World')

    return parser.parse_args()


# --------------------------------------------------


def main():
    """say hello"""

    args = get_args()
    word = args.name
    # print("test git")
    
    print(f"Hello, {word}!")


# --------------------------------------------------
if __name__ == '__main__':
    main()


