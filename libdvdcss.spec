%define distsuffix plf

%define major 2
%define libname %mklibname dvdcss %{major}
%define develname %mklibname -d dvdcss

Name:		libdvdcss
Version:	1.2.13
Release:	2
Summary:	Library for accessing DVDs like block device usind deCSS if needed
Group:		System/Libraries
License:	GPLv2+
URL:		http://www.videolan.org/libdvdcss
Source:		%{name}-%{version}.tar.bz2
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
Summary:	A library for accessing DVDs like block device usind deCSS if needed
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

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
Summary:	Development tools for programs which will use the %{name} library
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
The %{name}-devel package includes the header files and static libraries
necessary for developing programs which will manipulate DVDs files using
the %{name} library.

If you are going to develop programs which will manipulate DVDs, you
should install %{name}-devel.  You'll also need to have the %{name}
package installed.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%doc ChangeLog COPYING
%doc %{_docdir}/%{name}
%{_libdir}/*.*a
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc

