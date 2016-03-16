## Installation Guides for zawgyi keyboard on Fedora ##

#### Installing `.rpm` package ####

Red Hat (.rpm) packages are the packages that are used in Fedora. You can install any .rpm package in your system. .rpm files can generally be installed from your file manager (Nautilus) merely by clicking on them, since file associations with the default installer is already set in Fedora. These instructions are for those who wish to install packages from the command-line terminal (Terminal).

  * Install a downloaded zawgyi-keyboard Red Hat (Fedora) package (.rpm):
```
su 
rpm -ivh --force zawgyi-keyboard*.rpm 
```

  * Remove zawgyi-keyboard Red Hat (Fedora) package (.rpm):
```
su 
yum remove zawgyi-keyboard
```

**NOTE:**

> In case the system updates `xkeyboard-config` package, you may need to install `xkeyboard-config` package by force because those `xkeyboard-config` package and `zawgyi-keyboard` package are using the same data.

> In case the system updates a lot packages including `xkeyboard-config` package, the update will show you error. Then you need to remove `zawgyi-keyboard` for a while until the update finishes. After updating your system, you re-install `zawgyi-keyboard` package with above method.

**SUGGEST:**

> If your fedora system comes with pre-installed `padauk-fonts` package, you may need to remove it **first** so that you would see `zawgyi` font correctly on your desktop. To remove `padauk-fonts` package, _for example_:
```
su
yum remove padauk-fonts
```