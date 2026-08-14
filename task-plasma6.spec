Summary:	Metapackage for Plasma 6
Name:		task-plasma6
Version:	6.0.0
Release:	3
License:	GPLv2+
Group:		Graphical desktop/KDE
Requires:	task-plasma6-minimal = %{EVRD}
#Requires:	distro-plasma-config
#Requires:	openmandriva-kde-icons
Requires:	bluedevil
Requires:	drkonqi
Requires:	sddm
Requires:	sddm-kcm
Requires:	sddm-theme-breeze
Requires:	discover
#Requires:	discover-notifier
Requires:	discover-backend-dnf
Requires:	(kde-gtk-config if gtk+-3.0)
#Requires:	plasma-firewall
Requires:	plasma-systemmonitor

%description
This package is a meta-package, meaning that its purpose is to contain
the complete dependencies for running the Plasma 6 desktop.

%files

%package x11
Summary:	X11 window system support for Plasma 6
Group:		Graphical desktop/KDE
Requires:	task-x11
Requires:	plasma6-kwin-x11
Requires:	plasma-workspace-x11
Requires:	kf6-kwindowsystem-backend-x11

%description x11
X11 window system support for Plasma 6

%files x11

%package wayland
Summary:	Wayland window system support for Plasma 6
Group:		Graphical desktop/KDE
Requires:	plasma6-kwin-wayland
Requires:	plasma-workspace-wayland
Requires:	kf6-kwindowsystem-backend-wayland

%description wayland
Wayland window system support for Plasma 6

%files wayland

%package minimal
Summary:	Minimal dependencies needed for Plasma 6
Group:		Graphical desktop/KDE
# Basic
Requires:	xsettingsd
Conflicts:	xsettings-kde
Requires:	konsole
Requires:	breeze
Requires:	kf6-breeze-icons
Requires:	oxygen-sounds
Requires:	kf6-frameworkintegration
Requires:	kde-cli-tools
Requires:	kf6-kded
Requires:	kf6-kdeclarative
Requires:	milou
Requires:	kf6-baloo
Requires:	plasma-pa
Requires:	integration
Requires:	plasma-desktop
Requires:	plasma-vault
Requires:	plasma-browser-integration
Requires:	plasma-workspace
Requires:	kcolorchooser
Requires:	kdeplasma-addons
Requires:	kinfocenter
Requires:	kmenuedit
Requires:	kscreen
Requires:	kscreenlocker
Requires:	kf6-kservice
Requires:	ksshaskpass
Requires:	kwrited
Requires:	phonon4qt6-backend
Requires:	plasma-nm
Requires:	powerdevil
Requires:	kf6-solid
Requires:	polkit-kde-agent-1
Requires:	xdg-desktop-portal-kde
Suggests:	task-pulseaudio
Requires:	distro-release-desktop-Plasma6
Requires:	kwin-aurorae

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
Requires:	breeze
Requires:	kf6-breeze-icons
Requires:	oxygen-sounds
Requires:	kf6-frameworkintegration
Requires:	kde-cli-tools
Requires:	kf6-kded
Requires:	kf6-kdeclarative
Requires:	plasma-pa
Requires:	plasma-integration
Requires:	plasma-desktop
Requires:	plasma-vault
Requires:	plasma-browser-integration
Requires:	plasma-workspace
# FIXME This should really be "Requires:", but as of
# 5.20.4, kscreenlocker on Plasma Mobile fails to unlock
# even if the password is supplied correctly.
# In the mean time, Plasma Mobile without lock screen is
# usable, so let's not block further testing on this...
#Conflicts:	kscreenlocker
Requires:	ksshaskpass
Requires:	phonon4qt6-backend
Requires:	plasma-nm
Requires:	powerdevil
Requires:	kf6-solid
Requires:	polkit-kde-agent-1
Requires:	xdg-desktop-portal-kde
Requires:	milou

# FIXME at some point, we probably want to support plasma-mobile on X11
# as well...
Requires:	plasma6-kwin-wayland

# Key Plasma Mobile specific bits (stuff that is either
# required or active in the default config)
Requires:	plasma-mobile
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
Requires:	discover
Requires:	discover-backend-dnf
Requires:	kscreen
Requires:	plasma-pa

%description mobile
This package is a meta-package, meaning that its purpose is to contain
the mobile version of the Plasma 6 desktop environment.

%files mobile
#----------------------------------------------------------------------------

%prep

%build

%install
