%include	/usr/lib/rpm/macros.perl
%define	pdir	String
%define	pnam	ShellQuote
Summary:	String::ShellQuote perl module
Summary(pl):	Modu³ perla String::ShellQuote
Name:		perl-String-ShellQuote
Version:	1.00
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
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
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/String/ShellQuote.pm
%{_mandir}/man3/*
