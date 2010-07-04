Name:       parsidora-logos
Version:    13.0
Release:    2%{?dist}
Summary:    Parsidora Icons and pictures

Group:      System Environment/Base
URL:        http://parsidora.ir/parsidora-logos/ 
Source0:    http://parsidora.ir/released/%{name}/%{name}-%{version}.tar.bz2
#The KDE Logo is under a LGPL license (no version statement)
License:    GPLv2 and LGPLv2+
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:  noarch

Obsoletes:  redhat-logos
Provides:   redhat-logos = %{version}-%{release}
Provides:   system-logos = %{version}-%{release}

Conflicts:  fedora-logos
Conflicts:  kdebase <= 3.1.5
Conflicts:  anaconda-images <= 10
Conflicts:  redhat-artwork <= 5.0.5
Conflicts:  generic-logos
# For _kde4_appsdir macro:
BuildRequires: kde-filesystem


%description
This package contains various image files which will be used by the bootloader,
anaconda, and other related tools in Parsidora replacing fedora-logos package.

%prep
%setup -q

%build
#nothing to build

%install
rm -rf %{buildroot}

# should be ifarch i386
mkdir -p %{buildroot}/boot/grub
install -p -m 644 bootloader/splash.xpm.gz %{buildroot}/boot/grub/splash.xpm.gz
# end i386 bits

mkdir -p %{buildroot}%{_datadir}/firstboot/themes/parsidora
for i in firstboot/* ; do
  install -p -m 644 $i %{buildroot}%{_datadir}/firstboot/themes/parsidora
done

mkdir -p %{buildroot}%{_datadir}/pixmaps/splash
for i in gnome-splash/* ; do
  install -p -m 644 $i %{buildroot}%{_datadir}/pixmaps/splash
done

mkdir -p %{buildroot}%{_datadir}/pixmaps
for i in pixmaps/* ; do
  install -p -m 644 $i %{buildroot}%{_datadir}/pixmaps
done

mkdir -p %{buildroot}%{_datadir}/kde-settings/kde-profile/default/share/icons/Fedora-KDE/48x48/apps/
install -p -m 644 icons/Fedora/48x48/apps/* %{buildroot}%{_datadir}/kde-settings/kde-profile/default/share/icons/Fedora-KDE/48x48/apps/
mkdir -p %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Leonidas/2048x1536
install -p -m 644 ksplash/SolarComet-kde.png %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Leonidas/2048x1536/logo.png

mkdir -p $RPM_BUILD_ROOT%{_datadir}/plymouth/themes/charge/
for i in plymouth/charge/* ; do
    install -p -m 644 $i $RPM_BUILD_ROOT%{_datadir}/plymouth/themes/charge/
done

# File or directory names do not count as trademark infringement
mkdir -p %{buildroot}%{_datadir}/icons/Fedora/48x48/apps/
mkdir -p %{buildroot}%{_datadir}/icons/Fedora/scalable/apps/
install -p -m 644 icons/Fedora/48x48/apps/* %{buildroot}%{_datadir}/icons/Fedora/48x48/apps/
install	-p -m 644 icons/Fedora/scalable/apps/* %{buildroot}%{_datadir}/icons/Fedora/scalable/apps/

(cd anaconda; make DESTDIR=%{buildroot} install)

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING COPYING-kde-logo README
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
* Sun Jul 04 2010 Hedayat Vatankhah <hedayat@grad.com> - 13.0-2
- Do not overwrite progress_first.png
- Added a splash-small.png for firstboot
- Added a plymouth theme

* Sat May 15 2010 Hedayat Vatankhah <hedayat@grad.com> - 13.0-1
- Updated for Fedora 13

* Tue Jan 26 2010 Hedayat Vatankhah <hedayat@grad.com> - 12.2-1
- Initial version. Forked from generic-logos-12.2-2 package
