%define name	tidy
%define version 20051026
%define release %mkrel 1
%define epoch	1
%define major	0.99
%define libname %mklibname %{name} %{major}

Summary:	Program for tidying up messy HTML
Name:		%{name}
Version:	%{version}
Release:	%{release}
Epoch:		%{epoch}
Group:		Text tools
License:	W3C License
URL:		http://tidy.sourceforge.net/
Source0:	http://tidy.sourceforge.net/src/tidy_src.tar.bz2
Source1:	http://tidy.sourceforge.net/docs/tidy_docs.tar.bz2
Requires:	%{libname} = %{epoch}:%{version}
BuildRequires:	autoconf2.5
BuildRequires:	automake1.7

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

%package -n	%{libname}-devel
Summary:	Headers for developing programs that will use %{name}
Group:		Development/Other
Requires:	%{libname} = %{epoch}:%{version}
Provides:	lib%{name}-devel = %{epoch}:%{version}
Provides:	%{name}-devel = %{epoch}:%{version}

%description -n	%{libname}-devel
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%prep
%setup -q -n %{name}
%setup -q -n %{name} -T -D -b1

%build
%__cp -pr build/gnuauto/* .
libtoolize --copy --force && aclocal-1.7 && autoconf && automake-1.7 --copy --add-missing --foreign
%configure2_5x
%make

%install
%__rm -rf %{buildroot}
%makeinstall

install -d -m 755 %{buildroot}%{_mandir}/man1
install -m 644 htmldoc/man_page.txt %{buildroot}%{_mandir}/man1/%{name}.1

%clean
%__rm -rf %{buildroot}

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc htmldoc/*
%{_bindir}/*
%{_mandir}/man1/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.la
%{_libdir}/*.a
%{_libdir}/*.so


