SRCDIRS = iozone iperf mpi-tests \
	  stream sun-ct
pkg::
	if [ -d sun-ct ]; then	\
		(cd sun-ct; hg pull; hg update); \
	else \
		hg clone ssh://hg@aurora.rocksclusters.org/sun-utils/sun-ct;\
	fi

.PHONY: sun-ct
clean:: sun-ct
	-(cd sun-ct; gmake clean)

