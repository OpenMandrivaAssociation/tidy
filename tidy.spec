%define name	tidy
%define version 20090904
%define release %mkrel 4
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
Source0:	http://tidy.sourceforge.net/src/tidy-%{version}.tar.bz2
Patch0:		tidy-20081224cvs-fix-format-errors.patch
Requires:	%{libname} = %{epoch}:%{version}
BuildRequires:	xsltproc
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
%setup -q
%patch0 -p1

%build
sh build/gnuauto/setup.sh
%configure2_5x
%make

# generate man page
console/tidy -xml-help >  htmldoc/tidy-help.xml
console/tidy -xml-config >  htmldoc/tidy-config.xml
xsltproc -o tidy.1 htmldoc/tidy1.xsl  htmldoc/tidy-help.xml

%install
%__rm -rf %{buildroot}
%makeinstall

install -d -m 755 %{buildroot}%{_mandir}/man1
install -m 644 tidy.1 %{buildroot}%{_mandir}/man1/%{name}.1

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
