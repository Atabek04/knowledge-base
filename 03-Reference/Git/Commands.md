# Git Commands

## Setup
```bash
git config --global user.name "Name"
git config --global user.email "email@example.com"
git init
git init --bare repo.git
```

## Staging
```bash
git add <file>                  # stage file
git add .                       # stage all
git reset HEAD <file>           # unstage file
git reset HEAD                  # unstage all
```

## Commits
```bash
git commit -m "message"
git commit -am "message"        # stage tracked + commit
git commit --amend              # modify last commit
```

## Undo Commits
```bash
git reset --soft HEAD~1         # undo, keep staged
git reset HEAD~1                # undo, keep unstaged
git reset --hard HEAD~1         # undo, discard changes
git revert <hash>               # create inverse commit
```

## Branches
```bash
git branch <name>               # create
git branch                      # list local
git branch -r                   # list remote
git branch -d <name>            # delete (safe)
git branch -D <name>            # delete (force)
git branch -m <new>             # rename current
git branch -m <old> <new>       # rename other
git checkout <branch>           # switch
git checkout -b <branch>        # create + switch
git switch <branch>             # switch (modern)
git switch -c <branch>          # create + switch (modern)
```

## Merging
```bash
git merge <branch>
git merge --no-ff <branch>      # force merge commit
git merge --abort               # cancel merge
```

## Rebasing
```bash
git rebase <branch>
git rebase -i <branch>          # interactive
git rebase -i HEAD~3            # last 3 commits
git rebase --continue           # after conflict
git rebase --abort              # cancel rebase
```

## Stashing
```bash
git stash                       # save changes
git stash list                  # list stashes
git stash apply                 # apply latest
git stash apply stash@{2}       # apply specific
git stash pop                   # apply + remove
git stash drop stash@{2}        # remove specific
git stash clear                 # remove all
```

## Remote
```bash
git remote -v                   # list remotes
git remote add <name> <url>
git remote rename <old> <new>
git remote remove <name>
git fetch                       # download changes
git fetch -p                    # fetch + prune
git pull origin <branch>        # fetch + merge
git pull --rebase               # fetch + rebase
git push origin <branch>
git push -u origin <branch>     # set upstream
git push --force                # overwrite remote
git push --force-with-lease     # safe force push
```

## Tags
```bash
git tag <name>                  # lightweight tag
git tag <name> <hash>           # tag specific commit
git tag -a <name> -m "msg"      # annotated tag
git tag                         # list tags
git tag -l "v2*"                # filter tags
git tag -n                      # tags with messages
git tag -d <name>               # delete local
git push origin <tag>           # push single tag
git push origin --tags          # push all tags
git push -d origin <tag>        # delete remote tag
```

## History
```bash
git log
git log --oneline
git log -p                      # with diffs
git log <file>                  # file history
git log -L 100,150:<file>       # line range history
git log HEAD..origin/main       # incoming commits
git reflog                      # all HEAD movements
```

## Diff
```bash
git diff                        # unstaged changes
git diff --staged               # staged changes
git diff <branch1>..<branch2>
git diff <hash1>..<hash2>
```

## Inspection
```bash
git status
git show <hash>
git blame <file>
git blame -L 100,150 <file>     # line range
git blame -w <file>             # ignore whitespace
```

## Cherry-pick
```bash
git cherry-pick <hash>
git cherry-pick <start>..<end>  # range (excludes start)
git cherry-pick --continue
git cherry-pick --abort
```

## Bisect
```bash
git bisect start
git bisect good <hash>
git bisect bad <hash>
git bisect reset                # end bisect
```

## Cleanup
```bash
git gc                          # garbage collection
git gc --aggressive             # thorough cleanup
git gc --prune=now              # prune immediately
git remote prune origin         # remove stale refs
git remote prune origin --dry-run
```

## Patches
```bash
git diff <from> <to> > file.diff
git apply file.diff
git format-patch <range>
git format-patch -1 <hash>      # single commit
git am <patch-file>             # apply formatted patch
```

## Restore
```bash
git restore <file>              # discard changes
git restore --source=<hash> <file>
git checkout -- <file>          # older syntax
```

## Interactive
```bash
git add -i                      # interactive staging
git add -p                      # patch mode
git stash -p                    # selective stash
git reset -p                    # selective unstage
```
