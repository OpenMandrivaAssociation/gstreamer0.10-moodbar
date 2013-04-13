%define         gst_major_ver   0.10
%define         gstlibdir       %{_libdir}/gstreamer-%{gst_major_ver}

Summary:	Moodbar plugin for gstreamer
Name:		gstreamer%{gst_major_ver}-moodbar
Version:	0.1.2
Release:	11
License:	GPL v2
Group:		System/Libraries
Source:		moodbar-%{version}.tar.bz2
URL:		http://amarok.kde.org/wiki/Moodbar
BuildRequires:	fftw3-devel
BuildRequires:	gstreamer%{gst_major_ver}-devel >= %{gst_major_ver}
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





%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1.2-9mdv2011.0
+ Revision: 664936
- mass rebuild

* Sat Mar 12 2011 Funda Wang <fwang@mandriva.org> 0.1.2-8
+ Revision: 643982
- rebuild

* Fri Nov 05 2010 Funda Wang <fwang@mandriva.org> 0.1.2-7mdv2011.0
+ Revision: 593558
- rebuild for gstreamer provides

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.2-6mdv2010.1
+ Revision: 522775
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.1.2-5mdv2010.0
+ Revision: 425053
- rebuild

* Tue Apr 07 2009 Funda Wang <fwang@mandriva.org> 0.1.2-4mdv2009.1
+ Revision: 364968
- use configure2_5x

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.1.2-4mdv2009.0
+ Revision: 221109
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Oct 29 2007 Colin Guthrie <cguthrie@mandriva.org> 0.1.2-3mdv2008.1
+ Revision: 103540
- Provide moodbar


* Wed Feb 28 2007 Nicolas Lécureuil <neoclust@mandriva.org> 0.1.2-2mdv2007.0
+ Revision: 130217
- Fix Group ( thanks rpmdrake :) )

* Tue Feb 06 2007 Colin Guthrie <cguthrie@mandriva.org> 0.1.2-1mdv2007.1
+ Revision: 116942
- Import gstreamer0.10-moodbar

