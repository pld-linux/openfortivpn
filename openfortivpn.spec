Summary:	Client for PPP+SSL VPN tunnel services
Summary(pl.UTF-8):	Klient usług tunelowych VPN PPP+SSL
Name:		openfortivpn
Version:	1.10.0
Release:	1
License:	GPL v3+ with OpenSSL exception
Group:		Networking
#Source0Download: https://github.com/adrienverge/openfortivpn/releases
Source0:	https://github.com/adrienverge/openfortivpn/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	bfbbb82e31acb26cafa6b5aefc453eba
URL:		https://github.com/adrienverge/openfortivpn
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake
BuildRequires:	openssl-devel >= 0.9.8
BuildRequires:	pkgconfig
BuildRequires:	systemd-devel >= 1:209
Requires:	ppp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
openfortivpn is a client for PPP+SSL VPN tunnel services. It spawns a
pppd process and operates the communication between the gateway and
this process.

It is compatible with Fortinet VPNs.

%description -l pl.UTF-8
openfortivpn to klient usług tunelowych VPN PPP+SSL. Uruchamia proces
pppd i nadzoruje komunikację pomiędzy bramką a tym procesem.

Jest zgodny z VPN-ami Fortinet.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-proc \
	--disable-silent-rules \
	--with-pppd=/usr/sbin/pppd
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_datadir}/openfortivpn/config.template

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE.OpenSSL README.md
%attr(755,root,root) %{_bindir}/openfortivpn
%dir %{_sysconfdir}/openfortivpn
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/openfortivpn/config
%{_mandir}/man1/openfortivpn.1*
