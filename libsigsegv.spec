#
# Conditional build:
%bcond_with	tests	# perform "make check" (requires mounted /proc)
#
Summary:	GNU libsigsegv - handling page faults in user mode
Summary(pl.UTF-8):	GNU libsigsegv - obsługa błędów segmentacji na poziomie użytkownika
Name:		libsigsegv
Version:	2.14
Release:	1
License:	GPL v2+
Group:		Development/Libraries
Source0:	https://ftp.gnu.org/gnu/libsigsegv/%{name}-%{version}.tar.gz
# Source0-md5:	63a2b35f11b2fbccc3d82f9e6c6afd58
URL:		https://www.gnu.org/software/libsigsegv/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a library for handling page faults in user mode. A page fault
occurs when a program tries to access to a region of memory that is
currently not available. Catching and handling a page fault is a
useful technique for implementing:
- pageable virtual memory,
- memory-mapped access to persistent databases,
- generational garbage collectors,
- stack overflow handlers,
- distributed shared memory,
- ...

%description -l pl.UTF-8
Biblioteka obsługuje błędy obsługi stron na poziomie użytkownika. Błąd
strony pojawia się gdy program próbuje dostać się do aktualnie
niedostępnego obszaru pamięci. Zbieranie i obsługa błędów stron jest
użyteczną techniką do implementacji:
- stronicowalnej pamięci wirtualnej
- mapowalnej pamięci baz danych
- generowania odśmiecaczy
- błędów przepełnienia stosu
- rozproszonej pamięci współdzielonej
- ...

%package devel
Summary:	Header files for libsigsegv library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libsigsegv
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libsigsegv library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libsigsegv.

%package static
Summary:	Static libsigsegv library
Summary(pl.UTF-8):	Statyczna biblioteka libsigsegv
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libsigsegv library.

%description static -l pl.UTF-8
Statyczna biblioteka libsigsegv.

%prep
%setup -q

%build
CXXFLAGS="%{rpmcxxflags} -fPIC"
CFLAGS="%{rpmcflags} -fPIC"
%configure \
	--enable-shared
%{__make}

%{?with_tests:%{__make} check}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libsigsegv.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libsigsegv.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsigsegv.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsigsegv.so
%{_includedir}/sigsegv.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libsigsegv.a
