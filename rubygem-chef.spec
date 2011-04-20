# Generated from chef-0.10.0.beta.9.gem by gem2rpm -*- rpm-spec -*-
%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname chef
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: A systems integration framework, built to bring the benefits of configuration management to your entire infrastructure
Name: rubygem-%{gemname}
Version: 0.10.0.rc.0
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://wiki.opscode.com/display/chef
Source0: http://rubygems.org/downloads/%{gemname}-%{version}.gem
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
gem install --local --install-dir %{buildroot}%{gemdir} \
            --force --rdoc %{SOURCE0}
mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{gemdir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{gemdir}/bin
find %{buildroot}%{geminstdir}/bin -type f | xargs chmod a+x

%clean
rm -rf %{buildroot}

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


%changelog
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
