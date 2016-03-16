# Installation guide for zawgyi-keyboard-`*`.tar.gz #

### Guide For `zawgyi-keyboard-0.3.x.tar.gz` ###

This package is `python script install package` (source package). That is new upstream release of `zawgyi-keyboard-0.x.x` package series and It has been upgraded for new zawgyi 2009 font. This package can be installed on `Ubuntu 7.04`, `7.10`, `8.04`, 8.10`, `9.04`, `9.10`, `Fedora 6`, `7`, `8`, `9`, `10`, `11`, `Debian 4`, `5`, `FreeBSD 7.x Gnome2 Desktop` and also can be for other linux distro which has GNOME desktop such as `OpenSUSE` and so on.

  * Platform: Linux/Unix ( Debian, Fedora, Ubuntu, FreeBSD )
  * Package: zawgyi-keyboard
  * Version: 0.3.2

#### Using zawgyi\_keyboard.py ####

The Downloaded `zawgyi-keyboard-*.tar.gz` would be in `~/Desktop` or somewhere else.

  * Change to your Path
```
$ cd /path/to/zawgyi-keyboard-*.tar.gz/
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
$ cd zawgyi
```

  * Run `zawgyi_keyboard.py` python script
```
$ sudo python zawgyi_keyboard.py

`or`

$ su
# python zawgyi_keyboard.py
```

The program will detect which platform you are using and check the source package first before proceeding another tasks and ask you to press..
`[i]` install, `[r]` remove, `[h]` layout help, `[u]` update font, `[q]` exit :

**Keys:**
```
 i - install : Installing package
 r - remove : Removing package
 h - layout help : Showing short layout option guide
 o - update font : Updating new font from internet if new font available
 u - update font : Updating new font manually from your local directory
 s - show font : Showing your current installed font and latest font which is available
 q - exit : ending the program
```

See [Screenshots](http://picasaweb.google.com/thebox02/ZawgyiKeyboard030TarGzInstallAndHowto?feat=directlink)