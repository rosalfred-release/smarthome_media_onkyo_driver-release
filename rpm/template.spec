Name:           ros-indigo-smarthome-media-onkyo-driver
Version:        0.1.64
Release:        0%{?dist}
Summary:        ROS smarthome_media_onkyo_driver package

Group:          Development/Libraries
License:        GPLv3
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-smarthome-common-driver
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-rosjava-build-tools
BuildRequires:  ros-indigo-smarthome-common-driver

%description
This package is for interfacing Onkyo sound system (by JEISP API) to ROS. This
package is part of Alfred Assistant stack.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Thu Jun 09 2016 Mickael Gaillard <mick.gaillard@gmail.com> - 0.1.64-0
- Autogenerated by Bloom

* Sun Jun 05 2016 Mickael Gaillard <mick.gaillard@gmail.com> - 0.1.63-0
- Autogenerated by Bloom

