#
# Conditional build:
%bcond_with	tests	# perform "make check" (requires mounted /proc)
#
Summary:	GNU libsigsegv - handling page faults in user mode
Summary(pl.UTF-8):	GNU libsigsegv - obsługa błędów segmentacji na poziomie użytkownika
Name:		libsigsegv
Version:	2.6
Release:	1
License:	GPL v2+
Group:		Development/Libraries
Source0:	http://ftp.gnu.org/gnu/libsigsegv/%{name}-%{version}.tar.gz
# Source0-md5:	7e24993730649d13c6eabc28bd24de35
URL:		http://www.gnu.org/directory/GNU/GNUlibsigsegv.html
BuildRequires:	automake
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

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub autoconf
%configure
%{__make}

%{?with_tests:%{__make} check}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog NEWS AUTHORS
%{_includedir}/*.h
%{_libdir}/lib*.a
%{_libdir}/lib*.la
