# .dotfiles

[Inspiration](https://www.atlassian.com/git/tutorials/dotfiles)

**This guide assumes the repo is cloned to $HOME/.dotfiles.**

## Initial setup
```
git init --bare $HOME/.dotfiles
alias config='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'
config config --local status.showUntrackedFiles no
```

If ```config``` alias is not in your .zshrc yet.
```
echo "alias config='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'" >> $HOME/.zshrc
```

### Add file to vcs
```
config add .some_dot_file
config commit -m "..."
```

### Set up remote
```
git remote add origin git@github.com:<user>/<repo>.git
git push -u origin master
```

## Install on new system
Add ```config``` alias (for current shell session)
```
alias config='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'
```

Prevent recursion issues
```
echo ".dotfiles" >> $HOME/.gitignore
```

Then, clone repo
```
git clone --bare <git-repo-url> $HOME/.dotfiles
```

Check out repo content
```
config checkout
```

Configure local repo to hide untracked files
```
config config --local status.showUntrackedFiles no
```

