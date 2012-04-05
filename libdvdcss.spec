%define name 	libdvdcss
%define version	1.2.10
%define distsuffix plf
%define release	%mkrel 3
%define major  	2
%define libname %mklibname dvdcss %{major}
%define develname %mklibname -d dvdcss

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Library for accessing DVDs like block device usind deCSS if needed
Source:		%{name}-%{version}.tar.bz2
Patch:		libdvdcss-1.2.10-format-strings.patch
License:	GPLv2+
Group:		System/Libraries
URL:		http://www.videolan.org/libdvdcss
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
Conflicts:	libdvdcss0.0.1
Conflicts:	libdvdcss0.0.2

%description
libdvdcss is a simple library designed for accessing DVDs like a block device
without having to bother about the decryption. The important features are:
 * Portability. Currently supported platforms are GNU/Linux, FreeBSD, NetBSD,
   OpenBSD, BSD/OS, BeOS, Windows 95/98, Windows NT/2000, MacOS X, Solaris,
   and HP-UX.
 * Simplicity. There are currently 7 functions in the API, and we intend to
   keep this number low.
 * Freedom. libdvdcss is released under the General Public License, ensuring
   it will stay free, and used only for free software products.
 * Just better. Unlike most similar projects, libdvdcss doesn't require the
   region of your drive to be set.

This package is in restricted as it violates patents.

%package -n %{libname}
Summary:        A library for accessing DVDs like block device usind deCSS if needed
Group:          System/Libraries
Provides:       %{name} = %{version}-%{release}

%description -n %{libname}
libdvdcss is a simple library designed for accessing DVDs like a block device
without having to bother about the decryption. The important features are:
 * Portability. Currently supported platforms are GNU/Linux, FreeBSD, NetBSD,
   OpenBSD, BSD/OS, BeOS, Windows 95/98, Windows NT/2000, MacOS X, Solaris,
   and HP-UX.
 * Simplicity. There are currently 7 functions in the API, and we intend to
   keep this number low.
 * Freedom. libdvdcss is released under the General Public License, ensuring
   it will stay free, and used only for free software products.
 * Just better. Unlike most similar projects, libdvdcss doesn't require the
   region of your drive to be set.

%package -n %{develname}
Summary:        Development tools for programs which will use the %{name} library
Group:          Development/C
Requires:	%{libname} = %{version}
Provides:       %{name}-devel = %{version}-%{release}
Obsoletes: %mklibname -d dvdcss 2
 
%description -n %{develname}
The %{name}-devel package includes the header files and static libraries
necessary for developing programs which will manipulate DVDs files using
the %{name} library.
 
If you are going to develop programs which will manipulate DVDs, you
should install %{name}-devel.  You'll also need to have the %{name}
package installed.

%prep
%setup -q
%patch -p1

%build
%if %mdkversion <= 1000
%define __libtoolize true
%endif
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{lib_name} -p /sbin/ldconfig
%postun -n %{lib_name} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS COPYING
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc ChangeLog COPYING
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc

%changelog
* Fri Aug 19 2011 Andrey Bondrov <bondrov@math.dvgu.ru> 1.2.10-3plf2011.0
- Port from PLF to restricted
- Spec clean up

* Sun Aug 30 2009 Götz Waschk <goetz@zarb.org> 1.2.10-2plf2010.0
- update license
- fix format strings

* Fri Aug 29 2008 Götz Waschk <goetz@zarb.org> 1.2.10-1plf2009.0
- update file list
- new version

* Mon Jan 21 2008 Götz Waschk <goetz@zarb.org> 1.2.9-4plf2008.1
- fix plf reason
- new devel name

* Mon Aug 28 2006 Götz Waschk <goetz@zarb.org> 1.2.9-3plf2007.0
- rebuild

* Tue Jul 12 2005 Götz Waschk <goetz@zarb.org> 1.2.9-2plf
- fix backports

* Mon Jul 11 2005 trem <trem@zarb.org> 1.2.9-1plf
- 1.2.9

* Mon Mar 28 2005 Olivier Thauvin <nanardon@zarb.org> 1.2.8-3plf
- rebuild && %%mkrel

* Mon Sep 20 2004 Götz Waschk <goetz@zarb.org> 1.2.8-2plf
- update description
- use mklibname macro

* Wed Jul 30 2003 Götz Waschk <goetz@plf.zarb.org> 1.2.8-1plf
- autoconf 2.5 macro
- new version

* Mon Jun 23 2003 Guillaume Rousse <guillomovitch@zarb.org> 1.2.7-1plf
- 1.2.7
- purged any redhat heresy trace

* Tue Mar 11 2003 Götz Waschk <goetz@plf.zarb.org> 1.2.6-1plf
- new version

* Thu Nov 21 2002 Yves Duret <yves@zarb.org> 1.2.4-1plf
- new upstream version.

* Mon Oct 21 2002 Götz Waschk <waschk@informatik.uni-rostock.de> 1.2.3-1plf
- new version

* Mon Aug 12 2002 Götz Waschk <waschk@informatik.uni-rostock.de> 1.2.2-1plf
- new version

* Sun Jun 02 2002 Yves Duret <yduret@mandrakesoft.com> 1.2.1-1plf
- 1.2.1 by Samuel Hocevar <sam@zoy.org>
  * new upstream release
  * fix for a crash on disc/drive region mismatch

* Thu May 23 2002 Yves Duret <yduret@mandrakesoft.com> 1.2.0-1plf
- 1.2.0 by Samuel Hocevar <sam@zoy.org>
  * new upstream release
  * weird libxalf dependency is gone

* Sun Apr 07 2002 Yves Duret <yduret@mandrakesoft.com> 1.1.1-2plf
- major version is 2 (aka guillaume sux).
- spec clean up: do not rm in %prep, %%buildroot, %%makeinstall_std, %%provides %%version-%%release
- added doc in devel
- sync with cvs's one (%%description,%%files, conflicts).
- fix url

* Sat Apr 06 2002 Guillaume Rousse <rousse@ccr.jussieu.fr> 1.1.1-1plf
- 1.1.1

* Wed Jan 30 2002 Guillaume Rousse <rousse@ccr.jussieu.fr> 1.0.0-3plf 
- new plf extension

* Wed Dec 05 2001 Guillaume Rousse <g.rousse@linux-mandrake.com> 1.0.0-3mdk
- removed conflict

* Tue Dec 04 2001 Guillaume Rousse <g.rousse@linux-mandrake.com> 1.0.0-2mdk
- contributed to PLF by Yves Duret <yduret@mandrakesoft.com>
- Conflicts: libdvdcss-ogle
- more doc files
- no doc file for devel package

* Fri Nov 30 2001 Yves Duret <yduret@mandrakesoft.com> 1.0.0-1mdk
- version 1.0.0

* Thu Aug 23 2001 Yves Duret <yduret@mandrakesoft.com> 0.0.3-1mdk
- version 0.0.3

* Mon Aug 13 2001 Yves Duret <yduret@mandrakesoft.com> 0.0.2-1mdk
- version 0.0.2

* Tue Jun 19 2001 Yves Duret <yduret@mandrakesoft.com> 0.0.1-1mdk
- first release and first mdk release
