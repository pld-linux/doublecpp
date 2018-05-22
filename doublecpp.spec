Summary:	Doublecpp - double dispatch in C++
Summary(pl.UTF-8):	Doublecpp - podwójna dyspozycja w C++
Name:		doublecpp
Version:	0.6.3
Release:	1
License:	GPL v2+
Group:		Development/Tools
Source0:	http://downloads.sourceforge.net/doublecpp/%{name}-%{version}.tar.gz
# Source0-md5:	0537ff74de82901f2e3bd92aaa677b3d
Patch0:		%{name}-includes.patch
URL:		http://doublecpp.sourceforge.net/
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Doublecpp is a preprocessor for C++ that handles a new linguistic
construct for defining branches of a multi-method. The "right" branch
of such a method will be selected dynamically at run-time according to
the actual type of the object on which the method is invoked and to
the actual type of the first argument: double dispatch.

%description -l pl.UTF-8
Doublecpp to preprocesor dla C++ obsługujący nową konstrukcję językową
do definiowania odgałęzień multi-metody. Właściwa gałąź takiej metody
jest wybierana dynamicznie w czasie działania zgodnie z typem obiektu,
z jakim została wywołana metoda oraz typem pierwszego argumentu:
podwójna dyspozycja.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/doublecpp

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO doc/doublecpp.html
%attr(755,root,root) %{_bindir}/doublecpp
