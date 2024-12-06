Name:		docuum
Version:	0.25.0
Release:	1%{?dist}
Summary:	LRU eviction of Docker images

License:	MIT
URL:		https://github.com/stepchowfun/docuum
Source0:	docuum-x86_64-unknown-linux-musl
Source1:	docuum-aarch64-unknown-linux-musl

%description
Docuum performs least recently used (LRU) eviction of Docker images to keep the disk usage below a given threshold.

%prep
exit 0


%build
exit 0

%install
mkdir -p %{buildroot}/usr/local/sbin
%ifarch x86_64
install -pm 0755 %{SOURCE0} %{buildroot}/usr/local/sbin/docuum
%endif
%ifarch aarch64
install -pm 0755 %{SOURCE1} %{buildroot}/usr/local/sbin/docuum
%endif


%files
/usr/local/sbin/docuum


%changelog
* Fri Dec 06 2024 Tim Theisen <tim@cs.wisc.edu> - 0.25.0-1
- Initial packaging of docuum binaries

