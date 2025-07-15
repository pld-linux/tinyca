Summary:	Graphical Frontend for very simple Certification Authority
Summary(pl.UTF-8):	Graficzny interfejs do bardzo prostego Centrum Certyfikacji
Name:		tinyca
Version:	0.7.5
Release:	5
License:	GPL
Group:		Applications
Source0:	http://tinyca.sm-zone.net/%{name}2-%{version}.tar.bz2
# Source0-md5:	a7f63806dbdc38a34ed58e42e79f4822
Patch0:		%{name}-debian.patch
Patch1:		%{name}-sha2.patch
URL:		http://tinyca.sm-zone.net/
BuildRequires:	perl-Gtk2
BuildRequires:	perl-MIME-Base64
BuildRequires:	rpm-perlprov >= 3.0.3-16
Requires:	openssl-tools
Requires:	zip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Graphical Frontend for very simple CA. Based on OpenSSL and Perl-Tk.

%description -l pl.UTF-8
Graficzny interfejs do bardzo prostego CA. Bazuje na OpenSSL oraz
Perl-Tk.

%prep
%setup -q -n %{name}2-%{version}
%patch -P0 -p1
%patch -P1 -p1

%build
%{__perl} -pi -e 's:./lib:%{_datadir}/tinyca:g' tinyca2
%{__perl} -pi -e 's:./templates:%{_sysconfdir}/tinyca:g' tinyca2

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir}/tinyca,%{_datadir}/tinyca/GUI}

install lib/*.pm $RPM_BUILD_ROOT%{_datadir}/tinyca
install lib/GUI/*.pm $RPM_BUILD_ROOT%{_datadir}/tinyca/GUI
install templates/openssl.cnf $RPM_BUILD_ROOT%{_sysconfdir}/tinyca
install tinyca2 $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES
%attr(755,root,root) %{_bindir}/*
%{_datadir}/tinyca
%dir %{_sysconfdir}/tinyca
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/tinyca/*.*
