#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : lcov
Version  : 1.11
Release  : 6
URL      : http://downloads.sourceforge.net/ltp/lcov-1.11.tar.gz
Source0  : http://downloads.sourceforge.net/ltp/lcov-1.11.tar.gz
Summary  : A graphical GCOV front-end
Group    : Development/Tools
License  : GPL-2.0
Requires: lcov-bin
Requires: lcov-data
Requires: lcov-doc
Patch1: patch.patch

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
%setup -q -n lcov-1.11
%patch1 -p1

%build
make V=1  %{?_smp_mflags}

%install
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
