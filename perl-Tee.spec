%define upstream_name    Tee
%define upstream_version 0.14

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Pure Perl emulation of GNU tee
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module//%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Getopt::Long)
BuildRequires:	perl(IPC::Run3)
BuildRequires:	perl(Probe::Perl)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(IO::CaptureOutput)
BuildArch:	noarch

%description
The 'Tee' distribution provides the the ptee manpage program, a pure Perl
emulation of the standard GNU tool 'tee'. It is designed to be a
platform-independent replacement for operating systems without a native
'tee' program. As with 'tee', it passes input received on STDIN through to
STDOUT while also writing a copy of the input to one or more files. By
default, files will be overwritten.

Unlike 'tee', 'ptee' does not support ignoring interrupts, as signal
handling is not sufficiently portable.

The 'Tee' module provides a convenience function that may be used in place
of 'system()' to redirect commands through 'ptee'.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README LICENSE Changes META.yml
%{perl_vendorlib}/*
%{_bindir}/ptee
%{_mandir}/man1/ptee.1.xz
%{_mandir}/man3/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.140.0-2mdv2011.0
+ Revision: 657838
- rebuild for updated spec-helper

* Fri Feb 04 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.140.0-1
+ Revision: 635790
- update to new version 0.14

* Fri Dec 24 2010 Shlomi Fish <shlomif@mandriva.org> 0.130.0-1mdv2011.0
+ Revision: 624641
- import perl-Tee

