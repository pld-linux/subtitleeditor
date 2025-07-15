#
# Conditional build:
%bcond_with	opengl	# OpenGL waveform renderer [not ported to gtkmm 3]
#
Summary:	GTK+ tool to edit subtitles
Summary(pl.UTF-8):	Narzędzie napisane w GTK+ do edycji napisów
Name:		subtitleeditor
Version:	0.53.0
Release:	2
License:	GPL v3+
Group:		X11/Applications
Source0:	http://download.gna.org/subtitleeditor/0.53/%{name}-%{version}.tar.gz
# Source0-md5:	bcd3ce93a4759ed3f99a56dc7e4c4e00
Patch0:		%{name}-format.patch
Patch1:		gstreamermm-1.8.patch
URL:		http://home.gna.org/subtitleeditor/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	enchant-devel >= 1.4.0
BuildRequires:	gettext-tools
BuildRequires:	glibmm-devel >= 2.16.3
BuildRequires:	gstreamer-devel >= 1.0
BuildRequires:	gstreamer-plugins-base-devel >= 1.0
BuildRequires:	gstreamermm-devel >= 1.0
%{?with_opengl:BuildRequires:	gtkglextmm-devel >= 1.2.0}
BuildRequires:	gtkmm3-devel >= 3.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	iso-codes
BuildRequires:	libstdc++-devel >= 6:4.3
BuildRequires:	libtool
BuildRequires:	libxml++2-devel >= 2.20.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	enchant >= 1.4.0
Requires:	glibmm >= 2.16.3
Requires:	libxml++2 >= 2.20.0
Suggests:	gstreamer-aac
Suggests:	gstreamer-audio-effects-base
Suggests:	gstreamer-dts
Suggests:	gstreamer-imagesink-xv
Suggests:	gstreamer-libav
Suggests:	gstreamer-pango
Suggests:	gstreamer-plugins-good
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Subtitle Editor is a GTK+ tool to edit subtitles.

%description -l pl.UTF-8
Subtitle Editor jest narzędziem napisanym w GTK+ do edycji napisów.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
%configure \
	--disable-debug \
	%{?with_opengl:--enable-gl}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# API not exported
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libsubtitleeditor.{so,la}
# dlopened plugins
%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/{actions,subtitleformats}/*.la
# remove pt_PT as there is already pt locale
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/pt_PT

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
%attr(755,root,root) %{_libdir}/libsubtitleeditor.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsubtitleeditor.so.0
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
%attr(755,root,root) %{_libdir}/subtitleeditor/plugins/actions/libdocumentsnavigation.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libduplicatesubtitle.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libeditcell.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/liberrorchecking.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libextendlength.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libexternalvideoplayer.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libfindandreplace.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libinsertsubtitle.so
%attr(755,root,root) %{_libdir}/subtitleeditor/plugins/actions/libinsertsubtitlefromkeyframe.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libitalicize.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libjoindocument.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libkeyframesmanagement.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libmoveafterprecedingsubtitle.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libmovesubtitles.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libplaintext.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libpreferences.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libremovesubtitle.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libreversetextandtranslation.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libscalesubtitles.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libselection.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libsortsubtitles.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libspellchecking.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libsplitdocument.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libsplitsubtitle.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libstyleeditor.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libstylize.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libtemplate.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libtextcorrection.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libtimemodemanagement.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libtimingfromplayer.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libtypewriter.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libvideoplayermanagement.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libviewmanager.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libwaveformmanagement.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libbestfit.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libclipboard.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libminimizeduration.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/actions/libstacksubtitles.so
%dir %{_libdir}/%{name}/plugins/subtitleformats
%attr(755,root,root) %{_libdir}/%{name}/plugins/subtitleformats/libadobeencoredvdntsc.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/subtitleformats/libadobeencoredvdpal.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/subtitleformats/libadvancedsubstationalpha.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/subtitleformats/libavidds.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/subtitleformats/libbitc.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/subtitleformats/libdcsubtitle.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/subtitleformats/libmicrodvd.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/subtitleformats/libmpl2.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/subtitleformats/libmpsub.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/subtitleformats/libplaintextformat.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/subtitleformats/libsami.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/subtitleformats/libsbv.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/subtitleformats/libsprucestl.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/subtitleformats/libsubrip.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/subtitleformats/libsubstationalpha.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/subtitleformats/libsubtitleeditorproject.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/subtitleformats/libsubviewer2.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/subtitleformats/libtimedtextauthoringformat1.so
%{_datadir}/%{name}
%{_datadir}/appdata/subtitleeditor.appdata.xml
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/subtitleeditor.*
%{_pixmapsdir}/subtitleeditor.svg
%{_mandir}/man1/subtitleeditor.1*
