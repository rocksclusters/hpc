# $Id: mpi-verify.c,v 1.2 2009/01/26 22:26:50 mjk Exp $
#
# @Copyright@
# @Copyright@
#
# $Log: mpi-verify.c,v $
# Revision 1.2  2009/01/26 22:26:50  mjk
# added missing copyright
#

#include <stdio.h>
#include "mpi.h"

int
main(int argc, char *argv[])
{
	int	numprocs;
	int	myid;
	int	namelen;
	char	processor_name[MPI_MAX_PROCESSOR_NAME];

	MPI_Init(&argc,&argv);
	MPI_Comm_size(MPI_COMM_WORLD,&numprocs);
	MPI_Comm_rank(MPI_COMM_WORLD,&myid);
	MPI_Get_processor_name(processor_name,&namelen);

	fprintf(stderr,"Process %d on %s\n", myid, processor_name);

	MPI_Barrier(MPI_COMM_WORLD);

	MPI_Finalize();
}
