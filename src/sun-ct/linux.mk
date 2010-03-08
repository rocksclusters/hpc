RELEASE=1
RELEASE_NAME=Linux-gnu
SHAREDIR=gnu/share

install::
	if [ ! -d $(REDHAT.ROOT)/RPMS/$(ARCH)/ ]; then \
		mkdir -p $(REDHAT.ROOT)/RPMS/$(ARCH)/; fi
	find $(ARCHIVENAME)-$(VERSION)-$(RELEASE_NAME)/Product/ \
		-type f -name ClusterTools_gnu-$(VERSION)\*.$(ARCH).rpm \
		-exec cp -rf {} $(REDHAT.ROOT)/RPMS/$(ARCH) \;
	( find mpi-selector -type f | grep -v CVS | \
		cpio -pudv $(ROOT)/$(PKGROOT)/$(SHAREDIR) )
