#!/bin/bash
for entry in "etc/lightdm"/*
do
	sudo rm -rf "/$entry" && echo "/$entry"
	sudo ln -s "$HOME/dotfiles/$entry" "/$entry" && echo -e "Created symlink with $entry \n"
done