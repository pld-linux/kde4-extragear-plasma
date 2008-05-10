
%define		origname	extragear-plasma

Summary:	extragear-plasma
Summary(pl.UTF-8):	extragear-plasma
Name:		kde4-extragear-plasma
Version:	4.0.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/extragear/%{origname}-%{version}.tar.bz2
# Source0-md5:	44ae2fe926572e8424a80d2c64393931
URL:		http://www.kde.org/
BuildRequires:	bzip2-devel
BuildRequires:	cmake
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	qt4-qmake
BuildRequires:	rpmbuild(macros) >= 1.213
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
plasma applets.

%description -l pl.UTF-8
applety dla plasmy.

%package applet-bluemarble
Summary:	plasma-applet
Summary(pl.UTF-8):	plasma-applet
Group:		X11/Applications

%description applet-bluemarble
plasma-applet

%description applet-bluemarble -l pl.UTF-8
plasma-applet

%package applet-comic
Summary:	plasma-applet
Summary(pl.UTF-8):	plasma-applet
Group:		X11/Applications

%description applet-comic
plasma-applet

%description applet-comic -l pl.UTF-8
plasma-applet

%package applet-dict
Summary:	plasma-applet
Summary(pl.UTF-8):	plasma-applet
Group:		X11/Applications

%description applet-dict
plasma-applet

%description applet-dict -l pl.UTF-8
plasma-applet

%package applet-ebn
Summary:	plasma-applet
Summary(pl.UTF-8):	plasma-applet
Group:		X11/Applications

%description applet-ebn
plasma-applet

%description applet-ebn -l pl.UTF-8
plasma-applet

%package applet-fifteenPuzzle
Summary:	plasma-applet
Summary(pl.UTF-8):	plasma-applet
Group:		X11/Applications

%description applet-fifteenPuzzle
plasma-applet

%description applet-fifteenPuzzle -l pl.UTF-8
plasma-applet

%package applet-fileWatcher
Summary:	plasma-applet
Summary(pl.UTF-8):	plasma-applet
Group:		X11/Applications

%description applet-fileWatcher
plasma-applet

%description applet-fileWatcher -l pl.UTF-8
plasma-applet

%package applet-frame
Summary:	plasma-applet
Summary(pl.UTF-8):	plasma-applet
Group:		X11/Applications

%description applet-frame
plasma-applet

%description applet-frame -l pl.UTF-8
plasma-applet

%package applet-kolourpicker
Summary:	plasma-applet
Summary(pl.UTF-8):	plasma-applet
Group:		X11/Applications

%description applet-kolourpicker
plasma-applet

%description applet-kolourpicker -l pl.UTF-8
plasma-applet

%package applet-notes
Summary:	plasma-applet
Summary(pl.UTF-8):	plasma-applet
Group:		X11/Applications

%description applet-notes
plasma-applet

%description applet-notes -l pl.UTF-8
plasma-applet

%package applet-twitter
Summary:	plasma-applet
Summary(pl.UTF-8):	plasma-applet
Group:		X11/Applications

%description applet-twitter
plasma-applet

%description applet-twitter -l pl.UTF-8
plasma-applet

%package engine
Summary:	plasma-engine
Summary(pl.UTF-8):	plasma-engine
Group:		X11/Applications

%description engine
plasma-engine

%description engine -l pl.UTF-8
plasma-engine

%package applet-lancelot
Summary:	New menu for KDE4
Summary(pl.UTF-8):	Nowe menu dla KDE4
Group:		X11/Applications

%description applet-lancelot
New menu for KDE4

%description applet-lancelot -l pl.UTF-8
Nowe menu dla KDE4

%prep
%setup -q -n %{origname}-%{version}

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DSYSCONF_INSTALL_DIR=%{_sysconfdir} \
		../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang lancelot --with-kde
#%find_lang plasma_applet_bluemarble --with-kde
%find_lang plasma_applet_comic --with-kde
%find_lang plasma_applet_dict --with-kde
%find_lang plasma_applet_ebn --with-kde
#%find_lang plasma_applet_fifteenPuzzle --with-kde

%find_lang plasma_applet_fileWatcher --with-kde
%find_lang plasma_applet_frame --with-kde
%find_lang plasma_applet_kolourpicker --with-kde
%find_lang plasma_applet_notes --with-kde
%find_lang plasma_applet_twitter --with-kde

#%find_lang plasma_engine_comic --with-kde
#%find_lang plasma_engine_ebn --with-kde
#%find_lang plasma_engine_twitter --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files applet-bluemarble
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_bluemarble.so
%dir %{_datadir}/apps/plasma-bluemarble
%{_datadir}/apps/plasma-bluemarble/atmosphere.frag
%{_datadir}/apps/plasma-bluemarble/atmosphere.vert
%{_datadir}/apps/plasma-bluemarble/earth-night.png
%{_datadir}/apps/plasma-bluemarble/earth.frag
%{_datadir}/apps/plasma-bluemarble/earth.png
%{_datadir}/apps/plasma-bluemarble/earth.vert
%{_datadir}/kde4/services/plasma-applet-bluemarble.desktop

%files applet-comic -f plasma_applet_comic.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_comic.so
%{_datadir}/kde4/services/plasma-comic-default.desktop

%files applet-dict -f plasma_applet_dict.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_dict.so
%{_datadir}/kde4/services/plasma-dict-default.desktop

%files applet-ebn -f plasma_applet_ebn.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_ebn.so
%{_datadir}/kde4/services/plasma-applet-ebn.desktop

%files applet-fifteenPuzzle
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_fifteenPuzzle.so
%{_iconsdir}/hicolor/scalable/apps/fifteenpuzzle.svgz
%{_datadir}/kde4/services/plasma-applet-fifteenPuzzle.desktop

%files applet-fileWatcher -f plasma_applet_fileWatcher.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_fileWatcher.so
%{_datadir}/kde4/services/plasma-fileWatcher-default.desktop

%files applet-frame -f plasma_applet_frame.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_frame.so
%{_datadir}/apps/desktoptheme/default/widgets/picture-frame-default.svg
%{_datadir}/kde4/services/plasma-frame-default.desktop

%files applet-kolourpicker -f plasma_applet_kolourpicker.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_kolourpicker.so
%{_datadir}/kde4/services/plasma-kolourpicker-default.desktop

%files applet-notes -f plasma_applet_notes.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_notes.so
%{_datadir}/apps/desktoptheme/default/widgets/notes.svg
%{_datadir}/kde4/services/plasma-notes-default.desktop

%files applet-twitter -f plasma_applet_twitter.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_twitter.so
%{_datadir}/apps/desktoptheme/default/widgets/twitter.svg
%{_datadir}/kde4/services/plasma-twitter-default.desktop

%files engine
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_comic.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_ebn.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_twitter.so
%{_datadir}/kde4/services/plasma-dataengine-comic.desktop
%{_datadir}/kde4/services/plasma-dataengine-ebn.desktop
%{_datadir}/kde4/services/plasma-dataengine-twitter.desktop
%dir %{_datadir}/apps/desktoptheme

%files applet-lancelot -f lancelot.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lancelot
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_lancelot.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_lancelot_part.so
%{_datadir}/dbus-1/services/org.kde.lancelot.service
%{_iconsdir}/hicolor/*x*/apps/lancelot.png
%dir %{_datadir}/apps/desktoptheme/default
%{_datadir}/apps/desktoptheme/default/lancelot

%{_datadir}/kde4/services/plasma-applet-lancelot-part.desktop
%{_datadir}/kde4/services/plasma-applet-lancelot.desktop
%dir %{_datadir}/apps/desktoptheme/blue
%{_datadir}/apps/desktoptheme/blue/lancelot
