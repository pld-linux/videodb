%define		dl_ver	2_0_2
Summary:	Video database
Summary(pl.UTF-8):   Katalog filmów
Name:		videodb
Version:	2.0.2
Release:	1
Epoch:		1
License:	GPL
Group:		Applications/Archiving
Source0:	http://dl.sourceforge.net/videodb/%{name}-%{dl_ver}.tgz
# Source0-md5:	96d82437bada963b72362d66c0a32e88
URL:		http://www.splitbrain.org/Programming/PHP/VideoDB/index.php
Requires:	php(mysql)
Requires:	webserver
Requires:	webserver(php) >= 4.2.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_instdir	/home/services/httpd/html/videodb

%description
VideoDB is a database to manage your personal video collection.

%description -l pl.UTF-8
VideoDB jest programem służącym do katalogowania kolekcji filmów.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_instdir}

cp -R * $RPM_BUILD_ROOT%{_instdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{*.sql,CHANGES,README,TODO,manual,development}
%{_instdir}
