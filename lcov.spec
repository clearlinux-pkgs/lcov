#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : lcov
Version  : 1.13
Release  : 10
URL      : https://sourceforge.net/projects/ltp/files/Coverage%20Analysis/LCOV-1.13/lcov-1.13.tar.gz
Source0  : https://sourceforge.net/projects/ltp/files/Coverage%20Analysis/LCOV-1.13/lcov-1.13.tar.gz
Summary  : A graphical GCOV front-end
Group    : Development/Tools
License  : GPL-2.0
Requires: lcov-bin
Requires: lcov-data
Requires: lcov-doc
Patch1: 0001-Fix-Makefile-to-be-compatible-with-simple-autotools-.patch

%description
LCOV is a graphical front-end for GCC's coverage testing tool gcov. It collects
gcov data for multiple source files and creates HTML pages containing the
source code annotated with coverage information. It also adds overview pages
for easy navigation within the file structure.

%package bin
Summary: bin components for the lcov package.
Group: Binaries
Requires: lcov-data

%description bin
bin components for the lcov package.


%package data
Summary: data components for the lcov package.
Group: Data

%description data
data components for the lcov package.


%package doc
Summary: doc components for the lcov package.
Group: Documentation

%description doc
doc components for the lcov package.


%prep
%setup -q -n lcov-1.13
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1494864168
make V=1  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1494864168
rm -rf %{buildroot}
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

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man5/*
