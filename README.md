
A number of tools to augment git's standard functionality.

To use, simply download this package and add it to your path.

Then, one can simply run:

    git meta <args>
    git head <args>


# git-meta
Add string metadata to git branches.  The metadata stays with the branch even if it is committed to or rebased.

Usage:
git meta -m "This is the best branch"

git meta

    This is the best branch

git checkout my-other-branch

git meta -m "Delete this branch"

git meta

    Delete this branch

git checkout -
git meta

    This is the best branch

# git-hide
Hide branches that are no longer in use (but that you don't want to delete)

Usage:

git branch hide-me
git banch

    master
    hide-me

git hide -b hide-me
git branch

    master

git hide --show

    hide-me

git hide --restore hide-me
git branch

    master
    hide-me
