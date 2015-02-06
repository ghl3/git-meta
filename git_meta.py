
import argparse

import sys



def set_meta(metadata):
    pass


def clear_meta():
    pass


def main():

    parser = argparse.ArgumentParser(description='Process some integers.')

    parser.add_argument('-m', type=int,
                        help='Metadata for the current branch')

    parser.add_argument('-c', '--clear',
                        help="Clear the current branch's metadata")

    args = parser.parse_args()

    if args.m and parser.clear:
        sys.exit("Must select either -m or -c options")

    elif args.m:
        set_meta(args.m)

    elif args.clear:
        clear_meta()

    else:
        sys.exit("Must select either -m or -c options")



if __name__ == '__main__':
    main()
