%define major		2
%define libname		%mklibname wacom %{major}
%define develname	%mklibname wacom -d

%define url_ver	%(echo %{version}|cut -d. -f1,2)

Name:		libwacom
Summary:	A library to identify wacom tablets
Version:	0.7.1
Release:	1
Group:		Development/X11
License:	MIT
URL:		http://sourceforge.net/projects/linuxwacom/
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

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
Development files for %{name}.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static
%make

%install
%makeinstall_std
rm -f %{buildroot}%{_libdir}/*.la

%files
%{_datadir}/libwacom
%{_bindir}/libwacom-list-local-devices

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc

