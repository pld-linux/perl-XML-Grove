#
# Conditional build:
%bcond_with	tests	# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	XML
%define		pnam	Grove
Summary:	XML::Grove Perl module
Summary(cs.UTF-8):	Modul XML::Grove pro Perl
Summary(da.UTF-8):	Perlmodul XML::Grove
Summary(de.UTF-8):	XML::Grove Perl Modul
Summary(es.UTF-8):	Módulo de Perl XML::Grove
Summary(fr.UTF-8):	Module Perl XML::Grove
Summary(it.UTF-8):	Modulo di Perl XML::Grove
Summary(ja.UTF-8):	XML::Grove Perl モジュール
Summary(ko.UTF-8):	XML::Grove 펄 모줄
Summary(nb.UTF-8):	Perlmodul XML::Grove
Summary(pl.UTF-8):	Moduł Perla XML::Grove
Summary(pt.UTF-8):	Módulo de Perl XML::Grove
Summary(pt_BR.UTF-8):	Módulo Perl XML::Grove
Summary(ru.UTF-8):	Модуль для Perl XML::Grove
Summary(sv.UTF-8):	XML::Grove Perlmodul
Summary(uk.UTF-8):	Модуль для Perl XML::Grove
Summary(zh_CN.UTF-8):	XML::Grove Perl 模块
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

%description -l cs.UTF-8
Modul XML::Grove pro Perl.

%description -l da.UTF-8
Perlmodul XML::Grove.

%description -l de.UTF-8
XML::Grove Perl Modul.

%description -l es.UTF-8
Módulo de Perl XML::Grove.

%description -l fr.UTF-8
Module Perl XML::Grove.

%description -l it.UTF-8
Modulo di Perl XML::Grove.

%description -l ja.UTF-8
XML::Grove Perl モジュール

%description -l ko.UTF-8
XML::Grove 펄 모줄.

%description -l nb.UTF-8
Perlmodul XML::Grove.

%description -l pl.UTF-8
Moduł perla XML::Grove.

%description -l pt.UTF-8
Módulo de Perl XML::Grove.

%description -l pt_BR.UTF-8
Módulo Perl XML::Grove.

%description -l ru.UTF-8
Модуль для Perl XML::Grove.

%description -l sv.UTF-8
XML::Grove Perlmodul.

%description -l uk.UTF-8
Модуль для Perl XML::Grove.

%description -l zh_CN.UTF-8
XML::Grove Perl 模块

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
