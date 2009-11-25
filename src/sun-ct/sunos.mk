RELEASE=SunOS-i386
RELEASE_NAME=$(RELEASE)
SHAREDIR = sun/share

install::
	if [ ! -d $(REDHAT.ROOT)/PKGS/ ]; then mkdir -p $(REDHAT.ROOT)/PKGS/; fi
	# Patch the pkgmap files to use group "bin" and not "hpcgroup"
	( for i in `find $(ARCHIVENAME)-$(VERSION)-$(RELEASE)/Product \
			-type f -name pkgmap`; \
		do						\
		cat $$i | sed 's/hpcgroup/bin/g' > $${i}.new;	\
		mv $${i}.new $$i;				\
		done;						\
	)
	pkgtrans $(ARCHIVENAME)-$(VERSION)-$(RELEASE)/Product $(REDHAT.ROOT)/PKGS/ all
