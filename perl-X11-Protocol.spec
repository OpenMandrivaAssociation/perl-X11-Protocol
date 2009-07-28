%define upstream_name    X11-Protocol
%define upstream_version 0.56

Name:           perl-%{upstream_name}
Version:        %perl_convert_version %{upstream_version}
Release:        %mkrel 1

Summary:        Perl module for the X Window System Protocol
License:        Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{upstream_name}
Source0:        http://www.cpan.org/modules/by-module/X11/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This is a module for the X Window System Protocol.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" 
%make

%check
# test needs a running X server

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/X11
