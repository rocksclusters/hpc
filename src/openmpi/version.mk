NAME		= rocks-openmpi
VERSION		= 1.10.0
RELEASE		= 1

TARBALL-EXTENSION = tar.gz
#### if a bzip2 file
## TARBALL-EXTENSION = tar.bz2

ifneq (,$(findstring bz2, $(TARBALL-EXTENSION)))
CAT-COMPRESS = bzcat
else
CAT-COMPRESS = zcat
endif
