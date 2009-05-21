SRCDIRS = iozone iperf mpi-tests \
	  stream

HG_SOURCE = ssh://hg@rocks-168.sdsc.edu/sun-utils
HG_PACKAGE= sun-ct

$(HG_PACKAGE)::
	-if [ -d $@ ]; then	\
		(cd $@;\
		hg pull $(HG_SOURCE)/$@ ; \
		hg update;		\
	); \
	else \
		hg clone $(HG_SOURCE)/$@;\
	fi

pkg:: $(HG_PACKAGE)

pkg clean::
PKG_EXISTS = $(shell [ -d $(dir) ] && echo $(dir))
SRCDIRS += $(foreach dir, $(HG_PACKAGE), $(PKG_EXISTS))
