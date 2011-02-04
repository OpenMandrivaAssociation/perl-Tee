%define upstream_name    Tee
%define upstream_version 0.14

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Pure Perl emulation of GNU tee
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module//%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(File::Basename)
BuildRequires: perl(File::Spec)
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(IPC::Run3)
BuildRequires: perl(Probe::Perl)
BuildRequires: perl(Test::More)
BuildRequires: perl(IO::CaptureOutput)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README LICENSE Changes META.yml
%{_mandir}/man3/*
%perl_vendorlib/*
/usr/bin/ptee
/usr/share/man/man1/ptee.1.xz

