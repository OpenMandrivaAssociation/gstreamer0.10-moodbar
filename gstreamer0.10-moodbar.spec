%define         api   0.10
%define         gstlibdir       %{_libdir}/gstreamer-%{api}

Summary:	Moodbar plugin for gstreamer
Name:		gstreamer%{api}-moodbar
Version:	0.1.2
Release:	18
License:	GPLv2
Group:		System/Libraries
Url:		http://amarok.kde.org/wiki/Moodbar
Source0:	moodbar-%{version}.tar.bz2

BuildRequires:	pkgconfig(fftw3)
BuildRequires:	pkgconfig(gstreamer-%{api})
Requires:	gstreamer%{api}-plugins-base
Requires:	gstreamer%{api}-plugins-good
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
%setup -qn moodbar-%{version}

%build
%configure
%make LIBS='-lm'

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/moodbar
%{gstlibdir}/libmoodbar.so

