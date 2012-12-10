%define fontname    	zawgyi
%define fontdir     	%{_datadir}/fonts/%{fontname}
%define xkbdir	    	%{_datadir}/X11/xkb/symbols
%define appdir		%{_datadir}/applications
%define icondir		%{_datadir}/pixmaps
%define vendor		lrcmm
%define fversion	11


Name:		%{fontname}-keyboard
Version:        1.3
Release:        1%{?dist}
Summary:        Zawgyi Keyboard for Fedora Linux
Group:          User Interface/X
License:        GPLv3
URL:            http://code.google.com/p/zawgyi-keyboard/


Source0:	%{fontname}-keyboard-%{version}.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: 	noarch
BuildRequires:	desktop-file-utils


%description
 This package contains zawgyi font and xkeyboard for Fedora Linux.


%prep
%setup -q -c
unzip -j -L -q %{SOURCE0}


%build
# nothing here


%install
# See /usr/lib/rpm/macros for command macros
%{__rm} -rf %{buildroot}

%{__install} -d -m0755 \
			%{buildroot}%{_datadir}/%{fontname} \
			%{buildroot}%{fontdir} \
			%{buildroot}%{xkbdir} \
			%{buildroot}%{appdir} \
			%{buildroot}%{icondir} 


%{__install} -m 0644 -p COPYING		%{buildroot}%{_datadir}/%{fontname}
%{__install} -m 0644 -p COPYRIGHT	%{buildroot}%{_datadir}/%{fontname}
%{__install} -m 0644 -p LICENSE		%{buildroot}%{_datadir}/%{fontname}
%{__install} -m 0644 -p AUTHORS		%{buildroot}%{_datadir}/%{fontname}
%{__install} -m 0644 -p CREDITS		%{buildroot}%{_datadir}/%{fontname}
%{__install} -m 0644 -p NOTICE		%{buildroot}%{_datadir}/%{fontname}
%{__install} -m 0644 -p README		%{buildroot}%{_datadir}/%{fontname}
%{__install} -m 0644 -p zawgyikeyboard.pdf	%{buildroot}%{_datadir}/%{fontname}
%{__install} -m 0644 -p AlphaZawgyi.jpg	%{buildroot}%{_datadir}/%{fontname} 
%{__install} -m 0644 -p ZawgyiOne20080210.ttf	    %{buildroot}%{fontdir}
%{__install} -m 0644 -p mm			    %{buildroot}%{xkbdir}
%{__install} -m 0644 -p mm_orig			    %{buildroot}%{xkbdir}
%{__install} -m 0644 -p zawgyi.png		    %{buildroot}%{icondir}
%{__install} -m 0644 -p zawgyi.desktop		    %{buildroot}%{appdirdir}


#Create menu entry
#cat > %{buildroot}%{_datadir}/applications/%{fontname} <<EOF
#[Desktop Entry]
#Version=1.0
#Encoding=UTF-8
#Name=Zawgyi Keyboard
#GenericName=Zawgyi Keyboard
#Comment=Zawgyi Keyboard Layout
#Categories=System;X-Red-Hat-Base;X-Fedora;
#Exec=evince "/usr/share/zawgyi/zawgyikeyboard.pdf"
#Terminal=false
#Type=Application
#Icon=/usr/share/pixmaps/zawgyi.png
#StartupNotify=true
#
#EOF


%{_bindir}/desktop-file-install --vendor %{vendor} --delete-original	\
    				--dir 	%{buildroot}%{appdir}	\
				--add-category X-Fedora	%{fontname}.desktop


%clean
%{__rm} -rf %{buildroot}


%post

# Font information caches for fontconfig system. This enables applications that use fontconfig to load fonts more rapidly

if [ -x %{_bindir}/fc-cache ] ; then
    %{_bindir}/fc-cache %{fontdir} || :
fi


%postun
if [ $1 -eq 0 -a -x %{_bindir}/fc-cache ] ; then
    %{_bindir}/fc-cache %{fontdir} || :
fi


%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING LICENSE COPYRIGHT CREDITS NOTICE README
%{fontdir}/ZawgyiOne20080210.ttf
%{xkbdir}/mm
%{xkbdir}/mm_orig
%{icondir}/zawgyi.png
%{appdir}/%{vendor}-%{fontname}.desktop
%{_datadir}/%{fontname}/zawgyikeyboard.pdf
%{_datadir}/%{fontname}/AlphaZawgyi.jpg
%{_datadir}/%{fontname}/AUTHORS
%{_datadir}/%{fontname}/COPYING
%{_datadir}/%{fontname}/COPYRIGHT
%{_datadir}/%{fontname}/CREDITS
%{_datadir}/%{fontname}/NOTICE
%{_datadir}/%{fontname}/README
%{_datadir}/%{fontname}/LICENSE


%changelog
* Sat Jun 13 2009  box02 <thebox02@gmail.com> - 1.3-1
- upgrade zawgyi font ZawgyiOne20071230.ttf to ZawgyiOne20080210.ttf
- update AUTHORS, NOTICE
- modify README, .spec file

* Sat Apr 11 2009  box02 <thebox02@gmail.com> - 1.2-1
- Update new SPEC and add and remove some files

* Sun Dec 21 2008  Saturngod <saturngod@mysteryzillion.org> - 1.1-1
- Build on Fedora as Real rpm package 

* Sun Dec 7 2008  Saturngod <saturngod@mysteryzillion.org> - 1.0-1
- First release. Packed over deb Package
