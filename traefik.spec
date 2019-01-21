%global		debug_package	%{nil}

%define		pkg_release	    1
%define		git_bin_name	traefik_linux-amd64

Name:		traefik
Version:	1.7.7
Release:	%{pkg_release}%{?dist}
Summary:	The Cloud Native Edge Router https://traefik.io

License:	MIT
URL:		https://traefik.io
Source0:	https://github.com/containous/traefik/releases/download/v%{version}/%{git_bin_name}
Source1:	%{name}.service
Source2:	traefik.toml
Source3:	rules.toml

BuildRequires: systemd
Requires(pre): shadow-utils

%description
    Traefik is a modern HTTP reverse proxy and load balancer that makes
    deploying microservices easy. Traefik integrates with your existing
    infrastructure components (Docker, Swarm mode, Kubernetes, Marathon,
    Consul, Etcd, Rancher, Amazon ECS, ...) and configures itself 
    automatically and dynamically. Pointing Traefik at your orchestrator
    should be the only configuration step you need.

%install
#   create installation hierarchy
    %{__mkdir} -p %{buildroot}%{_bindir}
    %{__mkdir} -p %{buildroot}%{_unitdir}
    %{__mkdir} -p %{buildroot}%{_sysconfdir}/%{name}
    %{__mkdir} -p %{buildroot}%{_sharedstatedir}/%{name}
    %{__cp}   -p %{_sourcedir}/%{git_bin_name}    %{buildroot}%{_bindir}/%{name}
    %{__cp}   -p %{_sourcedir}/%{name}.service    %{buildroot}%{_unitdir}/
    %{__cp}   -p %{SOURCE2}                       %{buildroot}%{_sysconfdir}/%{name}/
    %{__cp}   -p %{SOURCE3}                       %{buildroot}%{_sysconfdir}/%{name}/

%files
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%config %{_sysconfdir}/%{name}/*.toml
%dir %attr(0751, %{name}, %{name}) %{_sysconfdir}/%{name}/
%dir %{_sharedstatedir}/%{name}

%clean
%{__rm} -rf $RPM_BUILD_ROOT


%pre
getent group GROUPNAME >/dev/null || groupadd -r GROUPNAME
getent passwd USERNAME >/dev/null || \
    useradd -r -g traefik -d /var/lib/treafik -s /sbin/nologin \
    -c "The Cloud Native Edge Router" traefik
exit 0


%changelog
* Mon Jan 21 2019 Anatolii Vorona <vorona.tolik@gmail.com>
- init COPR repo
