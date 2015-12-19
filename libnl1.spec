#
# Conditional build:
%bcond_without	apidocs		# don't build api docs

Summary:	Netlink sockets library
Summary(pl.UTF-8):	Biblioteka do obsługi gniazd netlink
Name:		libnl1
Version:	1.1.4
Release:	4
License:	LGPL v2.1
Group:		Libraries
Source0:	http://people.suug.ch/~tgr/libnl/files/libnl-%{version}.tar.gz
# Source0-md5:	580cb878be536804daca87fb75ae46cc
Patch4:		libnl-1.0-pre8-more-build-output.patch
Patch5:		libnl-1.1-include-limits-h.patch
Patch6:		libnl-1.1-doc-inlinesrc.patch
URL:		http://www.infradead.org/~tgr/libnl/
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_apidocs:BuildRequires:	doxygen}
%{?with_apidocs:BuildRequires:	graphviz}
BuildRequires:	linux-libc-headers >= 6:2.6.23
%{?with_apidocs:BuildRequires:	tetex-dvips}
%{?with_apidocs:BuildRequires:	tetex-format-latex}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libnl1 is a library for applications dealing with netlink socket. It
provides an easy to use interface for raw netlink message but also
netlink family specific APIs.

%description -l pl.UTF-8
libnl1 jest biblioteką dla aplikacji rozmawiających z gniazdem
netlink. Udostępnia łatwy w użyciu interfejs do korzystania z surowych
wiadomości netlink, a także API specyficzne dla rodziny gniazd
netlink.

%package devel
Summary:	Header files for libnl1 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libnl1
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Conflicts:	libnl-devel < 1:3.2

%description devel
Header files for libnl1 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libnl1.

%package static
Summary:	Static libnl1 library
Summary(pl.UTF-8):	Statyczna biblioteka libnl1
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Conflicts:	libnl-static < 1:3.2

%description static
Static libnl1 library.

%description static -l pl.UTF-8
Statyczna biblioteka libnl1.

%package apidocs
Summary:	libnl1 library API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki libnl1
Group:		Documentation
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
Documentation for libnl1 library API and guides in HTML format
generated from sources by doxygen.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libnl1 oraz wprowadzenie w formacie HTML
wygenerowane ze źródeł za pomocą doxygena.

%prep
%setup -q -n libnl-%{version}
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
%{__aclocal}
%{__autoconf}

%configure \
	--enable-static \
	--enable-verbose-errors

%{__make}
%{?with_apidocs:%{__make} -C doc gendoc}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# for autodeps to work
chmod +x $RPM_BUILD_ROOT%{_libdir}/libnl.so.*.*

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_libdir}/libnl.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libnl.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnl.so
%{_includedir}/netlink
%{_pkgconfigdir}/libnl-1.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libnl.a

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%doc doc/html/*
%endif
