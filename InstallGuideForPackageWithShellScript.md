# Installation guide for zawgyi-keyboard-`*`.tar.gz #

### Guide For `zawgyi-keyboard-0.2.x.tar.gz` ###

This package is `shell scripte install package` (source package). That is upstream release of `zawgyi-keyboard-0.1.2` package and It has been upgraded for new zawgyi font (2009 July version). This package can be installed on `Ubuntu 8.10`, `9.04`, `9.10`, `Fedora 9`, `10`, `11`, `Debian 5`, `FreeBSD 7.x Gnome2 Desktop` and also can be for `OpenSUSE`.

  * Platform: Linux/Unix ( Debian, Fedora, Ubuntu, FreeBSD )
  * Package: zawgyi-keyboard
  * Version: 0.2.0, 0.2.1

See [Installation Guide](#Installing_zawgyi_keyboard.md), [Post Installation](#Post_installation_for_new_zawgyi_font.md) and [Testing Zawgyi Keyboard](#Testing_Zawgyi_Keyboard.md).


### Guide For `zawgyi-keyboard-0.1.2.tar.gz` ###

This package is `shell scripte install package` (source package). That is upstream release of `zawgyi-keyboard-ubuntu904` package. This package can be installed on `Ubuntu 8.10`, `9.04`, `9.10`, `Fedora 9`, `10`, `11`, `Debian 5`, `FreeBSD 7.x Gnome Desktop` and also can be for `OpenSUSE`.

  * Platform: Linux/Unix ( Debian, Fedora, Ubuntu, FreeBSD )
  * Package: zawgyi-keyboard
  * Version: 0.1.2


#### Installing zawgyi keyboard ####

The Downloaded `zawgyi-keyboard-*.tar.gz` would be in `~/Desktop` or somewhere else.

  * Change to your Path
```
cd /path/to/zawgyi-keyboard-*.tar.gz/
```

  * Extract the `tar ball`
```
$ sudo tar xvf zawgyi-keyboard*.tar.gz
```

**Note:** `tar` is an application which can extract files from an archive, decompressing if necessary.
> -x means extract.
> -v means verbose (list what it is extracting).
> -f specifies the file to use.


  * Go to `source` Folder
```
cd zawgyi
```

  * Install `zawgyi keyboard`
```
sudo sh install.sh

`or`

su
sh install.sh
```

  * Remove `zawgyi keyboard`
```
sudo sh uninstall.sh 

`or` 

su
sh uninstall.sh 
```

**Note:** for Gnome Desktop base on FreeBSD Gnome2 users

> Please use `install_freebsd.sh` and `uninstall_freebsd.sh` scripts instead.

See [Post Installation](#Post_installation.md) and [Testing Zawgyi Keyboard](#Testing_Zawgyi_Keyboard.md).


### Guide For `zawgyi-keyboard-0.1.1.tar.gz` ###

This package is `shell scripte install package` (source package). That is upstream release of `zawgyi-keyboard-ubuntu904` package. This package can be installed on `Ubuntu 8.10`, `9.04`, `9.10`, `Fedora 9`, `10`, `11`, `Debian 5` and also can be for `OpenSUSE`.

  * Platform: Linux ( Debian, Fedora, Ubuntu )
  * Package: zawgyi-keyboard
  * Version: 0.1.1

#### Installing for zawgyi-keyboard-0.1.1.tar.gz ####

The Downloaded `zawgyi-keyboard-0.1.1.tar.gz` would be in `~/Desktop` or somewhere else.

  * Change to your Path
```
cd /path/to/zawgyi-keyboard-0.1.1.tar.gz/
```

  * Extract the `tar ball`
```
$ sudo tar xvf zawgyi-keyboard*.tar.gz
```

**Note:** `tar` is an application which can extract files from an archive, decompressing if necessary.
> -x means extract.
> -v means verbose (list what it is extracting).
> -f specifies the file to use.


  * Go to `source` Folder
```
cd zawgyi
```

  * Install `zawgyi keyboard`
```
sudo sh install.sh

`or`

su
sh install.sh
```

  * Remove `zawgyi keyboard`
```
sudo sh uninstall.sh 

`or` 

su
sh uninstall.sh 
```

See [Post Installation](#Post_installation.md) and [Testing Zawgyi Keyboard](#Testing_Zawgyi_Keyboard.md).


### Guide For `zawgyi-keyboard-ubuntu904.tar.gz` ###

#### Installing for zawgyi-keyboard-ubuntu904.tar.gz ####

The Downloaded `zawgyi-keyboard-ubuntu904.tar.gz` would be in `~/Desktop` or somewhere else.

  * Change to your Path
```
cd /path/to/zawgyi-keyboard-ubuntu904.tar.gz/
```

  * Extract the `tar ball`
```
$ sudo tar xvf zawgyi-keyboard*.tar.gz
```

**Note:** `tar` is an application which can extract files from an archive, decompressing if necessary.
> -x means extract.
> -v means verbose (list what it is extracting).
> -f specifies the file to use.


  * Go to `source` Folder
```
cd zawgyi
```

  * Install `zawgyi keyboard` from `shell script`
```
sudo sh install.sh
```


### Post installation ###

  * Go to `System -> Preferences-> Keyboard`, click on `Keyboard`, then _Keyboard Preferences_ would be appear.
  * Go to `Layout Tab` and click on `Add` button. Choose a Layout `Myanmar` and press `Add` button.

You will have both **US** English Layout and **Myanmar** Zawgyi Layout.
  * To get keyboard switching and Third Level chooser, press `Layout Options` in the Layout Tab of Keyboard Preferences.
  * Check _e.g._ Shift+Alt Change Layout in Layout Switching and Check _e.g._ Any-Wins key in Third Level Chooser.

  * Also you can do keyboard configuration manually in Terminal,
```
setxkbmap -model pc104 -layout us,mm -variant ,zawgyi
setxkbmap -option -option grp:alt_shift_toggle,lv3:win_switch
```

**NOTE:** It depends on you and your preferences. Then you can work with both of English and Zawgyi Keyboard.

If you want to get `Keyboard Indicator` on your panel, right-click on _Panel_ and click on **Add to Panel**. Search `Keyboard Indicator` and click it to add.
You will see _**Keyboard Indicator**_ on your Panel.

**TIPS:** You may Need to Log out your system after installing the package.


### Testing Zawgyi Keyboard ###

You can test some words in `Gedit` to know if it corrects or not. When you get correct words, it is done.

Having a lot of fun with your zawgyi-keyboard!! :-)

### Post installation for new zawgyi font ###

  * Go to `System -> Preferences-> Keyboard`, click on `Keyboard`, then _Keyboard Preferences_ would be appear.
  * Go to `Layout Tab` and click on `Add` button. Choose a Layout `Myanmar` and press `Add` button.

You will have both **US** English Layout and **Myanmar** Zawgyi Layout.
  * To get keyboard switching, press `Layout Options` in the Layout Tab of Keyboard Preferences.
  * Check _e.g._ Shift+Ctrl Change Layout in Layout Switching.
  * Also you can do keyboard configuration manually in Terminal,
```
setxkbmap -model pc105 -layout us,mm -variant ,zawgyi
```
For old zawgyi font till ZawgyiOne20080210.ttf, we had to have Third Level Chooser. But Right now we don't have to have Third Level Chooser for new zawgyi font (July 2009 version). It would be using `shift+f` instead.


**NOTE:** It depends on you and your preferences. Then you can work with both of English and Zawgyi Keyboard.

If you want to get `Keyboard Indicator` on your panel, right-click on _Panel_ and click on **Add to Panel**. Search `Keyboard Indicator` and click it to add.
You will see _**Keyboard Indicator**_ on your Panel.

**TIPS:** You may Need to Log out your system after installing the package.