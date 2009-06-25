RELEASE=1
RELEASE_NAME=Linux-gnu
SHAREDIR=gnu/share

install::
	if [ ! -d $(REDHAT.ROOT)/RPMS/$(ARCH)/ ]; then \
		mkdir -p $(REDHAT.ROOT)/RPMS/$(ARCH)/; fi
	cp $(ARCHIVENAME)-$(VERSION)-$(RELEASE_NAME)/Product/ClusterTools_gnu-$(VERSION)-09j.$(ARCH).rpm \
		$(REDHAT.ROOT)/RPMS/$(ARCH)/
