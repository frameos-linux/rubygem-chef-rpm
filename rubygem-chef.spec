# Generated from chef-0.9.12.gem by gem2rpm -*- rpm-spec -*-
%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname chef
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: A systems integration framework, built to bring the benefits of configuration management to your entire infrastructure
Name: rubygem-%{gemname}
Version: 0.9.12
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://wiki.opscode.com/display/chef
Source0: http://gemcutter.orggems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: rubygems
Requires: rubygem(mixlib-config) >= 1.1.2
Requires: rubygem(mixlib-cli) >= 1.1.0
Requires: rubygem(mixlib-log) >= 1.2.0
Requires: rubygem(mixlib-authentication) >= 1.1.0
Requires: rubygem(ohai) >= 0.5.7
Requires: rubygem(rest-client) >= 1.0.4
Requires: rubygem(rest-client) < 1.7.0
Requires: rubygem(bunny) >= 0.6.0
Requires: rubygem(json) >= 1.4.4
Requires: rubygem(json) <= 1.4.6
Requires: rubygem(erubis) >= 0
Requires: rubygem(extlib) >= 0
Requires: rubygem(moneta) >= 0
Requires: rubygem(highline) >= 0
Requires: rubygem(uuidtools) >= 0
BuildRequires: rubygems
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

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
* Sun Dec 19 2010 Sergio Rubio <rubiojr@frameos.org> - 0.9.12-1
- Initial package
