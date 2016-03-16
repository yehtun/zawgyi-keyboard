# Installation guide for mm3-keyboard-`*`.tar.gz #

### Guide For `mm3-keyboard-*.tar.gz` ###

  * Platform: Linux/FreeBSD ( Debian, Fedora, Ubuntu, FreeBSD, etc.. )
  * Package: mm3-keyboard
  * Version: 0.1.0 (TESTING)

#### Using mm3-keyboard.py ####

The Downloaded `mm3-keyboard-*.tar.gz` would be in `~/Desktop` or somewhere else.

  * Change to your Path
```
$ cd /path/to/mm3-keyboard-*.tar.gz/
```

> _for example_
```
$ cd ~/Desktop/
```
  * Extract the `tar ball`
```
$ tar xvf mm3-keyboard*.tar.gz
```

**Note:** `tar` is an application which can extract files from an archive, decompressing if necessary.
> -x means extract.
> -v means verbose (list what it is extracting).
> -f specifies the file to use.


  * Go to `source` Folder
```
$ cd mm3-keyboard
```

  * Run `mm3-keyboard.py` python script
```
$ sudo python mm3-keyboard.py

`or`

$ su
# python mm3-keyboard.py
```

The program will detect which platform you are using and check the source package first before proceeding another tasks and ask you to press..

`[i]` install, `[r]` remove, `[h]` layout help, `[q]` exit :

**Keys:**
```
 i - install : Installing package
 r - remove : Removing package
 h - layout help : Showing short layout option guide
 q - exit : ending the program
```