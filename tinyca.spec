%include        /usr/lib/rpm/macros.perl
Summary:	Graphical Frontend for very simple Certification Authority
Summary(pl):	Graficzny interfejs do bardzo prostego Centrum Certyfikacji
Name:		tinyca
Version:	0.7.1
Release:	1
License:	GPL
Group:		Applications
Source0:	http://tinyca.sm-zone.net/%{name}2-%{version}.tar.bz2
# Source0-md5:	2ee7a3f7414f6b7147f6c20c23749777
URL:		http://tinyca.sm-zone.net/
BuildRequires:	perl-Gtk2
BuildRequires:	perl-MIME-Base64
BuildRequires:	perl-gnome
BuildRequires:	rpm-perlprov >= 3.0.3-16
Requires:	openssl-tools
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Graphical Frontend for very simple CA. Based on OpenSSL and Perl-Tk.

%description -l pl
Graficzny interfejs do bardzo prostego CA. Bazuje na OpenSSL oraz
Perl-Tk.

%prep
%setup -q -n %{name}2-%{version}

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
