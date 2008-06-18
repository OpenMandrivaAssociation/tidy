%define name	tidy
%define version 20051026
%define release %mkrel 3
%define epoch	1
%define apiver	0.99
%define major	0
%define libname %mklibname %{name} %{apiver} %{major}
%define develname %mklibname %name -d

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
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
tidy is a program for tidying up messy html, for example, when we do 
html in vi, and we make the text italic with the <i> </i> tag some of us may
forget to end the italic text with </i>. tidy fixes this.

Install this if you need a program to help you tidy up your HTML.

%package -n	%{libname}
Summary:	Main library for %{name}
Group:		System/Libraries
Obsoletes:	%mklibname tidy 0.99

%description -n	%{libname}
This package contains the library needed to run programs dynamically
linked with %{name}.

%package -n	%{develname}
Summary:	Headers for developing programs that will use %{name}
Group:		Development/Other
Requires:	%{libname} = %{epoch}:%{version}
Provides:	lib%{name}-devel = %{epoch}:%{version}
Provides:	%{name}-devel = %{epoch}:%{version}
Obsoletes:	%mklibname -d tidy 0
Obsoletes:	%mklibname -d tidy 0.99

%description -n	%{develname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%prep
%setup -q -n %{name}
%setup -q -n %{name} -T -D -b1

%build
sh build/gnuauto/setup.sh
%configure2_5x
%make

%install
%__rm -rf %{buildroot}
%makeinstall

install -d -m 755 %{buildroot}%{_mandir}/man1
install -m 644 htmldoc/man_page.txt %{buildroot}%{_mandir}/man1/%{name}.1

%clean
%__rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root)
%doc htmldoc/*
%{_bindir}/*
%{_mandir}/man1/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.la
%{_libdir}/*.a
%{_libdir}/*.so


