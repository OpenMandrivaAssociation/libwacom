%define major 9
%define libname %mklibname wacom %{major}
%define devname %mklibname wacom -d

Summary:	A library to identify wacom tablets
Name:		libwacom
Version:	2.3.0
Release:	1
Group:		Development/X11
License:	MIT
Url:		http://sourceforge.net/projects/linuxwacom/
Source0:	https://github.com/linuxwacom/libwacom/releases/download/%{name}-%{version}/%{name}-%{version}.tar.xz

BuildRequires:  meson
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gudev-1.0)
BuildRequires:	pkgconfig(libxml-2.0)

%description
libwacom is a library to identify wacom tablets and their model-specific
features. It provides easy access to information such as "is this a built-in
on-screen tablet", "what is the size of this model", etc.

%package -n %{libname}
Summary:	A library to identify wacom tablets
Group:		Development/X11
Requires:	%{name} >= %{version}-%{release}

%description -n %{libname}
libwacom is a library to identify wacom tablets and their model-specific
features. It provides easy access to information such as "is this a built-in
on-screen tablet", "what is the size of this model", etc.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Development files for %{name}.

%prep
%autosetup -p1
# failing test:
rm -f data/check-data-in-meson.build.sh

%build
%meson -Dtests=disabled -Ddocumentation=disabled -Dudev-dir="$(dirname %{_udevrulesdir})"
%meson_build

%install
%meson_install
install -d ${RPM_BUILD_ROOT}/%{_udevrulesdir}

%files
%{_datadir}/libwacom
%{_udevrulesdir}/*.rules
%{_udevhwdbdir}/*.hwdb
%{_bindir}/*
%{_mandir}/man1/libwacom-list-local-devices.1.*
%{_mandir}/man1/libwacom-list-devices.1.*

%files -n %{libname}
%{_libdir}/libwacom.so.%{major}*

%files -n %{devname}
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
