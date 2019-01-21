# traefik-spec
RPM SPEC files for creating traefik package

# test build

    sudo dnf install rpmbuild -y
    mkdir -p ~/rpmbuild/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS}
    rpmbuild --undefine=_disable_source_fetch  -bb traefik.spec
