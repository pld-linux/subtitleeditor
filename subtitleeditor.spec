Summary:	GTK+ tool to edit subtitles
Summary(pl):	Narz�dzie w GTK+ do edycji napis�w
Name:		subtitleeditor
Version:	0.7.2
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://kitone.free.fr/subtitleeditor/files/%{name}-%{version}.tar.gz
# Source0-md5:	e5f0b5a57defc549034dac7fd94a2bf9
URL:		http://kitone.free.fr/subtitleeditor/
BuildRequires:	aspell-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtkmm-devel >= 2.6
BuildRequires:	libglademm-devel >= 2.4
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Subtitle Editor is a GTK+ tool to edit subtitles.

%description -l pl
Subtitle Editor jest narz�dziem w GTK+ do edycji napis�w.

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

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog NEWS
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
