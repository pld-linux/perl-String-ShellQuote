%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary:	String-ShellQuote perl module
Summary(pl):	Modu³ perla String-ShellQuote
Name:		perl-String-ShellQuote
Version:	1.00
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/String/String-ShellQuote-%{version}.tar.gz
BuildRequires:	perl >= 5.005_03-10
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
String-ShellQuote - quotes strings so they can be passed through the shell. 

%description -l pl
String-ShellQuote - cytuje ³añcuchy tak, by mog³y byæ przekazane do pow³oki.

%prep
%setup -q -n String-ShellQuote-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/String/ShellQuote
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%{perl_sitelib}/String/ShellQuote.pm
%{perl_sitearch}/auto/String/ShellQuote

%{_mandir}/man3/*
