%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}
%global enable_tests 0
%{?nodejs_find_provides_and_requires}

%global npm_name escape-string-regexp

Summary:       Escape RegExp special characters
Name:          %{?scl_prefix}nodejs-%{npm_name}
Version:       1.0.5
Release:       1%{?dist}
License:       MIT
URL:           https://github.com/sindresorhus/escape-string-regexp
Source0:       http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: %{?scl_prefix}runtime
ExclusiveArch: %{nodejs_arches} noarch
BuildArch:     noarch

%if 0%{enable_tests}
BuildRequires:    %{?scl_prefix}npm(xo)
BuildRequires:    %{?scl_prefix}npm(ava)
%endif

%description
Escape RegExp special characters

%prep
%setup -q -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr index.js package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
xo && ava
%endif

%files
%doc license readme.md
%{nodejs_sitelib}/%{npm_name}

%changelog
* Wed Sep 07 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.5-1
- Updated with script

* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.3-6
- Use macro in -runtime dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.3-5
- Rebuilt with updated metapackage

* Thu Jan 14 2016 Tomas Hrcka <thrcka@redhat.com> - 1.0.3-4
- Enable find provides and requires macro

* Mon Jan 11 2016 Tomas Hrcka <thrcka@redhat.com> - 1.0.3-3
- Enable scl macros

* Mon Sep 14 2015 Troy Dawson <tdawson@redhat.com> - 1.0.3-1
- Initial package
