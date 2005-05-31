#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	String
%define		pnam	ShellQuote
Summary:	String::ShellQuote perl module
Summary(pl):	Modu³ perla String::ShellQuote
Name:		perl-String-ShellQuote
Version:	1.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b42822efe385f6604f55b0cea5ac0b76
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
String::ShellQuote - quotes strings so they can be passed through the
shell.

%description -l pl
String::ShellQuote - cytuje ³añcuchy tak, by mog³y byæ przekazane do
pow³oki.

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
%{perl_vendorlib}/String/ShellQuote.pm
%attr(755,root,root) %{_bindir}/shell-quote
%{_mandir}/man3/*
%{_mandir}/man1/*
