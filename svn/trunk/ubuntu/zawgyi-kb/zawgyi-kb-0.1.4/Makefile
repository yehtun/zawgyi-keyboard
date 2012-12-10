
PACKAGE=zawgyi-kb
FONT=zawgyi
FONT_DIR= /usr/share/fonts/
XKB_DIR = /usr/share/X11/xkb/symbols/
DATA_DIR = /usr/share/
DOC_DIR = /usr/share/doc/
APPS_DIR = /usr/share/applications/
ICONS_DIR = /usr/share/pixmaps/

all:

install: make-install-dirs
	install ZawgyiOne20071230.ttf $(DESTDIR)$(FONT_DIR)$(FONT)
	install mm $(DESTDIR)$(XKB_DIR)
	install mm_orig $(DESTDIR)$(XKB_DIR)
	install zawgyikeyboard.pdf $(DESTDIR)$(DATA_DIR)$(PACKAGE)
	install AlphaZawgyi.jpg $(DESTDIR)$(DATA_DIR)$(PACKAGE)
	install zawgyi.desktop $(DESTDIR)$(APPS_DIR)
	install zawgyi.png $(DESTDIR)$(ICONS_DIR)
	

make-install-dirs:
	mkdir -p $(DESTDIR)$(FONT_DIR)$(FONT)
	mkdir -p $(DESTDIR)$(XKB_DIR)
	mkdir -p $(DESTDIR)$(DATA_DIR)$(PACKAGE)
	mkdir -p $(DESTDIR)$(APPS_DIR)
	mkdir -p $(DESTDIR)$(ICONS_DIR)
	

uninstall:
	rm $(DESTDIR)$(FONT_DIR)$(FONT)/*.ttf
	rm $(DESTDIR)$(XKB_DIR)/mm
	rm $(DESTDIR)$(XKB_DIR)/mm_orig
	rm $(DESTDIR)$(DOC_DIR)$(PACKAGE)/AUTHORS
	rm $(DESTDIR)$(DOC_DIR)$(PACKAGE)/CREDITS
	rm $(DESTDIR)$(DOC_DIR)$(PACKAGE)/NOTICE
	rm $(DESTDIR)$(DOC_DIR)$(PACKAGE)/README
	rm $(DESTDIR)$(DATA_DIR)$(PACKAGE)/zawgyikeyboard.pdf
	rm $(DESTDIR)$(DATA_DIR)$(PACKAGE)/AlphaZawgyi.jpg
	rm $(DESTDIR)$(APPS_DIR)/zawgyi.desktop
	rm $(DESTDIR)$(ICONS_DIR)/zawgyi.png
	
clean:
	rm -f *-stamp
	rm -rf debian/$(PACKAGE)
	rm -f debian/files
	find . -type f -iregex '.*~$$'  -print | xargs rm -rf
	find . -type f -iregex '.*\.pyc$$'  -print | xargs rm -rf
	find . -type f -iregex '.*\.bak$$'  -print | xargs rm -rf

.PHONY: all install clean distclean

