%include        /usr/lib/rpm/macros.perl
Summary:	Graphical Frontend for very simple Certification Authority
Summary(pl):	Graficzny interfejs do bardzo prostego Centrum Certyfikacji
Name:		tinyca
Version:	0.5.2
Release:	2
License:	GPL
Group:		Applications
Source0:	http://tinyca.sm-zone.net/%{name}-%{version}.tar.bz2
# Source0-md5:	572d51f95b65cbff16a0b4a566319645
URL:		http://tinyca.sm-zone.net/
BuildRequires:	perl-MIME-Base64
BuildRequires:	perl-Tk
BuildRequires:	rpm-perlprov >= 3.0.3-16
Requires:	openssl-tools
BuildArch:	noarch
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Graphical Frontend for very simple CA. Based on OpenSSL and Perl-Tk.

%description -l pl
Graficzny interfejs do bardzo prostego CA. Bazuje na OpenSSL oraz
Perl-Tk.

%prep
%setup -q -n TinyCA

%build
%{__perl} -pi -e 's:./lib:%{_datadir}/tinyca:g' tinyca
%{__perl} -pi -e 's:./templates:%{_sysconfdir}/tinyca:g' tinyca

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir}/tinyca,%{_datadir}/tinyca}

install lib/*.pm $RPM_BUILD_ROOT%{_datadir}/tinyca
install templates/openssl.cnf $RPM_BUILD_ROOT%{_sysconfdir}/tinyca
install tinyca $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES
%attr(755,root,root) %{_bindir}/*
%{_datadir}/tinyca
%dir %{_sysconfdir}/tinyca
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/tinyca/*.*
