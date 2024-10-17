%define upstream_name    X11-Protocol
%define upstream_version 0.56

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Perl module for the X Window System Protocol
License:	Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/X11/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This is a module for the X Window System Protocol.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS="vendor" 
%make

%check
# test needs a running X server

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/X11


%changelog
* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.560.0-1mdv2010.0
+ Revision: 401879
- rebuild using %%perl_convert_version

* Fri Aug 01 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.56-6mdv2009.0
+ Revision: 258794
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.56-5mdv2009.0
+ Revision: 246718
- rebuild

* Wed Dec 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.56-3mdv2008.1
+ Revision: 138071
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Dec 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.56-2mdv2008.1
+ Revision: 133732
- rebuild

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Nov 15 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.56-1mdv2007.0
+ Revision: 84297
- new version
- Import perl-X11-Protocol

* Wed Aug 30 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.55-2mdv2007.0
- Rebuild

* Wed Jan 25 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.55-1mdk
- new version
- more spec cleaning
- fix directory ownership
- enable tests

* Mon Dec 19 2005 Erwan Velu <erwan@seanodes.com> 0.54-2mdk
- Spec cleaning (thx guillaume)

* Mon Dec 19 2005 Erwan Velu <erwan@seanodes.com> 0.54-1mdk
- Initial Release

