# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:/usr/local/bin:$PATH

# Path to your oh-my-zsh installation.
export ZSH=$HOME/.oh-my-zsh

# Set name of the theme to load. Optionally, if you set this to "random"
# it'll load a random theme each time that oh-my-zsh is loaded.
# See https://github.com/robbyrussell/oh-my-zsh/wiki/Themes
ZSH_THEME="mortalscumbag-mod"

# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment the following line to use hyphen-insensitive completion. Case
# sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"

# Uncomment the following line to disable bi-weekly auto-update checks.
# DISABLE_AUTO_UPDATE="true"

# Uncomment the following line to change how often to auto-update (in days).
# export UPDATE_ZSH_DAYS=13

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
# COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# The optional three formats: "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
# HIST_STAMPS="mm/dd/yyyy"

# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

# Which plugins would you like to load? (plugins can be found in ~/.oh-my-zsh/plugins/*)
# Custom plugins may be added to ~/.oh-my-zsh/custom/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.

plugins=(
    vi-mode
)

source $ZSH/oh-my-zsh.sh

# User configuration

# export MANPATH="/usr/local/man:$MANPATH"

# You may need to manually set your language environment
# export LANG=en_US.UTF-8

# Preferred editor for local and remote sessions
# if [[ -n $SSH_CONNECTION ]]; then
#   export EDITOR='vim'
# else
#   export EDITOR='mvim'
# fi

# Compilation flags
# export ARCHFLAGS="-arch x86_64"

# ssh
# export SSH_KEY_PATH="~/.ssh/rsa_id"

# Set personal aliases, overriding those provided by oh-my-zsh libs,
# plugins, and themes. Aliases can be placed here, though oh-my-zsh
# users are encouraged to define aliases within the ZSH_CUSTOM folder.
# For a full list of active aliases, run `alias`.
#
# Example aliases
# alias zshconfig="mate ~/.zshrc"
# alias ohmyzsh="mate ~/.oh-my-zsh"


source /usr/share/fzf/completion.zsh
source /usr/share/fzf/key-bindings.zsh
source $HOME/.config/broot/launcher/bash/br


function fman() {
    man -k . | fzf -i -e -q "$1" --prompt='man> '  --preview $'echo {} | tr -d \'()\' | awk \'{printf "%s ", $2} {print $1}\' | xargs -r man' | tr -d '()' | awk '{printf "%s ", $2} {print $1}' | xargs -r man
}


eval "$(pyenv init -)"
#eval "$(starship init zsh)"


alias la='ls -la --group-directories-first --time-style=+"%d.%m.%Y %H:%M" --color=auto -F'
alias ll='ls -l --group-directories-first --time-style=+"%d.%m.%Y %H:%M" --color=auto -F'
alias config="/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME"
alias confg="lazygit --work-tree=$HOME --git-dir=$HOME/.dotfiles"
alias fpac="pacman -Slq | fzf --multi --preview 'pacman -Si {1}' | xargs -ro sudo pacman -S"
alias faur="paru -Slq | fzf --multi --preview 'paru -Si {1}' | xargs -ro paru -S"
alias fremove="pacman -Qq | fzf --multi --preview 'pacman -Qi {1}' | xargs -ro sudo pacman -Rns"
alias bat='bat --paging always'
alias pdf="fd --type f '.*.pdf.*' $HOME | fzf --preview-window=hidden -i -e | xargs -I {} okular {}"
alias ranger='source ranger'
alias porp='poetry run python'
alias por='poetry run'
alias lg='lazygit'
alias class="xprop | grep -m 1 WM_CLASS | awk '{print \$4}'"


export PATH=$HOME/.screenlayout:$PATH
export PATH=$HOME/.scripts:$PATH
export PATH=$HOME/Applications/bin:$PATH
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
export EDITOR=/usr/bin/vim
export VISUAL=/usr/bin/vim
export BROWSER=/usr/bin/firefox-developer-edition
export FZF_DEFAULT_OPTS="-i --exact --preview '([ -f {} ] && (bat --color=always --style=plain,header,grid {} | head -300)) || ([ -d {} ] && (tree -C {} | less)) || echo {} 2> /dev/null | head -300'"
export FZF_DEFAULT_COMMAND='fd --hidden'
export FZF_ALT_C_COMMAND="fd --type d --hidden --exclude '.git' --exclude '.cfg' --exclude '.dotfiles' --exclude 'Gdrive' --exclude '/mnt' --exclude '/media' --exclude '/run' . ."
export FZF_CTRL_T_COMMAND="fd --hidden --exclude '.git' --exclude '.dotfiles' --exclude '/Gdrive' --exclude '/Glacier' . '/'"
export TERM="xterm-256color"
export HISTORY_IGNORE="(ls|cd|pwd|exit|sudo reboot|history|cd -|cd ..)"
export MANPAGER="sh -c 'col -bx | bat -l man -p --paging always'"
export BAT_THEME=ansi
# Deep learning
export LD_LIBRARY_PATH=/opt/cuda/extras/CUPTI/lib64:/opt/cuda/targets/x86_64-linux/lib


fm6000 --color random --random

