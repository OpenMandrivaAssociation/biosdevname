Name:		biosdevname
Version:	0.7.2
Release:	1
Summary:	Udev helper for naming devices per BIOS names
Group:		System/Base 
License:	GPLv2
URL:		http://linux.dell.com/files/%{name}
# SMBIOS only exists on these arches.  It's also likely that other
# arches don't expect the PCI bus to be sorted breadth-first, or of
# so, there haven't been any comments about that on LKML.
Source0:	http://linux.dell.com/files/%{name}/permalink/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(libpci)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	udev
Requires:	udev

%description
biosdevname in its simplest form takes a kernel device name as an
argument, and returns the BIOS-given name it "should" be.  This is necessary
on systems where the BIOS name for a given device (e.g. the label on
the chassis is "Gb1") doesn't map directly and obviously to the kernel
name (e.g. eth0).

%prep
%autosetup -p1

%build
%configure 
%make_build

%install
%make_install install-data

%files
%doc COPYING README
%{_bindir}/biosdevname
/lib/udev/rules.d/71-biosdevname.rules
%{_mandir}/man1/%{name}.1*


%changelog
* Mon Jul 30 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.4.1-1
+ Revision: 811466
- version update  0.4.1

* Sat May 19 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.4.0-1
+ Revision: 799611
- version update 0.4.0

* Wed Nov 09 2011 Alexander Khrukin <akhrukin@mandriva.org> 0.3.11-1
+ Revision: 729511
- imported package biosdevname

