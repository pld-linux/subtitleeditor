#
# TODO: doesn't build with gl enabled
#
Summary:	GTK+ tool to edit subtitles
Summary(pl.UTF-8):	Narzędzie napisane w GTK+ do edycji napisów
Name:		subtitleeditor
Version:	0.38.0
Release:	0.1
License:	GPL v3+
Group:		X11/Applications
Source0:	http://download.gna.org/subtitleeditor/0.38/%{name}-%{version}.tar.gz
# Source0-md5:	2c4d7d4bd79f45effcea279a2e06ca66
URL:		http://home.gna.org/subtitleeditor/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	enchant-devel >= 1.1.0
BuildRequires:	gettext-devel
BuildRequires:	glibmm-devel >= 2.16.3
BuildRequires:	gstreamer-audio-effects-good >= 0.10.5
BuildRequires:	gstreamer-devel >= 0.10
BuildRequires:	gstreamer-plugins-base-devel >= 0.10
BuildRequires:	gstreamermm-devel >= 0.10
BuildRequires:	gtkglextmm-devel >= 1.2.0
BuildRequires:	gtkmm-devel >= 2.12.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	iso-codes
BuildRequires:	libglademm-devel >= 2.4
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libxml++-devel >= 2.20.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk+2
Requires:	gstreamer-imagesink-xv
Requires:	gstreamer-pango
Requires:	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Subtitle Editor is a GTK+ tool to edit subtitles.

%description -l pl.UTF-8
Subtitle Editor jest narzędziem napisanym w GTK+ do edycji napisów.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
#%%configure \
#	--enable-gl

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# remove pt_PT as there is already pt locale
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/pt_PT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/{actions,subtitleformats}/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%update_icon_cache hicolor
%update_desktop_database

%postun
/sbin/ldconfig
%update_icon_cache hicolor
%update_desktop_database_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/subtitleeditor
%attr(755,root,root) %{_libdir}/libsubtitleeditor.so*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%dir %{_libdir}/%{name}/plugins/actions
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libabout.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libadjusttime.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libapplytranslation.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libchangeframerate.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libcombinesubtitles.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libcommand.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libconfigurekeyboardshortcuts.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libdialoguize.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libdocumentmanagement.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libduplicatesubtitle.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libeditcell.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/liberrorchecking.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libextendlength.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libexternalvideoplayer.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libfindandreplace.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libinsertsubtitle.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libitalicize.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libjoindocument.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libmoveafterprecedingsubtitle.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libmovesubtitles.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libplaintext.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libpreferences.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libremovesubtitle.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libreversetextandtranslation.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libscalesubtitles.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libselection.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libspellchecking.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libsplitdocument.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libsplitsubtitle.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libstyleeditor.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libtextcorrection.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libtimemodemanagement.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libvideoplayermanagement.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libviewmanager.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libwaveformmanagement.so
%dir %{_libdir}/%{name}/plugins/subtitleformats
%attr(755,root,root) %{_libdir}/%{name}/plugins/subtitleformats/libadobeencoredvdntsc.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/subtitleformats/libadobeencoredvdpal.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/subtitleformats/libadvancedsubstationalpha.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/subtitleformats/libmicrodvd.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/subtitleformats/libmpl2.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/subtitleformats/libmpsub.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/subtitleformats/libsubrip.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/subtitleformats/libsubstationalpha.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/subtitleformats/libsubtitleeditorproject.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/subtitleformats/libsubviewer2.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/subtitleformats/libtimedtextauthoringformat1.so
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/subtitleeditor.*
%{_pixmapsdir}/*.svg
%{_mandir}/man1/subtitleeditor.1*
