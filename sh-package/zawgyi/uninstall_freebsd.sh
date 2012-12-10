#!/bin/bash

#    zawgyi-keyboard - zawgyi keyboard installation for FreeBSD Gnome2.
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
FONT_DIR=/usr/local/lib/X11/fonts
DOC_DIR=/usr/local/share/doc
DATA_DIR=/usr/local/share
XKB_DIR=/usr/local/share/X11/xkb/symbols
APPS_DIR=/usr/local/share/applications
ICONS_DIR=/usr/local/share/pixmaps

echo
echo "zawgyi-keyboard  Copyright (C) 2009  lrcmm.org"
echo "This program comes with ABSOLUTELY NO WARRANTY."
echo "This is free software, and you are welcome to redistribute it"
echo "under certain conditions; read the file LICENSE for details."
echo
echo "WARNING: Please run this script only if you installed zawgyi keyboard"
echo "previously from this package. Otherwise you needn't run this script!"
echo

# remove files which had installed by the script which comes with this package.
rm -f $XKB_DIR/mm
rm -f $APPS_DIR/zawgyi.desktop
rm -f $ICONS_DIR/zawgyi.png
rm -rf $DATA_DIR/$FONTNAME
rm -rf $DOC_DIR/$FONTNAME
rm -rf $FONT_DIR/$FONTNAME
 
# restore original 'mm' file
echo "Restoring the original keyboard..."
cp $XKB_DIR/mm_orig $XKB_DIR/mm
sleep 1
echo "zawgyi keyboard is successfully removed!"
echo "Good bye!"
echo

#EOF
