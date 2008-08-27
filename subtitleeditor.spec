Summary:	GTK+ tool to edit subtitles
Summary(pl.UTF-8):	Narzędzie w GTK+ do edycji napisów
Name:		subtitleeditor
Version:	0.20.1
Release:	1	
License:	GPL v2
Group:		Applications
Source0:	http://download.gna.org/subtitleeditor/0.20/%{name}-%{version}.tar.gz
# Source0-md5:	faf29dae3906561955718a9b8364817d
URL:		http://home.gna.org/subtitleeditor/
BuildRequires:	aspell-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtkmm-devel >= 2.6
BuildRequires:	gstreamer-devel >= 0.10
BuildRequires:	gstreamer-plugins-base-devel >= 0.10
BuildRequires:	gstreamer-audio-effects-good >= 0.10.5
BuildRequires:	libglademm-devel >= 2.4
BuildRequires:	libtool
BuildRequires:	libxml++-devel
BuildRequires:	pcre-cxx-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Subtitle Editor is a GTK+ tool to edit subtitles.

%description -l pl.UTF-8
Subtitle Editor jest narzędziem w GTK+ do edycji napisów.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_datadir}/locale/pt{_PT,}
%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog NEWS
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/subtitleeditor.*
