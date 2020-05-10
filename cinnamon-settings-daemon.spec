%define	cinnamon_desktop_ver	4.4.0

Summary:	Collection of Cinnamon settings plugins
Summary(pl.UTF-8):	Zbiór wtyczek do ustawień środowiska Cinnamon
Name:		cinnamon-settings-daemon
Version:	4.4.0
Release:	1
License:	GPL v2+
Group:		Applications
#Source0Download: https://github.com/linuxmint/cinnamon-settings-daemon/releases
Source0:	https://github.com/linuxmint/cinnamon-settings-daemon/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	51060a85e4922588f8ba5e120e79fcd2
# https://github.com/linuxmint/cinnamon-settings-daemon/commit/4c19a41429524a2da202b919a335a646103da0fd.patch
Patch0:		%{name}-restore_old_logind_check.patch
URL:		https://github.com/linuxmint/cinnamon-settings-daemon
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake >= 1:1.9
BuildRequires:	cinnamon-desktop-devel >= %{cinnamon_desktop_ver}
BuildRequires:	colord-devel >= 0.1.27
BuildRequires:	cups-devel >= 1.4
BuildRequires:	dbus-devel >= 1.1.2
BuildRequires:	dbus-glib-devel
#BuildRequires:	desktop-file-utils
BuildRequires:	fontconfig-devel
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.38.0
BuildRequires:	gtk+3-devel >= 3.9.10
BuildRequires:	intltool >= 0.37.1
BuildRequires:	lcms2-devel >= 2.2
BuildRequires:	libcanberra-gtk3-devel
BuildRequires:	libgnomekbd-devel >= 3.6.0
BuildRequires:	libnma-devel
BuildRequires:	libnotify-devel >= 0.7.3
BuildRequires:	librsvg-devel >= 2.36.2
BuildRequires:	libtool
BuildRequires:	libxklavier-devel >= 5.0
BuildRequires:	libxslt
BuildRequires:	nss-devel >= 3.11.2
BuildRequires:	pkgconfig
BuildRequires:	polkit-devel >= 0.97
BuildRequires:	pulseaudio-devel >= 0.9.16
BuildRequires:	systemd-devel >= 1:209
BuildRequires:	udev-glib-devel
BuildRequires:	upower-devel >= 0.9.11
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	xorg-proto-kbproto-devel
%ifnarch s390 s390x
BuildRequires:	libwacom-devel >= 0.7
BuildRequires:	xorg-driver-input-wacom-devel
%endif
# add hard cinnamon-desktop required version due logind schema
Requires:	cinnamon-desktop >= %{cinnamon_desktop_ver}
Requires:	colord >= 0.1.27
Requires:	cups-lib >= 1.4
Requires:	dbus >= 1.1.2
Requires:	glib2 >= 1:2.38.0
Requires:	gtk+3 >= 3.9.10
Requires:	ibus
Requires:	iio-sensor-proxy
Requires:	lcms2 >= 2.2
Requires:	libgnomekbd >= 3.6.0
%ifnarch s390 s390x
Requires:	libwacom >= 0.7
%endif
Requires:	libnotify >= 0.7.3
Requires:	librsvg >= 2.36.2
Requires:	libxklavier >= 5.0
Requires:	nss >= 3.11.2
Requires:	polkit >= 0.97
Requires:	pulseaudio-libs >= 0.9.16
Requires:	systemd-libs >= 1:209
Requires:	upower >= 0.9.11
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Collection of Cinnamon settings plugins, started by cinnamon-session
when you log in.

%description -l pl.UTF-8
Zbiór wtyczek do ustawień środowiska Cinnamon, uruchamianych przez
cinnamon-session przy logowaniu.

%package devel
Summary:	Development files for Cinnamon settings daemon
Summary(pl.UTF-8):	Pliki programistyczne demona ustawień środowiska Cinnamon
Group:		Development/Libraries
# doesn't require base

%description devel
Development files for Cinnamon settings daemon.

%description devel -l pl.UTF-8
Pliki programistyczne demona ustawień środowiska Cinnamon.

%prep
%setup -q
%patch0 -p1

%build
install -d m4
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/cinnamon-settings-daemon-3.0/libcsd.la

# example script, packaged as %doc
%{__rm} $RPM_BUILD_ROOT%{_datadir}/cinnamon-settings-daemon-3.0/input-device-example.sh

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS MAINTAINERS README.rst plugins/common/input-device-example.sh
%dir %{_libdir}/cinnamon-settings-daemon-3.0/
%attr(755,root,root) %{_libexecdir}/csd-a11y-keyboard
%attr(755,root,root) %{_libexecdir}/csd-a11y-settings
%attr(755,root,root) %{_libexecdir}/csd-automount
%attr(755,root,root) %{_libexecdir}/csd-background
%attr(755,root,root) %{_libexecdir}/csd-backlight-helper
%attr(755,root,root) %{_libexecdir}/csd-clipboard
%attr(755,root,root) %{_libexecdir}/csd-color
%attr(755,root,root) %{_libexecdir}/csd-cursor
%attr(755,root,root) %{_libexecdir}/csd-datetime-mechanism
%attr(755,root,root) %{_libexecdir}/csd-dummy
%attr(755,root,root) %{_libexecdir}/csd-housekeeping
%attr(755,root,root) %{_libexecdir}/csd-input-helper
%attr(755,root,root) %{_libexecdir}/csd-keyboard
%attr(755,root,root) %{_libexecdir}/csd-locate-pointer
%attr(755,root,root) %{_libexecdir}/csd-media-keys
%attr(755,root,root) %{_libexecdir}/csd-mouse
%attr(755,root,root) %{_libexecdir}/csd-orientation
%attr(755,root,root) %{_libexecdir}/csd-power
%attr(755,root,root) %{_libexecdir}/csd-printer
%attr(755,root,root) %{_libexecdir}/csd-print-notifications
%attr(755,root,root) %{_libexecdir}/csd-screensaver-proxy
%attr(755,root,root) %{_libexecdir}/csd-smartcard
%attr(755,root,root) %{_libexecdir}/csd-sound
%attr(755,root,root) %{_libexecdir}/csd-xrandr
%attr(755,root,root) %{_libexecdir}/csd-xsettings
%ifnarch s390 s390x
%attr(755,root,root) %{_libexecdir}/csd-list-wacom
%attr(755,root,root) %{_libexecdir}/csd-wacom
%attr(755,root,root) %{_libexecdir}/csd-wacom-led-helper
%attr(755,root,root) %{_libexecdir}/csd-wacom-osd
%endif
%attr(755,root,root) %{_libdir}/cinnamon-settings-daemon-3.0/libcsd.so
%config /etc/dbus-1/system.d/org.cinnamon.SettingsDaemon.DateTimeMechanism.conf
%{_sysconfdir}/xdg/autostart/cinnamon-settings-daemon-a11y-keyboard.desktop
%{_sysconfdir}/xdg/autostart/cinnamon-settings-daemon-a11y-settings.desktop
%{_sysconfdir}/xdg/autostart/cinnamon-settings-daemon-automount.desktop
%{_sysconfdir}/xdg/autostart/cinnamon-settings-daemon-background.desktop
%{_sysconfdir}/xdg/autostart/cinnamon-settings-daemon-clipboard.desktop
%{_sysconfdir}/xdg/autostart/cinnamon-settings-daemon-color.desktop
%{_sysconfdir}/xdg/autostart/cinnamon-settings-daemon-cursor.desktop
%{_sysconfdir}/xdg/autostart/cinnamon-settings-daemon-housekeeping.desktop
%{_sysconfdir}/xdg/autostart/cinnamon-settings-daemon-keyboard.desktop
%{_sysconfdir}/xdg/autostart/cinnamon-settings-daemon-media-keys.desktop
%{_sysconfdir}/xdg/autostart/cinnamon-settings-daemon-mouse.desktop
%{_sysconfdir}/xdg/autostart/cinnamon-settings-daemon-orientation.desktop
%{_sysconfdir}/xdg/autostart/cinnamon-settings-daemon-power.desktop
%{_sysconfdir}/xdg/autostart/cinnamon-settings-daemon-print-notifications.desktop
%{_sysconfdir}/xdg/autostart/cinnamon-settings-daemon-screensaver-proxy.desktop
%{_sysconfdir}/xdg/autostart/cinnamon-settings-daemon-smartcard.desktop
%{_sysconfdir}/xdg/autostart/cinnamon-settings-daemon-sound.desktop
%{_sysconfdir}/xdg/autostart/cinnamon-settings-daemon-wacom.desktop
%{_sysconfdir}/xdg/autostart/cinnamon-settings-daemon-xrandr.desktop
%{_sysconfdir}/xdg/autostart/cinnamon-settings-daemon-xsettings.desktop
%{_datadir}/cinnamon-settings-daemon
%{_datadir}/dbus-1/system-services/org.cinnamon.SettingsDaemon.DateTimeMechanism.service
%{_datadir}/glib-2.0/schemas/org.cinnamon.settings-daemon.enums.xml
%{_datadir}/glib-2.0/schemas/org.cinnamon.settings-daemon.*.gschema.xml
%{_datadir}/polkit-1/actions/org.cinnamon.settings*.policy
%{_desktopdir}/csd-automount.desktop
%{_iconsdir}/hicolor/*x*/apps/csd-*.png
%{_iconsdir}/hicolor/scalable/apps/csd-*.svg

%files devel
%defattr(644,root,root,755)
%{_includedir}/cinnamon-settings-daemon-3.0
%{_pkgconfigdir}/cinnamon-settings-daemon.pc
