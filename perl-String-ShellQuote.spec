#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	String
%define		pnam	ShellQuote
Summary:	String::ShellQuote - quote strings for passing through the shell
Summary(pl.UTF-8):	String::ShellQuote - cytowanie łańcuchów do przekazywania przez powłokę
Name:		perl-String-ShellQuote
Version:	1.04
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/String/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	da6329dc482b21adf5697cfbd2ac5412
URL:		http://search.cpan.org/dist/String-ShellQuote/
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
String::ShellQuote module contains some functions which are useful for
quoting strings which are going to pass through the shell or a
shell-like object.

%description -l pl.UTF-8
Moduł String::ShellQuote zawiera funkcje przydatne przy cytowaniu
łańcuchów znaków tak, by mogły być przekazane do powłoki lub innego
obiektu zachowującego się jak powłoka.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/shell-quote
%{perl_vendorlib}/String/ShellQuote.pm
%{_mandir}/man1/shell-quote.1p*
%{_mandir}/man3/String::ShellQuote.3pm*
