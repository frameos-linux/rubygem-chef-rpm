# Generated from chef-0.10.0.beta.9.gem by gem2rpm -*- rpm-spec -*-
%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname chef
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: A systems integration framework, built to bring the benefits of configuration management to your entire infrastructure
Name: rubygem-%{gemname}
Version: 0.10.4
Release: 1%{?buildstamp}%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://wiki.opscode.com/display/chef
Source0: http://rubygems.org/downloads/%{gemname}-%{version}.rc.4.1.gem
Source1: chef-client.init
Source2: chef-client.sysconfig
Source3: chef-client.logrotate
Source4: yum.rb

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: rubygems
Requires: rubygem(mixlib-config) >= 1.1.2
Requires: rubygem(mixlib-cli) >= 1.1.0
Requires: rubygem(mixlib-log) >= 1.3.0
Requires: rubygem(mixlib-authentication) >= 1.1.0
Requires: rubygem(ohai) >= 0.6
Requires: rubygem(rest-client) >= 1.0.4
Requires: rubygem(rest-client) < 1.7.0
Requires: rubygem(bunny) >= 0.6.0
Requires: rubygem(json) >= 1.4.4
Requires: rubygem(json) <= 1.4.6
Requires: rubygem(treetop) >= 1.4.9
Requires: rubygem(net-ssh) >= 2.1.3
Requires: rubygem(net-ssh-multi) >= 1.0.1
Requires: rubygem(erubis) >= 0
Requires: rubygem(moneta) >= 0
Requires: rubygem(highline) >= 0
Requires: rubygem(uuidtools) >= 0
Requires: ruby >= 1.8.7
BuildRequires: rubygems
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}
Obsoletes: chef

%description
A systems integration framework, built to bring the benefits of configuration
management to your entire infrastructure.


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
mkdir -p %{buildroot}/etc/rc.d/init.d
mkdir -p %{buildroot}/var/log/chef
mkdir -p %{buildroot}%{_sysconfdir}/chef
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig/
mkdir -p %{buildroot}/var/run/chef
mkdir -p %{buildroot}/var/log/chef
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
#chef needs /var/chef/cache in 0.10
mkdir -p %{buildroot}/var/chef/cache

gem install --local --install-dir %{buildroot}%{gemdir} \
            --force --rdoc %{SOURCE0}
mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{gemdir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{gemdir}/bin
find %{buildroot}%{geminstdir}/bin -type f | xargs chmod a+x

cp %{SOURCE1} %{buildroot}/etc/rc.d/init.d/chef-client
chmod +x %{buildroot}/etc/rc.d/init.d/chef-client
cp %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/chef-client
cp %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/chef-client
cp %{SOURCE4} %{buildroot}/usr/lib/ruby/gems/1.8/gems/chef-%{version}/lib/chef/provider/package/yum.rb


%clean
rm -rf %{buildroot}

%post
# This adds the proper /etc/rc*.d links for the script
/sbin/chkconfig --add chef-client

%preun
if [ $1 -eq 0 ] ; then
    /sbin/service chef-client stop >/dev/null 2>&1
    /sbin/chkconfig --del chef-client
fi

%files
%defattr(-, root, root, -)
%{_bindir}/chef-client
%{_bindir}/chef-solo
%{_bindir}/knife
%{_bindir}/shef
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/README.rdoc
%doc %{geminstdir}/LICENSE
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec
%config(noreplace) %{_sysconfdir}/sysconfig/chef-client
%config(noreplace) %{_sysconfdir}/logrotate.d/chef-client
%{_sysconfdir}/rc.d/init.d/chef-client
/var/log/chef/
/var/chef/cache/
%config(noreplace) %{_sysconfdir}/chef


%changelog
* Wed Jul 27 2011 Sergio Rubio <rubiojr@frameos.org> - 0.10.4-1
- preparing for 0.10.4 RC

* Mon Jul 25 2011 Sergio Rubio <rubiojr@frameos.org> - 0.10.2-3
- updated release version format

* Mon Jul 25 2011 Sergio Rubio <rubiojr@frameos.org> - 0.10.2-2
- added buildstamp to release

* Mon Jul 04 2011 Sergio Rubio <srubio@abiquo.com> - 0.10.2-1
- upstream update

* Fri Jun 10 2011 Sergio Rubio <rubiojr@frameos.org> - 0.10.0-5
- patch yum provider

* Fri May 06 2011 Sergio Rubio <rubiojr@frameos.org> - 0.10.0-4
- create /var/log/chef dir

* Thu May 05 2011 Sergio Rubio <rubiojr@frameos.org> - 0.10.0-3
- require ruby >= 1.8.7

* Thu May 05 2011 Sergio Rubio <rubiojr@frameos.org> - 0.10.0-2
- added init script
- added logrotate script
- added sysconfig file

* Tue May 03 2011 Sergio Rubio <rubiojr@frameos.org> - 0.10.0-1
- upstream update

* Mon May 02 2011 Sergio Rubio <rubiojr@frameos.org> - 0.10.0.rc.2-1
- upstream update

* Thu Apr 28 2011 Sergio Rubio <rubiojr@frameos.org> - 0.10.0.rc.1-1
- upstream update

* Wed Apr 20 2011 Sergio Rubio <rubiojr@frameos.org> - 0.10.0.rc.0-2
- bumped release
- create /var/chef/cache

* Wed Apr 20 2011 Sergio Rubio <rubiojr@frameos.org> - 0.10.0.rc.0-1
- bumped version

* Thu Apr 14 2011 Sergio Rubio <rubiojr@frameos.org> - 0.10.0.beta.10-3
- depend on ohai >= 0.6

* Thu Apr 14 2011 Sergio Rubio <rubiojr@frameos.org> - 0.10.0.beta.10-2
- obsoletes chef

* Thu Apr 13 2011 Sergio Rubio <rubiojr@frameos.org> - 0.10.0.beta.10-1
- bumped version

* Tue Apr 12 2011 Sergio Rubio <rubiojr@frameos.org> - 0.10.0.beta.9-1
- Initial package
