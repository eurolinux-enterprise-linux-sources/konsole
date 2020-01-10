Name:    konsole
Summary: KDE Terminal emulator
Version: 4.10.5
Release: 4%{?dist}

# sources: MIT and LGPLv2 and LGPLv2+ and GPLv2+
License: GPLv2 and GFDL
URL:     http://konsole.kde.org/
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif 
Source0: ftp://ftp.kde.org/pub/kde/%{stable}/%{version}/src/%{name}-%{version}.tar.xz

Patch1:  konsole-avoid-repeated-calls-to-redusername-method.patch

BuildRequires: desktop-file-utils
BuildRequires: kdelibs4-devel >= %{version}
BuildRequires: kde-baseapps-devel >= %{version}
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xrender)

Requires: %{name}-part = %{version}-%{release}

%description
%{summary}.

%package part
Summary: Konsole kpart plugin
# when konsole split occurred
Conflicts: kdebase < 6:4.6.95-10
# when -part split occurred
Conflicts: konsole < 4.7.3-2 
Requires: kdelibs4%{?_isa}%{?_kde4_version: >= %{_kde4_version}}
%description part
%{summary}.


%prep
%setup -q

%patch1 -p1 -b .avoid-repeated-calls-to-redusername-method

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
rm -rf %{buildroot}

make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

%find_lang konsole --with-kde --without-mo


%check
desktop-file-validate %{buildroot}%{_kde4_datadir}/applications/kde4/konsole.desktop


%files -f konsole.lang
%doc README
%{_kde4_bindir}/konsole
%{_kde4_bindir}/konsoleprofile
%{_kde4_datadir}/applications/kde4/konsole.desktop
%{_kde4_libdir}/libkdeinit4_konsole.so
%{_kde4_datadir}/kde4/services/ServiceMenus/konsolehere.desktop
%{_kde4_appsdir}/kconf_update/konsole*

%files part
%doc COPYING*
%{_kde4_appsdir}/konsole/
%{_kde4_libdir}/libkonsoleprivate.so
%{_kde4_libdir}/kde4/libkonsolepart.so
%{_kde4_datadir}/kde4/services/konsolepart.desktop
%{_kde4_datadir}/kde4/servicetypes/terminalemulator.desktop


%changelog
* Thu Mar 24 2016 Jan Grulich <jgrulich@redhat.com> - 4.10.5-4
- Avoid repeated calls to readUserName() method
  Resolves: bz#1283800

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 4.10.5-3
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 4.10.5-2
- Mass rebuild 2013-12-27

* Sun Jun 30 2013 Than Ngo <than@redhat.com> - 4.10.5-1
- 4.10.5

* Sat Jun 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.4-1
- 4.10.4

* Mon May 06 2013 Than Ngo <than@redhat.com> - 4.10.3-1
- 4.10.3

* Sun Mar 31 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.2-1
- 4.10.2

* Sat Mar 02 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.1-1
- 4.10.1

* Fri Feb 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.0-1
- 4.10.0

* Sun Jan 20 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.9.98-1
- 4.9.98

* Fri Jan 04 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.9.97-1
- 4.9.97

* Thu Dec 20 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.9.95-1
- 4.9.95

* Tue Dec 04 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.9.90-1
- 4.9.90

* Mon Dec 03 2012 Than Ngo <than@redhat.com> - 4.9.4-1
- 4.9.4

* Fri Nov 23 2012 Than Ngo <than@redhat.com> - 4.9.3-2
- fix license issue

* Sat Nov 03 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.9.3-1
- 4.9.3

* Thu Oct 04 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.2-2
- Failed to launch Konsole ... Failed to change $HOME and there is no such directory (#861504)

* Sat Sep 29 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.9.2-1
- 4.9.2

* Mon Sep 24 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.1-2
- Konsole (or Terminal) start in /Documents folder (#841471)

* Mon Sep 03 2012 Than Ngo <than@redhat.com> - 4.9.1-1
- 4.9.1

* Thu Jul 26 2012 Lukas Tinkl <ltinkl@redhat.com> - 4.9.0-1
- 4.9.0

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.97-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 11 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.8.97-1
- 4.8.97

* Wed Jun 27 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.95-1
- 4.8.95

* Sat Jun 09 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.8.90-1
- 4.8.90

* Fri Jun 01 2012 Jaroslav Reznik <jreznik@redhat.com> 4.8.80-2
- respin

* Mon May 28 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.80-1
- 4.8.80

* Mon Apr 30 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.3-1
- 4.8.3

* Mon Apr 02 2012 Than Ngo <than@redhat.com> - 4.8.2-4
- respin

* Mon Apr 02 2012 Than Ngo <than@redhat.com> - 4.8.2-3
- add better workaround for kde#280896

* Sun Apr 01 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.2-2
- konsole crashes running 'ssh -t' (kde#297156)

* Fri Mar 30 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.2-1
- 4.8.2

* Mon Mar 05 2012 Radek Novacek <rnovacek@redhat.com> - 4.8.1-1
- 4.8.1

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.0-3
- Rebuilt for c++ ABI breakage

* Tue Jan 31 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.0-2
- improved 'fonts get chopped' patch, fixes ascenders too (#742583,kde#280896)

* Fri Jan 20 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.0-1
- 4.8.0

* Wed Jan 04 2012 Radek Novacek <rnovacek@redhat.com> - 4.7.97-1
- 4.7.97

* Tue Dec 27 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.95-2
- Some fonts get chopped (#742583,kde#280896)

* Wed Dec 21 2011 Radek Novacek <rnovacek@redhat.com> - 4.7.95-1
- 4.7.95

* Sun Dec 04 2011 Rex Dieter <rdieter@fedoraproject.org> - 4.7.90-1
- 4.7.90

* Fri Nov 25 2011 Radek Novacek <rnovacek@redhat.com> 4.7.80-1
- 4.7.80 (beta 1)
- add BR: kdebase-devel

* Tue Nov 15 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.3-2
- konsole-part subpkg

* Sat Oct 29 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.3-1
- 4.7.3

* Tue Oct 04 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.2-1
- 4.7.2

* Wed Sep 07 2011 Than Ngo <than@redhat.com> - 4.7.1-1
- 4.7.1

* Tue Jul 26 2011 Jaroslav Reznik <jreznik@redhat.com> 4.7.0-1
- 4.7.0

* Thu Jul 21 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.95-4
- fix Conflicts: kdebase (wrong epoch)

* Thu Jul 21 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.95-3
- License: GPLv2 (per FAQ)

* Thu Jul 21 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.95-2
- fix URL
- drop Requires: kdebase-runtime (overkill)
- License: +LGPLv2 

* Mon Jul 18 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.95-1
- first try
