Summary:	Metapackage for Plasma 6
Name:		task-plasma6
Version:	6.0.0
Release:	0.20230726.0
License:	GPLv2+
Group:		Graphical desktop/KDE
Requires:	task-plasma6-minimal = %{EVRD}
#Requires:	distro-plasma-config
Requires:	openmandriva-kde-icons
Requires:	plasma6-bluedevil
Requires:	plasma6-drkonqi
# (crazy) FIXME: need -wayland task
Requires:	plasma6-kwayland-integration
Requires:	plasma6-kwin-wayland
Requires:	plasma6-workspace-wayland
Requires:	plasma6-sddm
Requires:	plasma6-sddm-kcm
Requires:	plasma6-sddm-theme-breeze
Requires:	plasma6-discover
Requires:	plasma6-discover-notifier
Requires:	plasma6-discover-backend-packagekit
Requires:	plasma6-kde-gtk-config
Requires:	plasma6-firewall
Requires:	plasma6-systemmonitor
Suggests:	xscreensaver

%description
This package is a meta-package, meaning that its purpose is to contain
the complete dependencies for running the Plasma 6 desktop.

%files

%package minimal
Summary:	Minimal dependencies needed for Plasma 6
Group:		Graphical desktop/KDE
# Basic
Requires:	plasma6-kwin-wayland
Requires:	plasma6-workspace-wayland
Requires:	task-x11
Requires:	plasma6-kwin-x11
Requires:	plasma6-workspace-x11
Requires:	xsettingsd
Conflicts:	xsettings-kde
Requires:	plasma6-konsole
Requires:	plasma6-breeze
Requires:	kf6-breeze-icons
Requires:	plasma6-oxygen-sounds
Requires:	kf6-frameworkintegration
Requires:	plasma6-kde-cli-tools
Requires:	kf6-kded
Requires:	kf6-kdeclarative
Requires:	plasma6-milou
Requires:	kf6-baloo
Requires:	plasma6-pa
Requires:	plasma6-integration
Requires:	plasma6-desktop
Requires:	plasma6-vault
Requires:	plasma6-browser-integration
Requires:	plasma6-workspace
Requires:	plasma6-kdeplasma-addons
Requires:	plasma6-kinfocenter
Requires:	plasma6-kmenuedit
Requires:	plasma6-kscreen
Requires:	plasma6-kscreenlocker
Requires:	kf6-kservice
Requires:	plasma6-ksshaskpass
Requires:	plasma6-kwrited
Requires:	phonon4qt6-backend
Requires:	plasma6-nm
Requires:	plasma6-powerdevil
Requires:	kf6-solid
Requires:	plasma6-polkit-kde-agent-1
Requires:	plasma6-xdg-desktop-portal-kde
Suggests:	task-pulseaudio

%description minimal
This package is a meta-package, meaning that its purpose is to contain
minimal dependencies for running a minimal Plama 6 desktop environment.

%files minimal

#----------------------------------------------------------------------------

%package mobile-minimal
Summary:	Minimal set of packages for Plasma Mobile
Group:		Graphical desktop/KDE
# Basic
Requires:	pinentry-qt5
Requires:	libproxy-kde
Requires:	libproxy-networkmanager
# Plasma 6
Requires:	plasma6-breeze
Requires:	kf6-breeze-icons
Requires:	plasma6-oxygen-sounds
Requires:	kf6-frameworkintegration
Requires:	plasma6-kde-cli-tools
Requires:	kf6-kded
Requires:	kf6-kdeclarative
Requires:	plasma6-pa
Requires:	plasma6-integration
Requires:	plasma6-desktop
Requires:	plasma6-vault
Requires:	plasma6-browser-integration
Requires:	plasma6-workspace
# FIXME This should really be "Requires:", but as of
# 5.20.4, kscreenlocker on Plasma Mobile fails to unlock
# even if the password is supplied correctly.
# In the mean time, Plasma Mobile without lock screen is
# usable, so let's not block further testing on this...
#Conflicts:	kscreenlocker
Requires:	plasma6-ksshaskpass
Requires:	phonon4qt6-backend
Requires:	plasma6-nm
Requires:	plasma6-powerdevil
Requires:	kf6-solid
Requires:	plasma6-polkit-kde-agent-1
Requires:	plasma6-xdg-desktop-portal-kde
Requires:	plasma6-milou

# FIXME at some point, we probably want to support plasma-mobile on X11
# as well...
Requires:	plasma6-kwin-wayland

# Key Plasma Mobile specific bits (stuff that is either
# required or active in the default config)
Requires:	plasma6-mobile
Suggests:	task-pulseaudio

%description mobile-minimal
This package is a meta-package, meaning that its purpose is to contain
a minimal version of the mobile version of the Plama 5 desktop environment.


%files mobile-minimal
#----------------------------------------------------------------------------

%package mobile
Summary:	Packages for Plasma Mobile
Group:		Graphical desktop/KDE
# Basic
Requires:	%{name}-mobile-minimal = %{EVRD}
Requires:	plasma6-discover
Requires:	plasma6-discover-backend-packagekit
Requires:	plasma6-kscreen
Requires:	plasma6-pa

%description mobile
This package is a meta-package, meaning that its purpose is to contain
the mobile version of the Plasma 6 desktop environment.

%files mobile
#----------------------------------------------------------------------------

%prep

%build

%install
