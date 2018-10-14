%global provider        github
%global provider_tld    com
%global project         swaywm
%global repo            sway
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global commit          e6a52ae387ff3db64cc0867415368bd711c41566
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           sway
Version:        1.0
Release:        0.6.git%{shortcommit}%{?dist}
Summary:        i3-compatible Wayland compositor
License:        MIT
URL:            http://swaywm.org/
# https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz
Source:         https://github.com/swaywm/%{name}/archive/%{version}-alpha.6.tar.gz
Requires:       cairo
Requires:       gdk-pixbuf2
Requires:       json-c
Requires:       libcap
Requires:       pango
Requires:       pcre
Requires:       wlroots
Requires:       xcb-util-image
BuildRequires:  cairo-devel
BuildRequires:  gcc
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  git
BuildRequires:  json-c-devel
BuildRequires:  libcap-devel
BuildRequires:  meson
BuildRequires:  pam-devel
BuildRequires:  pango-devel
BuildRequires:  pcre-devel
BuildRequires:  scdoc
BuildRequires:  wayland-protocols-devel
BuildRequires:  wlroots-devel
BuildRequires:  xcb-util-image-devel

%description
%{summary}.

%prep
%setup -q -n %{repo}-%{version}-alpha.6

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license LICENSE
%doc README*.md
%doc CONTRIBUTING.md
%doc HACKING.md
%{_sysconfdir}/pam.d/swaylock
%{_sysconfdir}/sway/config
%{_sysconfdir}/sway/security.d/00-defaults
%caps(cap_sys_admin=pe cap_sys_ptrace=pe) %{_bindir}/sway
%{_bindir}/swaybar
%{_bindir}/swaybg
%{_bindir}/swayidle
%{_bindir}/swaylock
%{_bindir}/swaymsg
%{_bindir}/swaynag
%{_datarootdir}/backgrounds/sway/Sway_Wallpaper_Blue_1136x640.png
%{_datarootdir}/backgrounds/sway/Sway_Wallpaper_Blue_1136x640_Portrait.png
%{_datarootdir}/backgrounds/sway/Sway_Wallpaper_Blue_1366x768.png
%{_datarootdir}/backgrounds/sway/Sway_Wallpaper_Blue_1920x1080.png
%{_datarootdir}/backgrounds/sway/Sway_Wallpaper_Blue_2048x1536.png
%{_datarootdir}/backgrounds/sway/Sway_Wallpaper_Blue_2048x1536_Portrait.png
%{_datarootdir}/backgrounds/sway/Sway_Wallpaper_Blue_768x1024.png
%{_datarootdir}/backgrounds/sway/Sway_Wallpaper_Blue_768x1024_Portrait.png
%{_datarootdir}/bash-completion/completions/sway
%{_datarootdir}/bash-completion/completions/swayidle
%{_datarootdir}/bash-completion/completions/swaylock
%{_datarootdir}/bash-completion/completions/swaymsg
%{_datarootdir}/fish/completions/sway.fish
%{_datarootdir}/fish/completions/swaylock.fish
%{_datarootdir}/fish/completions/swaymsg.fish
%{_mandir}/man1/sway.1.gz
%{_mandir}/man1/swayidle.1.gz
%{_mandir}/man1/swaylock.1.gz
%{_mandir}/man1/swaymsg.1.gz
%{_mandir}/man1/swaynag.1.gz
%{_mandir}/man5/sway-bar.5.gz
%{_mandir}/man5/sway-input.5.gz
%{_mandir}/man5/sway.5.gz
%{_mandir}/man5/swaynag.5.gz
%{_datarootdir}/wayland-sessions/sway.desktop
%{_datarootdir}/zsh/site-functions/_sway
%{_datarootdir}/zsh/site-functions/_swaylock
%{_datarootdir}/zsh/site-functions/_swaymsg

%changelog
* Sun Oct 14 2018 Sergey Korolev <rpm@skarbek.name> - 1.0-0.6.gite6a52ae3
- New release

* Tue Aug 7 2018 Marcin Skarbek <rpm@skarbek.name> - 1.0-0.5.git0cd418b
- New release

* Tue Jul 17 2018 Marcin Skarbek <rpm@skarbek.name> - 1.0-0.4.gitbec982b
- New release

* Wed May 23 2018 Marcin Skarbek <rpm@skarbek.name> - 1.0-0.3.git867fb6a
- New release

* Wed May 23 2018 Marcin Skarbek <rpm@skarbek.name> - 1.0-0.2.git404d006
- Initial package
