#!/bin/bash

NC='\033[0m' # No Color
ACCENT='\033[1;31m'

while getopts b flag
do
    case "${flag}" in
    	b) backup="True";;
    esac
done
[[ -d $HOME/.backup ]] && echo -e "\nA previous backup (~/.backup) has been found, it will be overwritten. To cancel press Ctrl+C or press ENTER to continue " && read answer
[[ "$backup" == "True" ]] && echo "Backing up to ~/.backup" && sudo rm -rf $HOME/.backup && mkdir $HOME/.backup &&sudo cp -p -r $HOME/.config/ $HOME/.backup/.config && echo "Done: .config/ " && sudo cp -p -r /etc/ $HOME/.backup/etc && echo "Done: etc/ " && sudo cp -p $HOME/{.Xresources,.bashrc,.bash_profile,.profile} $HOME/.backup/ && echo "Done: dotfiles \n"

#Symlink .config files
for entry in ".config"/*
do
	rm -rf "$HOME/$entry" && echo "Deleted $HOME/$entry"
	ln -s "$HOME/dotfiles/$entry" "$HOME/$entry" && echo -e "Created symlink with $entry \n"
done


#Symlink /etc files
for entry in "etc"/*
do
	sudo rm -rf /"$entry" && echo Deleted /"$entry"
	sudo ln -s "$HOME"/dotfiles/$entry /"$entry" && echo -e "Created symlink with $entry \n"
done

#Symlink myfonts folder
[[ -d /usr/share/fonts/myfonts ]]  && echo "Found /usr/share/fonts/myfonts" && sudo rm -rf /usr/share/fonts/myfonts && echo "Deleted /usr/share/fonts/myfonts"
sudo ln -s $HOME/dotfiles/myfonts /usr/share/fonts/ && echo -e "Created symlink with myfonts \n"

#Symlink scripts folder
[[ -d $HOME/scripts ]]  && echo "Found ~/scripts" && rm -rf $HOME/scripts && echo "Deleted ~/scripts"
ln -s $HOME/dotfiles/scripts $HOME  && echo -e "Symlinked scripts folder \n"

#Symlink .bashrc
[[ -f $HOME/.bashrc ]] && echo "Found .bashrc" && rm $HOME/.bashrc && echo "Deleted .bashrc"
ln -s $HOME/dotfiles/.bashrc $HOME && echo -e "Symlinked .bashrc \n"

#Symlink .bash_profile
[[ -f $HOME/.bash_profile ]] && echo "Found .bash_profile" && rm $HOME/.bash_profile && echo "Deleted .bash_profile"
ln -s $HOME/dotfiles/.bash_profile $HOME && echo -e "Symlinked .bash_profile \n"

#Symlink .profile
[[ -f $HOME/.profile ]] && echo "Found .profile" && rm $HOME/.profile && echo "Deleted .profile"
ln -s $HOME/dotfiles/.profile $HOME && echo -e "Symlinked .profile \n"

#Symlink .Xresources
[[ -f $HOME/.Xresources ]] && echo "Found .Xresources" && rm $HOME/.Xresources && echo "Deleted .Xresources"
ln -s $HOME/dotfiles/.Xresources $HOME && echo "Symlinked .Xresources "