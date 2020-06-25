%define major 2
%define libname %mklibname wacom %{major}
%define devname %mklibname wacom -d

Summary:	A library to identify wacom tablets
Name:		libwacom
Version:	1.4
Release:	1
Group:		Development/X11
License:	MIT
Url:		http://sourceforge.net/projects/linuxwacom/
Source0:	https://github.com/linuxwacom/libwacom/releases/download/%{name}-%{version}/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gudev-1.0)

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

%build
%configure \
	--disable-static

%make_build

%install
%make_install
rm -rf %{buildroot}/%{_libdir}/udev/
pushd tools
mkdir -p %{buildroot}/%{_udevrulesdir}/
./generate-udev-rules > %{buildroot}/%{_udevrulesdir}/65-libwacom.rules
popd

%files
%{_datadir}/libwacom
%{_udevrulesdir}/65-libwacom.rules
%{_bindir}/libwacom-list-local-devices
%{_mandir}/man1/libwacom-list-local-devices.1.*
 
%files -n %{libname}
%{_libdir}/libwacom.so.%{major}*

%files -n %{devname}
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
