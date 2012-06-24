Summary:	Netlink library
Summary(pl):	Biblioteka do obs�ugi gniazd netlink
Name:		libnl
Version:	1.0
%define pre pre6
Release:	0.%{pre}.1
License:	LGPL v2.1
Group:		Libraries
Source0:	http://people.suug.ch/~tgr/libnl/files/%{name}-%{version}-%{pre}.tar.gz
# Source0-md5:	0f57cb7085dc27e054691bff858613c9
Patch0:		%{name}-llh.patch
URL:		http://people.suug.ch/~tgr/libnl/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libnl is a library for applications dealing with netlink socket. It
provides an easy to use interface for raw netlink message but also
netlink family specific APIs.

%description -l pl
libnl jest bibliotek� dla aplikacji rozmawiaj�cych z gniazdem
netlink. Udost�pnia �atwy w u�yciu interfejs do korzystania z
surowych wiadomo�ci netlink, a tak�e API specyficzne dla rodziny
gniazd netlink.

%package devel
Summary:	Header files for libnl library
Summary(pl):	Pliki nag��wkowe biblioteki libnl
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libnl library.

%description devel -l pl
Pliki nag��wkowe biblioteki libnl.

%package static
Summary:	Static libnl library
Summary(pl):	Statyczna biblioteka libnl
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libnl library.

%description static -l pl
Statyczna biblioteka libnl.

%prep
%setup -q -n %{name}-%{version}-%{pre}
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}

%configure \
	--enable-verbose-errors

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_libdir}/libnl.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnl.so
%{_includedir}/netlink
%{_pkgconfigdir}/libnl-1.pc
