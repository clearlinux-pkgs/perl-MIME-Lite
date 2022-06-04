#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-MIME-Lite
Version  : 3.033
Release  : 10
URL      : https://cpan.metacpan.org/authors/id/R/RJ/RJBS/MIME-Lite-3.033.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RJ/RJBS/MIME-Lite-3.033.tar.gz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-2.0
Requires: perl-MIME-Lite-license = %{version}-%{release}
Requires: perl-MIME-Lite-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Email::Date::Format)
BuildRequires : perl(MIME::Types)
BuildRequires : perl(Mail::Address)

%description
NAME
MIME::Lite - low-calorie MIME generator
WAIT!
MIME::Lite is not recommended by its current maintainer. There are a
number of alternatives, like Email::MIME or MIME::Entity and
Email::Sender, which you should probably use instead. MIME::Lite
continues to accrue weird bug reports, and it is not receiving a large
amount of refactoring due to the availability of better alternatives.
Please consider using something else.

%package dev
Summary: dev components for the perl-MIME-Lite package.
Group: Development
Provides: perl-MIME-Lite-devel = %{version}-%{release}
Requires: perl-MIME-Lite = %{version}-%{release}

%description dev
dev components for the perl-MIME-Lite package.


%package license
Summary: license components for the perl-MIME-Lite package.
Group: Default

%description license
license components for the perl-MIME-Lite package.


%package perl
Summary: perl components for the perl-MIME-Lite package.
Group: Default
Requires: perl-MIME-Lite = %{version}-%{release}

%description perl
perl components for the perl-MIME-Lite package.


%prep
%setup -q -n MIME-Lite-3.033
cd %{_builddir}/MIME-Lite-3.033

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-MIME-Lite
cp %{_builddir}/MIME-Lite-3.033/COPYING %{buildroot}/usr/share/package-licenses/perl-MIME-Lite/aa57d45530d46f5b52279b5d703112dda67cbdc1
cp %{_builddir}/MIME-Lite-3.033/LICENSE %{buildroot}/usr/share/package-licenses/perl-MIME-Lite/f11692fc652e231edd2a23a60c72d9be8a840e0c
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/MIME::Lite.3
/usr/share/man/man3/MIME::changes.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-MIME-Lite/aa57d45530d46f5b52279b5d703112dda67cbdc1
/usr/share/package-licenses/perl-MIME-Lite/f11692fc652e231edd2a23a60c72d9be8a840e0c

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
