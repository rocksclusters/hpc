# Generated automatically from Makefile.in by configure.
##### User configurable options #####
# This is an example Makefile.in (or Makefile configured with mpireconfig)
# for the programs cpi, pi3, and cpilog.  

CC		= $(MPIDIR)/bin/mpicc
CCC		= $(MPIDIR)/bin/mpiCC
F77		= $(MPIDIR)/bin/mpif77
CLINKER		= $(MPIDIR)/bin/mpicc
CCLINKER	= $(MPIDIR)/bin/mpiCC
FLINKER		= $(MPIDIR)/bin/mpif77
F90		= 
F90LINKER	= 	  
MAKE		+= --no-print-directory
SHELL		= /bin/sh
#

### End User configurable options ###

LIBS =
FLIBS =
EXECS = mpi-cleanup

default: $(EXECS)

install: $(EXECS)
	-mkdir $(MPIDIR)/bin
	cp mpirun $(MPIDIR)/bin/mpirun.rocks

	mkdir $(MPIDIR)/clean
	cp mpi-cleanup $(MPIDIR)/clean
	cp cleanipcs $(MPIDIR)/clean


mpi-cleanup: mpi-cleanup.o 
	$(CLINKER) -o mpi-cleanup mpi-cleanup.o -lm

clean:
	-/bin/rm -f *.o mpi-cleanup

.c.o:
	$(CC) -D CLEANIPCS="\"$(MPIDIR)/clean/cleanipcs\"" $(CFLAGS) -c $<

