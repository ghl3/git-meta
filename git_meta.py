
from __future__ import print_function

import os
import sys
import re

import argparse


branch_regex = re.compile('ref: refs/heads/(.*)')

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
    with open('.git/HEAD') as f:
        head = f.read()
        match = branch_regex.match(head)
        if match:
            return match.groups()[0]
    return None


def get_meta_path():
    branch = get_current_git_branch()
    return '.git/meta/{}'.format(branch)


def show_metadata():
    try:
        print("\n".join(open(get_meta_path()).readlines()))
    except IOError as e:
        print("No metadata in current branch")


def set_meta(metadata):
    create_meta_directory()
    with open(get_meta_path(), 'w') as f:
        f.write(metadata)


def clear_meta():
    if not has_meta_directory():
        return
    else:
        os.remove(get_meta_path())
    

def main():

    parser = argparse.ArgumentParser(description='Process some integers.')

    parser.add_argument('-m', '--meta', help='Metadata for the current branch')

    parser.add_argument('-c', '--clear', action='store_true', help="Clear the current branch's metadata")

    args = parser.parse_args()

    if not is_git_init():
        sys.exit("Not a git directory")

    if args.meta and args.clear:
        sys.exit("Must select either -m or -c options, not both")

    elif args.meta:
        set_meta(args.meta)

    elif args.clear:
        clear_meta()

    else:
        show_metadata()


if __name__ == '__main__':
    main()
