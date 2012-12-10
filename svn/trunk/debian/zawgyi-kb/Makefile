
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
	install src/ZawgyiOne20080210.ttf $(DESTDIR)$(FONT_DIR)$(FONT)
	install src/mm $(DESTDIR)$(XKB_DIR)
	install src/mm_orig $(DESTDIR)$(XKB_DIR)
	install src/zawgyikeyboard.pdf $(DESTDIR)$(DATA_DIR)$(PACKAGE)
	install src/AlphaZawgyi.jpg $(DESTDIR)$(DATA_DIR)$(PACKAGE)
	install src/zawgyi.desktop $(DESTDIR)$(APPS_DIR)
	install src/zawgyi.png $(DESTDIR)$(ICONS_DIR)
	

make-install-dirs:
	mkdir -p $(DESTDIR)$(FONT_DIR)$(FONT)
	mkdir -p $(DESTDIR)$(XKB_DIR)
	mkdir -p $(DESTDIR)$(DATA_DIR)$(PACKAGE)
	mkdir -p $(DESTDIR)$(APPS_DIR)
	mkdir -p $(DESTDIR)$(ICONS_DIR)
	

uninstall:
	rm $(DESTDIR)$(XKB_DIR)/mm
	rm $(DESTDIR)$(XKB_DIR)/mm_orig
	rm $(DESTDIR)$(APPS_DIR)/zawgyi.desktop
	rm $(DESTDIR)$(ICONS_DIR)/zawgyi.png
	rm -rf $(DESTDIR)$(FONT_DIR)$(FONT)
	rm -rf $(DESTDIR)$(DATA_DIR)$(PACKAGE)
	rm -rf $(DESTDIR)$(DOC_DIR)$(PACKAGE)

	
clean:
	rm -f *-stamp
	rm -rf debian/$(PACKAGE)
	rm -f debian/files
	find . -type f -iregex '.*~$$'  -print | xargs rm -rf
	find . -type f -iregex '.*\.pyc$$'  -print | xargs rm -rf
	find . -type f -iregex '.*\.bak$$'  -print | xargs rm -rf

.PHONY: all install clean distclean
