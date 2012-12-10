#!/bin/bash

#    zawgyi-keyboard - zawgyi keyboard installation for linux.
#    Copyright (C) 2009  lrcmm.org
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#    Author: box02 (thebox02@gmail.com)
#    Sat Jul 25, 2009

FONTNAME=zawgyi
FONT_DIR=/usr/share/fonts
DOC_DIR=/usr/share/doc
DATA_DIR=/usr/share
XKB_DIR=/usr/share/X11/xkb/symbols
APPS_DIR=/usr/share/applications
ICONS_DIR=/usr/share/pixmaps

echo
echo "zawgyi-keyboard  Copyright (C) 2009  lrcmm.org"
echo "This program comes with ABSOLUTELY NO WARRANTY."
echo "This is free software, and you are welcome to redistribute it"
echo "under certain conditions; read the file LICENSE for details."
echo
echo "WARNING: Please remove your zawgyi keyboard previous installed"
echo "before starting this installation."
echo

# install directories
mkdir -p $DATA_DIR/$FONTNAME 
mkdir -p $DOC_DIR/$FONTNAME 
mkdir -p $FONT_DIR/$FONTNAME 

# install zawgyi font
echo "Installing font..."
cp src/*.ttf $FONT_DIR/$FONTNAME
fc-cache $FONT_DIR/$FONTNAME
sleep 1
echo

# install zawgyi xkeyboard
echo "Installing xkeyboard..."
cp -f src/mm $XKB_DIR
cp -f src/mm_orig $XKB_DIR
sleep 1
echo

# install zawgyi keymaps layout
echo "Installing keymaps layout..."
cp src/xkb.keyboard.map.png $DATA_DIR/$FONTNAME
cp src/zawgyi.desktop $APPS_DIR
cp src/zawgyi.png $ICONS_DIR
sleep 1
echo

# install docs
echo "Installing documents..."
cp AUTHORS CREDITS NOTICE $DOC_DIR/$FONTNAME
cp changelog COPYRIGHT README $DOC_DIR/$FONTNAME
sleep 1
echo

# you might want to prepare keyboard layout preferences
# use the following options.
#setxkbmap -model pc105 -layout us,mm -variant ,zawgyi

echo "Installation successfully Done!"
echo "You may NEED to Log Out your system to correct your keyboard."
echo "Good bye!"
echo

#EOF
