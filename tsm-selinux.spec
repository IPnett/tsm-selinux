%define _prefix   /

Name:       tsm-selinux
Version:    2.0.0
Release:    4%{?dist}
Summary:    SELinux Policy for tsm

Group:      System Environment/Base
BuildArch:  noarch
License:    GPLv2
Requires:       policycoreutils, libselinux-utils
Requires(post):     selinux-policy-base >= %{selinux_policyver}, selinux-policy-targeted >= %{selinux_policyver}, policycoreutils, policycoreutils-python
Requires(postun):   policycoreutils
BuildRequires:      selinux-policy selinux-policy-devel
Source0:        ./tsm.pp


%description
SELinux Policy module for use with tsm


%prep

%build

%install
install -D %{S:0} %{buildroot}%{_prefix}/usr/share/selinux/packages/tsm/tsm.pp


%files
%dir %attr(0700, root, root) /usr/share/selinux/packages/tsm/
%attr(0600, root, root) /usr/share/selinux/packages/tsm/tsm.pp

%post
    /usr/sbin/semodule -i /usr/share/selinux/packages/tsm/tsm.pp
    for i in /etc/adsm /opt/tivoli/tsm/client /var/log/tsm; do
        if [ -d "$i" ] ; then
            /sbin/restorecon -R $i
        fi
    done
    #label all the ports.
    /sbin/semanage port -a -t tsmadmin_ssl_port_t -p tcp 1601
    /sbin/semanage port -a -t tsm_ssl_port_t -p tcp 1600

%postun
if [ $1 -eq 0 ]; then
    /usr/sbin/semodule -r tsm
    for i in /etc/adsm /opt/tivoli/tsm/client /var/log/tsm; do
        if [ -d "$i" ] ; then
            /sbin/restorecon -R $i
        fi
    done
    /sbin/semanage port -d -t tsmadmin_ssl_port_t -p tcp 1601
    /sbin/semanage port -d -t tsm_ssl_port_t -p tcp 1600
fi


%changelog
