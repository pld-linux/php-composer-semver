%define		pkgname	semver
Summary:	Semver library that offers utilities, version constraint parsing and validation
Name:		php-composer-%{pkgname}
Version:	1.5.0
Release:	1
License:	MIT
Group:		Development/Libraries
Source0:	https://github.com/composer/semver/archive/%{version}/%{pkgname}-%{version}.tar.gz
# Source0-md5:	e20956c037edbcae3517e9eb8a4d3f30
Patch0:		versionparser.patch
URL:		https://github.com/composer/semver
Requires:	php(core) >= 5.3.2
Requires:	php(pcre)
Requires:	php(spl)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Semver library that offers utilities, version constraint parsing and
validation.

Originally written as part of composer/composer, now extracted and
made available as a stand-alone library.

%prep
%setup -q -n %{pkgname}-%{version}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}/Composer/Semver
cp -a src/* $RPM_BUILD_ROOT%{php_data_dir}/Composer/Semver

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.md LICENSE
# NOTE: dir shared with composer
%dir %{php_data_dir}/Composer
%{php_data_dir}/Composer/Semver
