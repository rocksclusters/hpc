RELEASE=SunOS-i386
RELEASE_NAME=$(RELEASE)
SHAREDIR = sun/share

install::
	if [ ! -d $(REDHAT.ROOT)/PKGS/ ]; then mkdir -p $(REDHAT.ROOT)/PKGS/; fi
	pkgtrans $(ARCHIVENAME)-$(VERSION)-$(RELEASE)/Product $(REDHAT.ROOT)/PKGS/ all
