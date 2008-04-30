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
