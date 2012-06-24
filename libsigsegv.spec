#
# Conditional build:
%bcond_with	tests	# perform "make check" (requires mounted /proc)
#
Summary:	GNU libsigsegv - handling page faults in user mode
Summary(pl):	GNU libsigsegv - obs�uga b��d�w segmentacji na poziomie u�ytkownika
Name:		libsigsegv
Version:	2.1
Release:	2
License:	GPL
Group:		Development/Libraries
Source0:	ftp://ftp.gnu.org/gnu/libsigsegv/%{name}-%{version}.tar.gz
# Source0-md5:	6d75ca3fede5fbfd72a78bc918d9e174
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

%description -l pl
Biblioteka obs�uguje b��dy obs�ugi stron na poziomie u�ytkownika. B��d
strony pojawia si� gdy program pr�buje dosta� si� do aktualnie
niedost�pnego obszaru pami�ci. Zbieranie i obs�uga b��d�w stron jest
u�yteczn� technik� do implementacji:
- stronicowalnej pami�ci wirtualnej
- mapowalnej pami�ci baz danych
- generowania od�miecaczy
- b��d�w przepe�nienia stosu
- rozproszonej pami�ci wsp�dzielonej
- ...

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub .
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
