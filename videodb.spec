%define		dl_ver	2004-08-01
Summary:	Video database
Summary(pl):	Katalog filmów
Name:		videodb
Version:	20040801
Release:	1
License:	GPL
Group:		Applications/Archiving
Source0:	http://dl.sourceforge.net/videodb/%{name}-%{dl_ver}.tgz
# Source0-md5:	9a71671f09b9b4d7f79a5545b840973c
Patch0:		%{name}-install_fix.patch
URL:		http://www.splitbrain.org/Programming/PHP/VideoDB/index.php
BuildArch:	noarch
Requires:	php >= 4.1.0
Requires:	php-mysql
Requires:	webserver
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_instdir	/home/services/httpd/html/videodb

%description
VideoDB is a database to manage your personal video collection.

%description -l pl
VideoDB jest programem s³u¿±cym do katalogowania kolekcji filmów.

%prep
%setup -q -n %{name}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_instdir}

cp -R * $RPM_BUILD_ROOT%{_instdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{CHANGES,README,TODO,manual}
%{_instdir}
