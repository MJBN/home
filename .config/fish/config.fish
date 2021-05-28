set -g fish_greeting
fish_add_path $HOME/.config/composer/vendor/bin

#Aliases
alias mi="micro"
alias ls="exa -lh"
alias la="exa -lah"
alias pm="sudo pacman"
alias android-mount="jmtpfs ~/android"
alias android-unmount="fusermount -u ~/android"
alias wifi-c="nmtui connect"
alias mic-e="amixer set Capture cap"
alias mic-d="amixer set Capture nocap"
alias part="php artisan"
