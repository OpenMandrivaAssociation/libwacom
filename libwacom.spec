%define major 2
%define libname %mklibname wacom %{major}
%define devname %mklibname wacom -d

Summary:	A library to identify wacom tablets
Name:		libwacom
Version:	0.29
Release:	3
Group:		Development/X11
License:	MIT
Url:		http://sourceforge.net/projects/linuxwacom/
Source0:	http://downloads.sourceforge.net/project/linuxwacom/%{name}/%{name}-%{version}.tar.bz2
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
%setup -q

%build
%configure \
	--disable-static
%make

%install
%makeinstall_std

%files
%{_datadir}/libwacom
%{_bindir}/libwacom-list-local-devices

%files -n %{libname}
%{_libdir}/libwacom.so.%{major}*

%files -n %{devname}
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc

