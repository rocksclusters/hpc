RELEASE=SunOS-i386
RELEASE_NAME=$(RELEASE)
SHAREDIR = sun/share

bootstrap:
	gunzip -c $(ARCHIVENAME)-$(VERSION)-$(RELEASE_NAME).tar.gz | $(TAR) -xf -
	( for i in `find $(ARCHIVENAME)-$(VERSION)-$(RELEASE)/Product \
			-type f -name pkgmap`; \
		do						\
		cat $$i | sed 's/hpcgroup/bin/g' > $${i}.new;	\
		mv $${i}.new $$i;				\
		done;						\
	)
	(cd $(ARCHIVENAME)-$(VERSION)-$(RELEASE)/Product/Install_Utilities/bin \
		&& ./ctinstall -l)

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
