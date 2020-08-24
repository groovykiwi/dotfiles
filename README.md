# Dotfiles

To install the whole setup :

```
cd ~
git clone https://github.com/groovykiwi/dotfiles/
cd dotfiles
./packages
./config

```

All the dotfiles are symlinked to the ~/dotfiles folder for an easy management.

The install scripts are made to be ran on a fresh install of Manjaro i3 Edition but should work fine on any Arch based system.

The color scheme are generated using [pywal](https://github.com/dylanaraps/pywal) and made permanent with a custom script. Instead of using `wal` use `bpw`, check `bpw -h` for more information.
This means that if you want to make changes to .Xresources, refer to `.config/wal/templates/colors.Xresources` instead.

## Screenshots

![Picture](https://github.com/groovykiwi/dotfiles/blob/master/git-stuff/ss1.png)
