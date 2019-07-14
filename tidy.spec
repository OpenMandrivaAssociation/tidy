%define major 5
%define libname %mklibname %{name} %{major}
%define develname %mklibname %name -d

Summary:	Program for tidying up messy HTML
Name:		tidy
Version:	5.7.28
Release:	1
Epoch:		2
Group:		Text tools
License:	W3C License
URL:		http://tidy.sourceforge.net/
Source0:	https://github.com/htacg/tidy-html5/archive/%{version}/%{name}-html5-%{version}.tar.gz
Requires:	%{libname} = %{EVRD}
BuildRequires:	xsltproc
BuildRequires:	cmake

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
%setup -qn %{name}-html5-%{version}
%apply_patches

%build
%cmake \
	-DTIDY_COMPAT_HEADERS:BOOL=ON \
	-DBUILD_TAB2SPACE:BOOL=ON
%make

# generate man page
#console/tidy -xml-help >  htmldoc/tidy-help.xml
#console/tidy -xml-config >  htmldoc/tidy-config.xml
#xsltproc -o tidy.1 htmldoc/tidy1.xsl  htmldoc/tidy-help.xml

%install
%makeinstall_std -C build

#install -d -m 755 %{buildroot}%{_mandir}/man1
#install -m 644 tidy.1 %{buildroot}%{_mandir}/man1/%{name}.1

rm -fv %{buildroot}%{_libdir}/libtidys.a

%files
%doc README.md
%{_bindir}/*
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/*.so.*

%files -n %{develname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/tidy.pc

