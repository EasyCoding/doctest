%global debug_package %{nil}

Name: doctest
Version: 2.3.7
Release: 1%{?dist}

Summary: Feature-rich header-only C++ testing framework
License: MIT
URL: https://github.com/onqtam/%{name}
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: ninja-build
BuildRequires: gcc-c++
BuildRequires: cmake

%description
Feature-rich C++11/14/17/20 header-only testing framework for unit tests
and TDD.

%package devel
Summary: Development files for %{name}
Provides: %{name}-static%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: libstdc++-devel%{?_isa}

%description devel
%{summary}.

%prep
%autosetup -p1
mkdir -p %{_target_platform}

%build
pushd %{_target_platform}
    %cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DDOCTEST_WITH_MAIN_IN_STATIC_LIB:BOOL=OFF \
    -DDOCTEST_WITH_TESTS:BOOL=ON \
    ..
popd
%ninja_build -C %{_target_platform}

%check
pushd %{_target_platform}
    ctest --output-on-failure
popd

%install
%ninja_install -C %{_target_platform}

%files devel
%doc README.md CHANGELOG.md CONTRIBUTING.md
%license LICENSE.txt
%{_includedir}/%{name}/
%{_libdir}/cmake/%{name}/

%changelog
* Sun May 03 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2.3.7-1
- Initial SPEC release.
