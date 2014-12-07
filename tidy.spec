%define apiver 0.99
%define major 0
%define libname %mklibname %{name} %{apiver} %{major}
%define develname %mklibname %name -d

Summary:	Program for tidying up messy HTML
Name:		tidy
Version:	20090904
Release:	14
Epoch:		1
Group:		Text tools
License:	W3C License
URL:		http://tidy.sourceforge.net/
Source0:	http://tidy.sourceforge.net/src/tidy-%{version}.tar.bz2
Patch0:		tidy-20081224cvs-fix-format-errors.patch
Requires:	%{libname} = %{EVRD}
BuildRequires:	xsltproc

%description
tidy is a program for tidying up messy html, for example, when we do 
html in vi, and we make the text italic with the <i> </i> tag some of us may
forget to end the italic text with </i>. tidy fixes this.

Install this if you need a program to help you tidy up your HTML.

%package -n	%{libname}
Summary:	Main library for %{name}
Group:		System/Libraries

%description -n	%{libname}
This package contains the library needed to run programs dynamically
linked with %{name}.

%package -n	%{develname}
Summary:	Headers for developing programs that will use %{name}
Group:		Development/Other
Requires:	%{libname} = %{EVRD}
Provides:	lib%{name}-devel = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n	%{develname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%prep
%setup -q
%patch0 -p1

%build
sh build/gnuauto/setup.sh
%configure2_5x --disable-static
%make

# generate man page
console/tidy -xml-help >  htmldoc/tidy-help.xml
console/tidy -xml-config >  htmldoc/tidy-config.xml
xsltproc -o tidy.1 htmldoc/tidy1.xsl  htmldoc/tidy-help.xml

%install
%__rm -rf %{buildroot}

%makeinstall_std

install -d -m 755 %{buildroot}%{_mandir}/man1
install -m 644 tidy.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%doc htmldoc/*
%{_bindir}/*
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/*.so.*

%files -n %{develname}
%{_includedir}/*
%{_libdir}/*.so


%changelog
* Sun Dec 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1:20090904-5
+ Revision: 737615
- drop the static lib and the libtool *.la file
- various fixes

* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 1:20090904-4
+ Revision: 670680
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1:20090904-3mdv2011.0
+ Revision: 607994
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 1:20090904-2mdv2010.1
+ Revision: 519075
- rebuild

* Fri Sep 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1:20090904-1mdv2010.0
+ Revision: 431461
- new snapshot

* Fri Sep 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1:20081224-1mdv2010.0
+ Revision: 431414
- new CVS snapshot, from Debian
- generate man page from tidy-output
- don't ship API doc

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1:20051026-4mdv2010.0
+ Revision: 427356
- rebuild

* Sat Apr 11 2009 Funda Wang <fwang@mandriva.org> 1:20051026-3mdv2009.1
+ Revision: 366368
- fix str fmt

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1:20051026-3mdv2009.0
+ Revision: 225691
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Fri Feb 01 2008 Funda Wang <fwang@mandriva.org> 1:20051026-2mdv2008.1
+ Revision: 160978
- New devel package policy

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Tue Oct 31 2006 Oden Eriksson <oeriksson@mandriva.com> 20051026-1mdv2007.0
+ Revision: 74471
- Import tidy

* Fri Jan 20 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1:20051026-1mdk
- new version
- %%mkrel

* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 20050415-2mdk
- Rebuild

* Tue Apr 26 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1:20050415-1mdk
- New release 20050415
- spec cleanup

* Sat Jan 22 2005 David Walluck <walluck@mandrake.org> 1:20050120-1mdk
- 20050120
- fix src URL

* Tue Jan 04 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 20041025-2mdk
- it builds perfectly fine with automake1.7 (on 10.0 too, that has no
  automake1.9)
- fix deps

* Sun Dec 05 2004 Guillaume Rousse <guillomovitch@mandrake.org> 20041025-1mdk 
- new version
- fix license spelling
- fix main package requires instead of lib package provides
- switch to automake 1.9

* Sat Jul 17 2004 Charles A Edwards <eslrahc@bellsouth.net> 20040713-2mdk 
- rm obsoletes/provides for hacktidy
- enforce versioing for automake
- fix provides for lib pkg

* Wed Jul 14 2004 Guillaume Rousse <guillomovitch@mandrake.org> 20040713-1mdk 
- new version
- revert to a sane versioning

* Tue Jun 15 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1:0.99-0.20040318.2mdk
- use the %%configure2_5x macro
- fix deps

* Mon Apr 26 2004 David Walluck <walluck@mandrake.org> 1:0.99-0.20040318.1mdk
- 20040318
- add epochs to all Provides/Requires

* Sun Feb 29 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.99-0.20040228.1mdk
- 20040228
- fixed dependencies

* Wed Dec 03 2003 Guillaume Rousse <guillomovitch@mandrake.org> 0.99-0.20031101.1mdk
- 20031101
- fixed lib package name

