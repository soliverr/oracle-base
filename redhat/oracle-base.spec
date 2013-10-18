#
# $Id$
#

Summary   :  Directory layout for Oracle Software.
Summary(ru_RU.UTF-8)   : Иерархия каталогов для ПО Oracle.
Name      : oracle-base
Version   : 3.0
Release   : 1
Group     : RDBMS

Packager  : Kryazhevskikh Sergey, <soliverr@gmail.com>
License   : GPLv2

BuildArch : noarch
Requires  : bash, shadow-utils

Source: %name-%version.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}

%define pkg_build_dir   %_builddir/%name-%version
%define pkg_functions   %pkg_build_dir/_pkg-functions

%description
Directory layout and system users and groups for Oracle Software.

%description -l ru_RU.UTF-8
Иерархия каталогов и базовые системные пользователи и группы для 
программного обеспечения Oracle.

%prep

%setup -q

%build

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%{__install} -d %{buildroot}/etc/oracle
%{__install} -d %{buildroot}/opt/oracle
%{__install} -d %{buildroot}/tmp/.oracle
%{__install} -d %{buildroot}/var/tmp/.oracle
%{__install} -d %{buildroot}/var/log/oracle/
%{__install} -d %{buildroot}/var/spool/oracle/
%{__install} -D orabase-functions %{buildroot}/lib/lsb/orabase-functions

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%pre
%include %{pkg_functions}

if [ $1 -eq 1 ] ; then
  action=install
else
  action=upgrade
fi

preinst "redhat" "$action"


%preun
%include %pkg_functions

if [ $1 -eq 0 ] ; then
  action=remove
else
  action=upgrade
fi

prerm "redhat" "$action"

%post
%include %pkg_functions

if [ $1 -eq 1 ] ; then
  action=configure
else
  action=upgrade
fi

postinst "redhat" "$action"

%postun
%include %pkg_functions

if [ $1 -eq 0 ] ; then
  action=purge
else
  action=upgrade
fi

postrm "redhat" "$action"


%files
%defattr(-,root,root)
%doc README
%dir /opt/oracle
%dir %attr(2775,oracle,oinstall) /etc/oracle
%dir %attr(2775,oracle,oinstall) /var/log/oracle
%dir %attr(2775,oracle,oinstall) /var/spool/oracle
%dir %attr(1777,-,-) /var/tmp/.oracle
%dir %attr(1777,-,-) /tmp/.oracle
%attr(644,-,-) /lib/lsb/*

%changelog
* Fri Oct 18 2013 Kryazhevskikh Sergey <soliverr@gmail.com> - 3.0-1  11:51:03 +0600
- Added orabase-functions [tickets:#4]
- Added /var/spool/oracle directory
- Change default group for directories to `oinstall'

* Thu Aug 18 2011 Kryazhevskikh Sergey <soliverr@gmail.com> - 2.0-1  17:00:04 +0600
- New base directories for Oracle software
- `oinstall' group for Oracle software

* Thu Aug 04 2011 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-3  17:24:49 +0600
- Added oraInventory directory

* Wed May 25 2011 Kryazhevskikh Sergey <soliverr@gmail.com> - 1.0-1  13:00:06 +0600
- Initial version of package.
