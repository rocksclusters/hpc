NAME		= rocks-openmpi
VERSION		= 2.1.1
RELEASE		= 1
PKGROOT		= /opt/openmpi

TARBALL-EXTENSION = tar.gz
#### if a bzip2 file
## TARBALL-EXTENSION = tar.bz2

ifneq (,$(findstring bz2, $(TARBALL-EXTENSION)))
CAT-COMPRESS = bzcat
else
CAT-COMPRESS = zcat
endif
RPM.FILES = $(PKGROOT) 
