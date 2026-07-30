%define upstream_name    X11-Protocol
%define upstream_version 0.56
Name:		perl-%{upstream_name}
Version:	0.56
Release:	2

Summary:	Perl module for the X Window System Protocol
License:	Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/X11-Protocol
Source0:	https://cpan.metacpan.org/authors/id/S/SM/SMCCAM/X11-Protocol-0.56.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
This is a module for the X Window System Protocol.

%prep
%setup -q -n X11-Protocol-0.56

%build
perl Makefile.PL INSTALLDIRS="vendor" 
%make

%check
# soft: do not fail package on test failures
set +e
# test needs a running X server
:  # soft check
%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/X11


