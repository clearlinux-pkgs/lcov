#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : lcov
Version  : 1.14
Release  : 16
URL      : https://github.com/linux-test-project/lcov/releases/download/v1.14/lcov-1.14.tar.gz
Source0  : https://github.com/linux-test-project/lcov/releases/download/v1.14/lcov-1.14.tar.gz
Summary  : A graphical GCOV front-end
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: lcov-bin = %{version}-%{release}
Requires: lcov-data = %{version}-%{release}
Requires: lcov-license = %{version}-%{release}
Requires: lcov-man = %{version}-%{release}
Patch1: 0001-Fix-Makefile-to-be-compatible-with-simple-autotools-.patch
Patch2: 0002-geninfo-Add-intermediate-text-format-support.patch
Patch3: 0003-geninfo-Add-intermediate-JSON-format-support.patch

%description
LCOV is a graphical front-end for GCC's coverage testing tool gcov. It collects
gcov data for multiple source files and creates HTML pages containing the
source code annotated with coverage information. It also adds overview pages
for easy navigation within the file structure.

%package bin
Summary: bin components for the lcov package.
Group: Binaries
Requires: lcov-data = %{version}-%{release}
Requires: lcov-license = %{version}-%{release}

%description bin
bin components for the lcov package.


%package data
Summary: data components for the lcov package.
Group: Data

%description data
data components for the lcov package.


%package license
Summary: license components for the lcov package.
Group: Default

%description license
license components for the lcov package.


%package man
Summary: man components for the lcov package.
Group: Default

%description man
man components for the lcov package.


%prep
%setup -q -n lcov-1.14
cd %{_builddir}/lcov-1.14
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1576268529
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1576268529
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/lcov
cp %{_builddir}/lcov-1.14/COPYING %{buildroot}/usr/share/package-licenses/lcov/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gendesc
/usr/bin/genhtml
/usr/bin/geninfo
/usr/bin/genpng
/usr/bin/lcov

%files data
%defattr(-,root,root,-)
/usr/share/defaults/lcov/lcovrc

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/lcov/06877624ea5c77efe3b7e39b0f909eda6e25a4ec

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/gendesc.1
/usr/share/man/man1/genhtml.1
/usr/share/man/man1/geninfo.1
/usr/share/man/man1/genpng.1
/usr/share/man/man1/lcov.1
/usr/share/man/man5/lcovrc.5
