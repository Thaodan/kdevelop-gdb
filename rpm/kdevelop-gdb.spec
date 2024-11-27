Name: kdevelop-gdb
Version: 24.11.80
Summary: KDevelop's GDB printers for Qt and KDE types
Release: 0
License: GPL-2.0-or-later
URL: https://invent.kde.org/kdevelop/kdevelop.git
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Supplements: gdb
BuildArch: noarch

%description
KDevelop but just it's GDB pretty printers. 

%prep
%autosetup -p1 -n %{name}-%{version}/upstream

%build
true

%install
cd plugins/gdb/printers
install qt.py -Dm644 %{buildroot}/%{_datadir}/kdevgdb/printers/qt.py
install kde.py -Dm644 %{buildroot}/%{_datadir}/kdevgdb/printers/kde.py
install helper.py -Dm644 %{buildroot}/%{_datadir}/kdevgdb/printers/helper.py
install gdbinit -Dm644 %{buildroot}/%{_datadir}/kdevgdb/printers/gdbinit


%files
%license LICENSES/GPL-2.0-or-later.txt
%{_datadir}/kdevgdb/printers/qt.py
%{_datadir}/kdevgdb/printers/kde.py
%{_datadir}/kdevgdb/printers/helper.py
%{_datadir}/kdevgdb/printers/gdbinit
