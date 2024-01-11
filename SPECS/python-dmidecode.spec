Name: python-dmidecode
Summary: Python module to access DMI data
Version: 3.12.3
Release: 2%{?dist}
License: GPLv2
Group: System Environment/Libraries
URL: https://github.com/nima/python-dmidecode
Source0: https://github.com/nima/python-dmidecode/archive/refs/tags/%{name}-%{version}.tar.gz
Patch0: 0001-Fix-dmi_cache_size_2-will-add-unit-twice.patch
Patch1: 0002-Fix-wrong-DMI-structures-count.patch

BuildRequires: make
BuildRequires: gcc
BuildRequires: libxml2-devel

BuildRequires: python3-devel
BuildRequires: python3-libxml2

%global _description\
python-dmidecode is a python extension module that uses the\
code-base of the 'dmidecode' utility, and presents the data\
as python data structures or as XML data using libxml2.\
\


%description %_description

%package -n python3-dmidecode
Summary: Python 3 module to access DMI data
Requires: libxml2-python3
ExclusiveArch:  x86_64

%description -n python3-dmidecode
python3-dmidecode is a Python 3 extension module that uses the
code-base of the 'dmidecode' utility, and presents the data
as Python 3 data structures or as XML data using libxml2.



%prep
%autosetup -p1

%build
# -std=gnu89 is there to avoid `undefined symbol: dmixml_GetContent`
export PYTHON_BIN=%{__python3}
export PYTHON_VERSION=%{python3_version}
export CFLAGS="%{build_cflags} -std=gnu89"
export CC=gcc
%make_build

%install
%{__python3} src/setup.py install --root %{buildroot} --prefix=%{_prefix}


%check
export PYTHONPATH=%{buildroot}%{python3_sitearch}
export PYTHON_BIN=%{__python3}
make -C unit-tests


%files -n python3-dmidecode
%license doc/LICENSE doc/AUTHORS doc/AUTHORS.upstream
%doc README doc/README.upstream
%{python3_sitearch}/dmidecodemod.cpython-%{python3_version_nodots}m-*.so
%{python3_sitearch}/__pycache__/dmidecode.cpython-%{python3_version_nodots}*.py[co]
%{python3_sitearch}/dmidecode.py
%{python3_sitearch}/*.egg-info
%{_datadir}/python-dmidecode/

%changelog
* Fri Feb 17 2023 Lichen Liu <lichliu@redhat.com> - 3.12.3-2
- Resolves: rhbz#2103911

* Tue Feb 07 2023 Lichen Liu <lichliu@redhat.com> - 3.12.3-1
- Resolves: rhbz#2070727
- Resolves: rhbz#2103911

* Wed May 08 2019 Lianbo Jiang <lijiang@redhat.com> - 3.12.2-15
- Fix an index out of range when calling dmidecode.memory().
- Resolves: #1665443

* Mon Apr 15 2019 Lianbo Jiang <lijiang@redhat.com> - 3.12.2-14
- Add the gating test
- Resolves: #1680625

* Fri Sep 14 2018 Lianbo Jiang <lijiang@redhat.com> - 3.12.2-13
- Disable build python-dmidecode package other than x86_64 architecture
- Resolves: #1626424

* Mon Jun 04 2018 Petr Viktorin <pviktori@redhat.com> - 3.12.2-12
- Drop the Python2 subpackage
  https://bugzilla.redhat.com/show_bug.cgi?id=1567417

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Iryna Shcherbina <ishcherb@redhat.com> - 3.12.2-10
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.12.2-9
- Python 2 binary package renamed to python2-dmidecode
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 3.12.2-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12.2-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Nov 07 2015 Robert Kuska <rkuska@redhat.com> - 3.12.2-2
- Rebuilt for Python3.5 rebuild

* Fri Jul 10 2015 Miro Hrončok <mhroncok@redhat.com> - 3.12.2-1
- Update to 3.12.2
- Add Python 3 subpackage (#1236000)
- Removed deprecated statements
- Moved some docs to license
- Removed pacthes
- Corrected bogus dates in %%changelog
- Build with -std=gnu89

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.13-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.13-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.13-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.13-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun 20 2013 Ales Ledvinka <aledvink@redhat.com> - 3.10.13-9
- Attribute installed may appear as duplicate and cause invalid XML.

* Mon Jun 17 2013 Ales Ledvinka <aledvink@redhat.com> - 3.10.13-8
- Attribute dmispec may cause invalid XML on some hardware.
- Signal handler for SIGILL.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jul 19 2012 Ales Ledvinka <aledvink@redhat.com> 3.10.14-5
- Upstream relocated. Document source tag and tarball generation.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 3.10.13-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Jun 15 2010 Roman Rakus <rrakus@redhat.com> - 3.10.13-1
- Update to new release

* Fri Mar 12 2010 Nima Talebi <nima@it.net.au> - 3.10.12-1
- Update to new release

* Tue Feb 16 2010 Nima Talebi <nima@it.net.au> - 3.10.11-1
- Update to new release

* Tue Jan 12 2010 Nima Talebi <nima@it.net.au> - 3.10.10-1
- Update to new release

* Thu Jan 07 2010 Nima Talebi <nima@it.net.au> - 3.10.9-1
- Update to new release


* Tue Dec 15 2009 Nima Talebi <nima@it.net.au> - 3.10.8-1
- New Upstream release.
- Big-endian and little-endian approved.
- Packaged unit-test to tarball.
- Rewritten unit-test to be able to run as non-root user, where it will not
  try to read /dev/mem.
- Added two dmidump data files to the unit-test.

* Thu Nov 26 2009 David Sommerseth <davids@redhat.com> - 3.10.7-3
- Fixed even more .spec file issues and removed explicit mentioning
  of /usr/share/python-dmidecode/pymap.xml

* Wed Nov 25 2009 David Sommerseth <davids@redhat.com> - 3.10.7-2
- Fixed some .spec file issues (proper Requires, use _datadir macro)

* Wed Sep 23 2009 Nima Talebi <nima@it.net.au> - 3.10.7-1
- Updated source0 to new 3.10.7 tar ball

* Mon Jul 13 2009 David Sommerseth <davids@redhat.com> - 3.10.6-6
- Only build the python-dmidecode module, not everything

* Mon Jul 13 2009 David Sommerseth <davids@redhat.com> - 3.10.6-5
- Added missing BuildRequres for libxml2-python

* Mon Jul 13 2009 David Sommerseth <davids@redhat.com> - 3.10.6-4
- Added missing BuildRequres for python-devel

* Mon Jul 13 2009 David Sommerseth <davids@redhat.com> - 3.10.6-3
- Added missing BuildRequres for libxml2-devel

* Mon Jul 13 2009 David Sommerseth <davids@redhat.com> - 3.10.6-2
- Updated release, to avoid build conflict

* Wed Jun 10 2009 David Sommerseth <davids@redhat.com> - 3.10.6-1
- Updated to work with the new XML based python-dmidecode

* Sat Mar  7 2009 Clark Williams <williams@redhat.com> - 2.10.3-1
- Initial build.

