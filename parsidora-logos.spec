Name: parsidora-logos
Summary: Parsidora Icons and pictures
Version: 12.2
Release: 1%{?dist}
Group: System Environment/Base
Source0: parsidora-logos-%{version}.tar.bz2
License: GPLv2 and LGPL
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
Obsoletes: redhat-logos
Provides: redhat-logos = %{version}-%{release}
Provides: system-logos = %{version}-%{release}
Conflicts: generic-logos
Conflicts: fedora-logos
Conflicts: kdebase <= 3.1.5
Conflicts: anaconda-images <= 10
Conflicts: redhat-artwork <= 5.0.5
# For _kde4_appsdir macro:
BuildRequires: kde-filesystem


%description
This package contains various image files which will be used by the bootloader,
anaconda, and other related tools in Parsidora replacing fedora-logos package.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT

# should be ifarch i386
mkdir -p $RPM_BUILD_ROOT/boot/grub
install -p -m 644 bootloader/splash.xpm.gz $RPM_BUILD_ROOT/boot/grub/splash.xpm.gz
# end i386 bits

mkdir -p $RPM_BUILD_ROOT%{_datadir}/firstboot/themes/parsidora
for i in firstboot/* ; do
  install -p -m 644 $i $RPM_BUILD_ROOT%{_datadir}/firstboot/themes/parsidora
done

mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps/splash
for i in gnome-splash/* ; do
  install -p -m 644 $i $RPM_BUILD_ROOT%{_datadir}/pixmaps/splash
done

mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
for i in pixmaps/* ; do
  install -p -m 644 $i $RPM_BUILD_ROOT%{_datadir}/pixmaps
done

mkdir -p $RPM_BUILD_ROOT%{_datadir}/kde-settings/kde-profile/default/share/icons/Fedora-KDE/48x48/apps/
install -p -m 644 icons/Fedora/48x48/apps/* $RPM_BUILD_ROOT%{_datadir}/kde-settings/kde-profile/default/share/icons/Fedora-KDE/48x48/apps/
mkdir -p $RPM_BUILD_ROOT%{_kde4_appsdir}/ksplash/Themes/Leonidas/2048x1536
install -p -m 644 ksplash/SolarComet-kde.png $RPM_BUILD_ROOT%{_kde4_appsdir}/ksplash/Themes/Leonidas/2048x1536/logo.png

mkdir -p $RPM_BUILD_ROOT%{_datadir}/plymouth/themes/charge/
for i in plymouth/charge/* ; do
    install -p -m 644 $i $RPM_BUILD_ROOT%{_datadir}/plymouth/themes/charge/
done

# File or directory names do not count as trademark infringement
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/Fedora/48x48/apps/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/Fedora/scalable/apps/
install -p -m 644 icons/Fedora/48x48/apps/* $RPM_BUILD_ROOT%{_datadir}/icons/Fedora/48x48/apps/
install	-p -m 644 icons/Fedora/scalable/apps/* $RPM_BUILD_ROOT%{_datadir}/icons/Fedora/scalable/apps/

(cd anaconda; make DESTDIR=$RPM_BUILD_ROOT install)

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc COPYING COPYING-kde-logo
%{_datadir}/firstboot/themes/*
%{_datadir}/anaconda/pixmaps/*
%{_datadir}/icons/Fedora/*/apps/*
%{_datadir}/pixmaps/*
%{_datadir}/plymouth/themes/charge/*
/usr/lib/anaconda-runtime/*.jpg
%{_kde4_appsdir}/ksplash/Themes/Leonidas/2048x1536/logo.png
%{_datadir}/kde-settings/kde-profile/default/share/icons/Fedora-KDE/*/apps/*
# should be ifarch i386
/boot/grub/splash.xpm.gz
# end i386 bits

%changelog
* Tue Jan 26 2010 Hedayat Vatankhah <hedayat@grad.com> - 12.2-1
- Initial version. Forked from generic-logos-12.2-2 package
