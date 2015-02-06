# git-meta
Add metadata to git repositories

Usage:
git meta -m "This is the best branch"

git meta
> This is the best branch

git checkout my-other-branch

git meta -m "Delete this branch"

git meta
> Delete this branch

git checkout -
git meta
> This is the best branch
