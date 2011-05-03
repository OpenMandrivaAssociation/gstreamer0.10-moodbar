%define         gst_major_ver   0.10
%define         gstlibdir       %{_libdir}/gstreamer-%{gst_major_ver}

Summary:	Moodbar plugin for gstreamer
Name:		gstreamer%{gst_major_ver}-moodbar
Version:	0.1.2
Release:	%mkrel 9
License:	GPL v2
Group:		System/Libraries
Source:		moodbar-%{version}.tar.bz2
URL:		http://amarok.kde.org/wiki/Moodbar
BuildRequires:	fftw3-devel
BuildRequires:	libgstreamer-devel >= %{gst_major_ver}
BuildRoot:	%{_tmppath}/%{name}-%{version}
Requires:	gstreamer%{gst_major_ver}-plugins-base >= %{gst_major_ver}
Requires:	gstreamer%{gst_major_ver}-plugins-good >= %{gst_major_ver}
Provides:	moodbar = %{version}-%{release}

%description
The Moodbar is an algorithm for creating a colorful visual
representation of the contents of an audio file, giving an idea of its
"mood" (this is a rather fanciful term for the simple analysis it
actually does). The Moodbar was invented by Gavin Wood and Simon
O'Keefe for inclusion in the Amarok music player.

This package contains a GStreamer plugin with elements that are used
in the moodbar analysis, and an application that actually does the
analysis.

%prep
%setup -q -n moodbar-%{version}

%build
%configure2_5x \
	--disable-static
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

rm -f $RPM_BUILD_ROOT%{gstlibdir}/libmoodbar.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/moodbar
%attr(755,root,root) %{gstlibdir}/libmoodbar.so



