%define librsl %mklibname rsl 1
%define librsl_devel %mklibname -d rsl

Name:		rsl
Version:	1.42
Release:	1
Group:		System/Libraries
License:	LGPLv2+
URL:		http://trmm-fc.gsfc.nasa.gov/trmm_gv/software/rsl/
Summary:	TRMM Radar Software Library
Source0:	%{name}-v%{version}.tar.gz
Patch0:		rsl-1.42-mdv-install.patch
BuildRequires:	zlib-devel
BuildRequires:	flex

%description
This library is an object oriented programming environment for writing software
applicable to all RADAR data related to the TRMM GV effort. This library reads
the WSR88D, Lassen, Sigmet, McGill, UF, HDF, RAPIC, RADTEC and native RSL file
formats. Additional functions are provided to manipulate the RSL objects.
Nearly all of the functions return objects. When they don't, they usually
perform actions like output, making images, etc. The most general object in RSL
is Radar. The structure Radar is the method used to define the ideal
or universal radar representation in RAM while keeping the natural resolution
of the data unchanged. More simply, Radar represents the super set of all radar
file formats. The Radar structure is hierarchically defined such that it is
composed of Volumes, each containing one field type. Volumes are composed
of Sweeps. Sweeps are composed of Rays and Rays contains a vector of the field
type. Some field types are Reflectivity(DZ), Velocity(VR), Spectrum Width(SW),
etc. There are approximately 20 field types.

%files
%{_bindir}/*
%doc CHANGES Copyright README

#------------------------------------------------------------------------------

%package -n %librsl

Summary:	TRMM Radar Software Library
Requires:	%{name}-data == %{version}

%description -n %librsl

This library is an object oriented programming environment for writing software
applicable to all RADAR data related to the TRMM GV effort. This library reads
the WSR88D, Lassen, Sigmet, McGill, UF, HDF, RAPIC, RADTEC and native RSL file
formats. Additional functions are provided to manipulate the RSL objects.
Nearly all of the functions return objects. When they don't, they usually
perform actions like output, making images, etc. The most general object in RSL
is Radar. The structure Radar is the method used to define the ideal
or universal radar representation in RAM while keeping the natural resolution
of the data unchanged. More simply, Radar represents the super set of all radar
file formats. The Radar structure is hierarchically defined such that it is
composed of Volumes, each containing one field type. Volumes are composed
of Sweeps. Sweeps are composed of Rays and Rays contains a vector of the field
type. Some field types are Reflectivity(DZ), Velocity(VR), Spectrum Width(SW),
etc. There are approximately 20 field types.

%files -n %librsl
%{_libdir}/*.so.*

#------------------------------------------------------------------------------

%package -n %librsl_devel

Summary:	TRMM Radar Software Library development files
Group:		Development/C++
Requires:	%{librsl} == %{EVRD}
Provides:	%{name}-devel == %{EVRD}

%description -n %librsl_devel

This library is an object oriented programming environment for writing software
applicable to all RADAR data related to the TRMM GV effort. This library reads
the WSR88D, Lassen, Sigmet, McGill, UF, HDF, RAPIC, RADTEC and native RSL file
formats. Additional functions are provided to manipulate the RSL objects.
Nearly all of the functions return objects. When they don't, they usually
perform actions like output, making images, etc. The most general object in RSL
is Radar. The structure Radar is the method used to define the ideal
or universal radar representation in RAM while keeping the natural resolution
of the data unchanged. More simply, Radar represents the super set of all radar
file formats. The Radar structure is hierarchically defined such that it is
composed of Volumes, each containing one field type. Volumes are composed
of Sweeps. Sweeps are composed of Rays and Rays contains a vector of the field
type. Some field types are Reflectivity(DZ), Velocity(VR), Spectrum Width(SW),
etc. There are approximately 20 field types.

This package contains files needed only for development.

%files -n %librsl_devel
%{_libdir}/*.so
%{_includedir}/*
%doc CHANGES Copyright README

#------------------------------------------------------------------------------

%package data

Summary:	TRMM Radar Software Library data files

%description data

This library is an object oriented programming environment for writing software
applicable to all RADAR data related to the TRMM GV effort. This library reads
the WSR88D, Lassen, Sigmet, McGill, UF, HDF, RAPIC, RADTEC and native RSL file
formats. Additional functions are provided to manipulate the RSL objects.
Nearly all of the functions return objects. When they don't, they usually
perform actions like output, making images, etc. The most general object in RSL
is Radar. The structure Radar is the method used to define the ideal
or universal radar representation in RAM while keeping the natural resolution
of the data unchanged. More simply, Radar represents the super set of all radar
file formats. The Radar structure is hierarchically defined such that it is
composed of Volumes, each containing one field type. Volumes are composed
of Sweeps. Sweeps are composed of Rays and Rays contains a vector of the field
type. Some field types are Reflectivity(DZ), Velocity(VR), Spectrum Width(SW),
etc. There are approximately 20 field types.

%files data
%{_datadir}/rsl/

#------------------------------------------------------------------------------

%package doc

Summary:	TRMM Radar Software Library documentation
Requires:	%{name} == %{version}

%description doc
This library is an object oriented programming environment for writing software
applicable to all RADAR data related to the TRMM GV effort. This library reads
the WSR88D, Lassen, Sigmet, McGill, UF, HDF, RAPIC, RADTEC and native RSL file
formats. Additional functions are provided to manipulate the RSL objects.
Nearly all of the functions return objects. When they don't, they usually
perform actions like output, making images, etc. The most general object in RSL
is Radar. The structure Radar is the method used to define the ideal
or universal radar representation in RAM while keeping the natural resolution
of the data unchanged. More simply, Radar represents the super set of all radar
file formats. The Radar structure is hierarchically defined such that it is
composed of Volumes, each containing one field type. Volumes are composed
of Sweeps. Sweeps are composed of Rays and Rays contains a vector of the field
type. Some field types are Reflectivity(DZ), Velocity(VR), Spectrum Width(SW),
etc. There are approximately 20 field types.

This package contains RSL documentation.

%files doc
%doc doc/*.html doc/*.gif doc/*.jpg doc/*.fig

#------------------------------------------------------------------------------

%prep
%setup -q -n %{name}-v%{version}
%patch0 -p1

%build
autoreconf
%configure
%make

%install
%makeinstall_std
rm -f %{buildroot}%{_libdir}/*.la %{buildroot}%{_libdir}/*.a
rm -rf %{buildroot}%{_docdir}
