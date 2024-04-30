%define	translations_version	6.0.2
%define	cinnamon_desktop_ver	4.8.0

Summary:	Collection of Cinnamon settings plugins
Summary(pl.UTF-8):	Zbiór wtyczek do ustawień środowiska Cinnamon
Name:		cinnamon-settings-daemon
Version:	6.0.0
Release:	1
License:	GPL v2+
Group:		Applications
#Source0Download: https://github.com/linuxmint/cinnamon-settings-daemon/tags
Source0:	https://github.com/linuxmint/cinnamon-settings-daemon/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	2196db65d92eb9a768942c4491a8e292
#Source1Download: https://github.com/linuxmint/cinnamon-translations/tags
Source1:	https://github.com/linuxmint/cinnamon-translations/archive/%{translations_version}/cinnamon-translations-%{translations_version}.tar.gz
# Source1-md5:	36552df46587be4e32ac311b8d7084e4
URL:		https://github.com/linuxmint/cinnamon-settings-daemon
BuildRequires:	cinnamon-desktop-devel >= %{cinnamon_desktop_ver}
BuildRequires:	colord-devel >= 0.1.27
BuildRequires:	cups-devel >= 1.4
BuildRequires:	dbus-devel >= 1.1.2
BuildRequires:	fontconfig-devel
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.40.0
BuildRequires:	gtk+3-devel >= 3.14.0
BuildRequires:	lcms2-devel >= 2.2
BuildRequires:	libcanberra-gtk3-devel
BuildRequires:	libgnomekbd-devel >= 3.6.0
BuildRequires:	libnma-devel
BuildRequires:	libnotify-devel >= 0.7.3
BuildRequires:	librsvg-devel >= 2.36.2
BuildRequires:	libxklavier-devel >= 5.0
BuildRequires:	libxslt-progs
BuildRequires:	meson >= 0.56.0
BuildRequires:	ninja >= 1.5
BuildRequires:	nss-devel >= 3.11.2
BuildRequires:	pango-devel >= 1:1.20.0
BuildRequires:	pkgconfig
BuildRequires:	polkit-devel >= 0.97
BuildRequires:	pulseaudio-devel >= 0.9.16
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	systemd-devel >= 1:209
BuildRequires:	udev-glib-devel
BuildRequires:	upower-devel >= 0.9.11
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
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
Requires:	glib2 >= 1:2.40.0
Requires:	gtk+3 >= 3.14.0
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
Requires:	glib2-devel >= 1:2.40.0
# doesn't require base

%description devel
Development files for Cinnamon settings daemon.

%description devel -l pl.UTF-8
Pliki programistyczne demona ustawień środowiska Cinnamon.

%prep
%setup -q -a1

%build
%meson build \
	--default-library=shared

%ninja_build -C build

%{__make} -C cinnamon-translations-%{translations_version}

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

# example script, packaged as %doc
%{__rm} $RPM_BUILD_ROOT%{_datadir}/cinnamon-settings-daemon-3.0/input-device-example.sh

cd cinnamon-translations-%{translations_version}
for f in usr/share/locale/*/LC_MESSAGES/%{name}.mo ; do
	install -D "$f" "$RPM_BUILD_ROOT/$f"
done
cd ..

# not supported by glibc
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{ie,rue,zgh}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README.rst debian/changelog plugins/common/input-device-example.sh
%attr(755,root,root) %{_bindir}/csd-a11y-settings
%attr(755,root,root) %{_bindir}/csd-automount
%attr(755,root,root) %{_bindir}/csd-background
%attr(755,root,root) %{_bindir}/csd-backlight-helper
%attr(755,root,root) %{_bindir}/csd-clipboard
%attr(755,root,root) %{_bindir}/csd-color
%attr(755,root,root) %{_bindir}/csd-datetime-mechanism
%attr(755,root,root) %{_bindir}/csd-housekeeping
%attr(755,root,root) %{_bindir}/csd-input-helper
%attr(755,root,root) %{_bindir}/csd-keyboard
%attr(755,root,root) %{_bindir}/csd-media-keys
%attr(755,root,root) %{_bindir}/csd-power
%attr(755,root,root) %{_bindir}/csd-print-notifications
%attr(755,root,root) %{_bindir}/csd-printer
%attr(755,root,root) %{_bindir}/csd-screensaver-proxy
%attr(755,root,root) %{_bindir}/csd-settings-remap
%attr(755,root,root) %{_bindir}/csd-smartcard
%attr(755,root,root) %{_bindir}/csd-xsettings
%ifnarch s390 s390x
%attr(755,root,root) %{_bindir}/csd-wacom
%endif
%attr(755,root,root) %{_libexecdir}/csd-a11y-settings
%attr(755,root,root) %{_libexecdir}/csd-automount
%attr(755,root,root) %{_libexecdir}/csd-background
%attr(755,root,root) %{_libexecdir}/csd-backlight-helper
%attr(755,root,root) %{_libexecdir}/csd-clipboard
%attr(755,root,root) %{_libexecdir}/csd-color
%attr(755,root,root) %{_libexecdir}/csd-datetime-mechanism
%attr(755,root,root) %{_libexecdir}/csd-housekeeping
%attr(755,root,root) %{_libexecdir}/csd-input-helper
%attr(755,root,root) %{_libexecdir}/csd-keyboard
%attr(755,root,root) %{_libexecdir}/csd-media-keys
%attr(755,root,root) %{_libexecdir}/csd-power
%attr(755,root,root) %{_libexecdir}/csd-print-notifications
%attr(755,root,root) %{_libexecdir}/csd-printer
%attr(755,root,root) %{_libexecdir}/csd-screensaver-proxy
%attr(755,root,root) %{_libexecdir}/csd-settings-remap
%attr(755,root,root) %{_libexecdir}/csd-smartcard
%attr(755,root,root) %{_libexecdir}/csd-xsettings
%ifnarch s390 s390x
%attr(755,root,root) %{_libexecdir}/csd-wacom
%attr(755,root,root) %{_libexecdir}/csd-wacom-led-helper
%attr(755,root,root) %{_libexecdir}/csd-wacom-oled-helper
%endif
%dir %{_libdir}/cinnamon-settings-daemon
%attr(755,root,root) %{_libdir}/cinnamon-settings-daemon/csd-a11y-settings
%attr(755,root,root) %{_libdir}/cinnamon-settings-daemon/csd-automount
%attr(755,root,root) %{_libdir}/cinnamon-settings-daemon/csd-background
%attr(755,root,root) %{_libdir}/cinnamon-settings-daemon/csd-backlight-helper
%attr(755,root,root) %{_libdir}/cinnamon-settings-daemon/csd-clipboard
%attr(755,root,root) %{_libdir}/cinnamon-settings-daemon/csd-color
%attr(755,root,root) %{_libdir}/cinnamon-settings-daemon/csd-datetime-mechanism
%attr(755,root,root) %{_libdir}/cinnamon-settings-daemon/csd-housekeeping
%attr(755,root,root) %{_libdir}/cinnamon-settings-daemon/csd-input-helper
%attr(755,root,root) %{_libdir}/cinnamon-settings-daemon/csd-keyboard
%attr(755,root,root) %{_libdir}/cinnamon-settings-daemon/csd-media-keys
%attr(755,root,root) %{_libdir}/cinnamon-settings-daemon/csd-power
%attr(755,root,root) %{_libdir}/cinnamon-settings-daemon/csd-print-notifications
%attr(755,root,root) %{_libdir}/cinnamon-settings-daemon/csd-printer
%attr(755,root,root) %{_libdir}/cinnamon-settings-daemon/csd-screensaver-proxy
%attr(755,root,root) %{_libdir}/cinnamon-settings-daemon/csd-settings-remap
%attr(755,root,root) %{_libdir}/cinnamon-settings-daemon/csd-smartcard
%attr(755,root,root) %{_libdir}/cinnamon-settings-daemon/csd-xsettings
%ifnarch s390 s390x
%attr(755,root,root) %{_libdir}/cinnamon-settings-daemon/csd-wacom
%endif

%dir %{_libdir}/cinnamon-settings-daemon-3.0
%attr(755,root,root) %{_libdir}/cinnamon-settings-daemon-3.0/libcsd.so
%{_sysconfdir}/xdg/autostart/cinnamon-settings-daemon-a11y-settings.desktop
%{_sysconfdir}/xdg/autostart/cinnamon-settings-daemon-automount.desktop
%{_sysconfdir}/xdg/autostart/cinnamon-settings-daemon-background.desktop
%{_sysconfdir}/xdg/autostart/cinnamon-settings-daemon-clipboard.desktop
%{_sysconfdir}/xdg/autostart/cinnamon-settings-daemon-color.desktop
%{_sysconfdir}/xdg/autostart/cinnamon-settings-daemon-housekeeping.desktop
%{_sysconfdir}/xdg/autostart/cinnamon-settings-daemon-keyboard.desktop
%{_sysconfdir}/xdg/autostart/cinnamon-settings-daemon-media-keys.desktop
%{_sysconfdir}/xdg/autostart/cinnamon-settings-daemon-power.desktop
%{_sysconfdir}/xdg/autostart/cinnamon-settings-daemon-print-notifications.desktop
%{_sysconfdir}/xdg/autostart/cinnamon-settings-daemon-screensaver-proxy.desktop
%{_sysconfdir}/xdg/autostart/cinnamon-settings-daemon-settings-remap.desktop
%{_sysconfdir}/xdg/autostart/cinnamon-settings-daemon-smartcard.desktop
%{_sysconfdir}/xdg/autostart/cinnamon-settings-daemon-wacom.desktop
%{_sysconfdir}/xdg/autostart/cinnamon-settings-daemon-xsettings.desktop
%{_datadir}/cinnamon-settings-daemon
%{_datadir}/dbus-1/system-services/org.cinnamon.SettingsDaemon.DateTimeMechanism.service
%{_datadir}/dbus-1/system.d/org.cinnamon.SettingsDaemon.DateTimeMechanism.conf
%{_datadir}/glib-2.0/schemas/org.cinnamon.settings-daemon.enums.xml
%{_datadir}/glib-2.0/schemas/org.cinnamon.settings-daemon.*.gschema.xml
%{_datadir}/polkit-1/actions/org.cinnamon.settings-daemon.plugins.*.policy
%{_datadir}/polkit-1/actions/org.cinnamon.settingsdaemon.datetimemechanism.policy
%{_desktopdir}/csd-automount.desktop
%{_iconsdir}/hicolor/*x*/apps/csd-*.png
%{_iconsdir}/hicolor/scalable/apps/csd-*.svg

%files devel
%defattr(644,root,root,755)
%{_includedir}/cinnamon-settings-daemon-3.0
%{_pkgconfigdir}/cinnamon-settings-daemon.pc
