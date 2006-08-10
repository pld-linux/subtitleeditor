Summary:	GTK+ tool to edit subtitles
Summary(pl):	Narzêdzie w GTK+ do edycji napisów
Name:		subtitleeditor
Version:	0.9.1
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://kitone.free.fr/subtitleeditor/files/%{name}-%{version}.tar.gz
# Source0-md5:	1b47c2931ac8c5479c6846fb5422766e
Patch0:		%{name}-init_aspell.patch
URL:		http://kitone.free.fr/subtitleeditor/
BuildRequires:	aspell-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtkmm-devel >= 2.6
BuildRequires:	gstreamer-devel >= 0.10
BuildRequires:	gstreamer-plugins-base-devel >= 0.10
BuildRequires:	libglademm-devel >= 2.4
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Subtitle Editor is a GTK+ tool to edit subtitles.

%description -l pl
Subtitle Editor jest narzêdziem w GTK+ do edycji napisów.

%prep
%setup -q
%patch0 -p1

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

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog NEWS
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
