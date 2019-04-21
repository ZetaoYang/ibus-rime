Name:           ibus-rime
Version:        1.4.0
Release:        0%{?dist}
Summary:        IBus rime
License:        GPL-3.0
Group:          System/I18n/Chinese
URL:            https://github.com/rime/ibus-rime
Source0:         https://github.com/rime/ibus-rime/archive/%{version}.tar.gz
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel >= 1.46
%endif
BuildRequires:  glog
BuildRequires:  glog-devel
BuildRequires:  gtest
BuildRequires:  gtest-devel
BuildRequires:  ibus-devel
BuildRequires:  libnotify-devel
BuildRequires:  cmake >= 2.8
BuildRequires:  gcc-c++
BuildRequires:  ibus-devel
BuildRequires:  leveldb-devel
BuildRequires:  librime-devel >= 1.0
BuildRequires:  marisa-devel
BuildRequires:  yaml-cpp >= 0.5
BuildRequires:  yaml-cpp-devel >= 0.5
BuildRequires:  opencc
BuildRequires:  opencc-devel
Requires:       rime

%description
Rime Input Method Engine - riming with your keystrokes.

%prep
%setup -q

%build
cd librime; make %{?_smp_mflags} && make install
cd ..
cd plum; make %{?_smp_mflags} && make install
cd ..
make clean && make %{?_smp_mflags}

%install
make install %{?_smp_mflags}

%files
%defattr(-,root,root)
%doc README
%{_ibus_componentdir}/rime.xml
%{_datadir}/ibus-rime/
%{_libexecdir}/ibus-rime/

%changelog
