
from __future__ import print_function

import os
import sys

import argparse


def is_git_init():
    return os.path.isdir(".git")


def has_meta_directory():
    return os.path.isdir(".git/meta")


def create_meta_directory():
    try:
        os.makedirs('.git/meta')
    except OSError:
        pass


def get_current_git_branch():
    return 'branch'


def get_meta_path():
    branch = get_current_git_branch()
    return '/.git/meta/{}'.format(branch)


def show_metadata():
    # TODO: Check for existence
    return open(get_meta_path()).readlines()


def set_meta(metadata):
    create_meta_directory()
    with open(get_meta_path(), 'w+') as f:
        f.write(metadate)


def clear_meta():
    if not has_meta_directory():
        return


def main():

    parser = argparse.ArgumentParser(description='Process some integers.')

    parser.add_argument('-m', type=int,
                        help='Metadata for the current branch')

    parser.add_argument('-c', '--clear',
                        help="Clear the current branch's metadata")

    args = parser.parse_args()

    if not is_git_init():
        sys.exit("Not a git directory")

    if args.m and parser.clear:
        sys.exit("Must select either -m or -c options, not both")

    elif args.m:
        set_meta(args.m)

    elif args.clear:
        clear_meta()

    else:
        show_metadata()


if __name__ == '__main__':
    main()
