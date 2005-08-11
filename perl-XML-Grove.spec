#
# Conditional build:
%bcond_with	tests	# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	XML
%define		pnam	Grove
Summary:	XML::Grove Perl module
Summary(cs):	Modul XML::Grove pro Perl
Summary(da):	Perlmodul XML::Grove
Summary(de):	XML::Grove Perl Modul
Summary(es):	Módulo de Perl XML::Grove
Summary(fr):	Module Perl XML::Grove
Summary(it):	Modulo di Perl XML::Grove
Summary(ja):	XML::Grove Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	XML::Grove ÆÞ ¸ðÁÙ
Summary(nb):	Perlmodul XML::Grove
Summary(pl):	Modu³ Perla XML::Grove
Summary(pt):	Módulo de Perl XML::Grove
Summary(pt_BR):	Módulo Perl XML::Grove
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl XML::Grove
Summary(sv):	XML::Grove Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl XML::Grove
Summary(zh_CN):	XML::Grove Perl Ä£¿é
Name:		perl-XML-Grove
Version:	0.46alpha
Release:	10
# same as perl (however COPYING says Artistic)
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	48bee70ae412bd6cf8ef302b6c68e24e
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-XML-Parser
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML::Grove perl module.

%description -l cs
Modul XML::Grove pro Perl.

%description -l da
Perlmodul XML::Grove.

%description -l de
XML::Grove Perl Modul.

%description -l es
Módulo de Perl XML::Grove.

%description -l fr
Module Perl XML::Grove.

%description -l it
Modulo di Perl XML::Grove.

%description -l ja
XML::Grove Perl ¥â¥¸¥å¡¼¥ë

%description -l ko
XML::Grove ÆÞ ¸ðÁÙ.

%description -l nb
Perlmodul XML::Grove.

%description -l pl
Modu³ perla XML::Grove.

%description -l pt
Módulo de Perl XML::Grove.

%description -l pt_BR
Módulo Perl XML::Grove.

%description -l ru
íÏÄÕÌØ ÄÌÑ Perl XML::Grove.

%description -l sv
XML::Grove Perlmodul.

%description -l uk
íÏÄÕÌØ ÄÌÑ Perl XML::Grove.

%description -l zh_CN
XML::Grove Perl Ä£¿é

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/XML/Grove.pm
%{perl_vendorlib}/XML/Grove
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
