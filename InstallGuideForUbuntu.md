## Installation Guides for zawgyi keyboard on Ubuntu ##


#### Add Repositories Using Synaptic Package Manager ####
This is the preferred method.
  * System -> Administration -> Synaptic Manager -> Settings -> Repositories
  * Here you can enable the repositories for Ubuntu Software and Third Party Software.
  * For Third Party Software select Add -> enter the repository's address. It will have a format similar to: for example;
```
deb http://archive.ubuntu.com/ubuntu/ jaunty main restricted
deb-src http://archive.ubuntu.com/ubuntu/ jaunty main restricted
```
  * So we will add the zawgyi-kb repository; Add:
> For Ubuntu 9.04,
```
deb http://ppa.launchpad.net/zawgyi-kb/ppa/ubuntu jaunty main
deb-src http://ppa.launchpad.net/zawgyi-kb/ppa/ubuntu jaunty main
```
  * Download the repository key to a folder.
  * The Launchpad zawgyi-kb key can be downloaded from
> > http://zawgyi-keyboard.googlecode.com/files/launchpad_zawgyi-kb.gpg
  * Then add the key from:
> > System -> Administration -> Synaptic Manager -> Settings -> Repositories -> Authentication -> Import Key File...
  * Refresh the package list from the new repository:
> > Synaptic -> Reload

#### Manually Add Repositories ####
  * Do this at your own risk. Modify the default Ubuntu sources.list only if you understand what you're doing. Mixing repositories can break your system. For more information see the [Ubuntu Command Line Repository Guide](https://help.ubuntu.com/community/Repositories/CommandLine)
  * Create a backup of your current list of sources.
```
sudo cp -p /etc/apt/sources.list /etc/apt/sources.list_backup
```
Note: sudo - runs the command with root privileges. cp = copy. -p = prompt to overwrite if a file already exists.
  * Edit the list of sources:
```
sudo vim /etc/apt/sources.list
```
> > or using a graphical editor:
```
gksu gedit /etc/apt/sources.list
```
  * sources.list file will open with your editor, then at the end of that file, you may want to add zawgyi-kb repositories.
  * Save the sources.list file and exit or close your editor.
  * Download and add the repository key to your keyring. See [Add repository keys](#Add_repository_key.md).
  * Refresh the packages list from the new repositories:
```
sudo apt-get update 
```

#### Add repository key ####
  * Download the gpg keys for the repositories and automatically add them to your repository keyring:
    * _Example_: To obtain and add the Launchpad zawgyi-kb repository key:
```
wget -q http://zawgyi-keyboard.googlecode.com/files/launchpad_zawgyi-kb.gpg -O- | sudo apt-key add -
```
Note: wget - retrieves a file from a network location. -q = no output. -O = Output downloaded item to terminal. The | (pipe symbol) is used to capture the output from the previous command (in our case the screen) and use it as an input for the piped command (i.e. apt-key, which adds it to the keyring).

#### Package Installing and Update ####
Most new users will use the Synaptic Package Manager to install packages. These instructions are for installing packages from the command-line Terminal. Terminal can be started:


> Applications -> Accessories -> Terminal

  * Install zawgyi-kb package
```
sudo apt-get install --force-yes zawgyi-kb
```

  * Remove zawgyi-kb package
```
sudo apt-get remove zawgyi-kb
```

  * Search zawgyi-kb package
```
apt-cache search zawgyi-kb
```

  * Update packages
```
sudo apt-get update
```

#### Installing .deb packages ####
Debian (.deb) packages are the packages that are used in Ubuntu. You can install any .deb package in your system. .deb files can generally be installed from your file manager (Nautilus) merely by clicking on them, since file associations with the default installer is already set in Ubuntu. These instructions are for those who wish to install packages from the command-line terminal (Terminal).
  * Install a downloaded zawgyi-kb Debian (Ubuntu) package (.deb):
```
sudo dpkg -i --force-overwrite zawgyi-kb*.deb
```
  * Remove zawgyi-kb Debian (Ubuntu) package (.deb):
```
sudo dpkg -r zawgyi-kb
```
  * Reconfigure/Repair an installed zawgyi-kb Debian (Ubuntu) package (.deb):
```
sudo dpkg-reconfigure zawgyi-kb
```


--to be continuous--