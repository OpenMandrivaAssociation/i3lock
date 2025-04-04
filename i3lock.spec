%define debug_package %{nil}
Name:		i3lock
Version:	2.15
Release:	1
Source0:	https://github.com/i3/i3lock/archive/refs/tags/%{version}.tar.gz
Summary:	improved screen locker
URL:		https://github.com/i3/i3lock
License:	BSD-3-Clause
Group:		Windows Manager/I3

BuildSystem:	meson

BuildRequires:	pkgconfig(xcb)
BuildRequires:	pkgconfig(xcb-image)
BuildRequires:	pkgconfig(xcb-util)
BuildRequires:	pkgconfig(xcb-xrm)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(xkbcommon-x11)
BuildRequires:	pkgconfig(cairo)
BuildRequires:  libev-devel
BuildRequires:  pam-devel

%description
i3lock is a simple screen locker like slock.

%prep
%autosetup -p1
%meson -Dc_args=-I/usr/include/libev

%files
%doc CHANGELOG README*
%license LICENSE
%{_sysconfdir}/pam.d/%{name}
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.zst
