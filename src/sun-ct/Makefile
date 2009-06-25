# $Id: Makefile,v 1.1 2009/06/25 23:40:25 anoop Exp $

# @Copyright@
# @Copyright@

# $Log: Makefile,v $
# Revision 1.1  2009/06/25 23:40:25  anoop
# Added Sun HPC Cluster tools 8.2 to the CVS tree
#

REDHAT.ROOT = $(CURDIR)/../../
-include $(ROCKSROOT)/etc/Rules.mk
include Rules.mk
PKGROOT = /opt/SUNWhpc/HPC$(VERSION)

build:
	gunzip -c $(ARCHIVENAME)-$(VERSION)-$(RELEASE_NAME).tar.gz | $(TAR) -xf -
	gunzip -c $(ARCHIVENAME)-$(VERSION)-docs.tar.gz | $(TAR) -xf -

install::
	mkdir -p $(ROOT)/$(PKGROOT)/$(SHAREDIR)/
	(\
		cd $(ARCHIVENAME)-$(VERSION)-$(RELEASE_NAME);	\
		find src | cpio -pudv $(ROOT)/$(PKGROOT)/$(SHAREDIR)/ ; \
	)
	(\
		cd $(ARCHIVENAME)-$(VERSION)-docs; \
		find . -type f | cpio -pudv $(ROOT)/$(PKGROOT)/$(SHAREDIR)/ ; \
	)
	chown -R 0:0 $(ROOT)/$(PKGROOT)/$(SHAREDIR)/
	
clean::
	rm -rf $(ARCHIVENAME)-$(VERSION)-$(RELEASE_NAME)
	rm -rf $(ARCHIVENAME)-$(VERSION)-docs
