# This is a readme for git commands

### Basic commands [for individual]

- git init (to initialize a git repo)
- git add <name of the file> or .(to add all the files)
- git status
- git commit -m "name of the commit"
- git push <to push it to remote repo>
- git pull

# Log

```
git log --graph --topo-order --pretty='%w(100,0,6)%C(yellow)%h%C(bold)%C(black)%d %C(cyan)%ar %C(green)%an%n%C(bold)%C(white)%s %N' --abbrev-commit
```

```
git log
```

- useful flags: --oneline --graph --parents --decorate
- -- decorate.
- It can be one of:
- short (the default)
- full (shows the full ref name)
- no (no decoration)

# Configs

- git config --global or --local
- git config --get or --add <name of the config>
- git config --remove-section section
- important configs => user.name "" user.email
- git config --unset <key> => to remove a config
- git cat-file -p <hash> to view the content of the commit

# Branch

```
 git branch
```

- to see current working branch

```
git branch -m oldname newname
```

- to rename a branch

```
 git branch -M main
```

- to change master to main

```git branch my_new_branch

```

- to create new branch

```
 git switch -c my_new_branch
```

- (new way) to create and switch branch

# Merge REPO

- create a new repo
- add the repo to merge
  :c
  :x
  :x
  :X

  git merge <name of repo>/main --allow-unrelated-histories

##### Merge branches

```
 git merge <name of the branch>
```

- we merge branch on the main
- merge commit => merging braches present you with a with a code editor to change the commit message.
- add the commit message then exit
- merge log => after the merge git log will present you with a merge log

# Important notes

- Git is made up of objects that are stored in the .git/objects directory.
- A commit is just a type of object.
- for git config
- We've used --list to see all the configuration values, but the - --get flag is useful for getting a single value.

# Location of config

- system: /etc/gitconfig, a file that configures Git for all users on the system
- global: ~/.gitconfig, a file that configures.
  - Git for all projects of a user.
  - local: .git/config, a file that configures Git for a specific project
  - worktree: .git/config.worktree
  - a file that configures Git for part of a project

# Git Files

- The "heads" (or "tips") of branches are stored in the .git/refs/heads directory.
- If you cat one of the files in that directory, you should be able to see the commit hash that the branch points to.
#### how to commit on previous date 
```bash
GIT_AUTHOR_DATE="2025-09-03 12:00:00" GIT_COMMITTER_DATE="2025-09-03 12:00:00" git commit -m "commit message"
```

