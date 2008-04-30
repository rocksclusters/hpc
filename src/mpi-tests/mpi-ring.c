#include <stdio.h>
#include <stdlib.h>
#include "mpi.h"


int
main(int argc, char *argv[])
{
	MPI_Request	sendreq;
	MPI_Request	recvreq;
	MPI_Status	status;
	int		numprocs;
	int		myid;
	int		namelen;
	int		left, right;
	int		bufsize;
	char		processor_name[MPI_MAX_PROCESSOR_NAME];
	char		*sendbuf, *recvbuf;

	MPI_Init(&argc, &argv);
	MPI_Comm_size(MPI_COMM_WORLD, &numprocs);
	MPI_Comm_rank(MPI_COMM_WORLD, &myid);
	MPI_Get_processor_name(processor_name, &namelen);

	fprintf(stderr,"Process %d on %s\n", myid, processor_name);

	right = (myid + 1) % numprocs;
	if (myid == 0) {
		left = numprocs - 1;
	} else {
		left = (myid - 1) % numprocs;
	}

	if (argc == 2) {
		bufsize = atoi(argv[1]);
	} else {
		bufsize = 1024 * 1024;
	}

	if ((sendbuf = (char *)malloc(bufsize)) == NULL) {
		fprintf(stderr,"Process %d on %s:malloc failed\n",
			myid, processor_name);

		MPI_Finalize();
		exit(-1);
	}

	if ((recvbuf = (char *)malloc(bufsize)) == NULL) {
		fprintf(stderr,"Process %d on %s:malloc failed\n",
			myid, processor_name);

		MPI_Finalize();
		exit(-1);
	}

	if (MPI_Isend(sendbuf, bufsize, MPI_CHAR, right, 1,
			MPI_COMM_WORLD, &sendreq) != MPI_SUCCESS) {

		fprintf(stderr,"Process %d on %s:MPI_Isend failed\n",
			myid, processor_name);

		MPI_Finalize();
		exit(-1);
	}

	if (MPI_Irecv(recvbuf, bufsize, MPI_CHAR, left, 1,
			MPI_COMM_WORLD, &recvreq) != MPI_SUCCESS) {

		fprintf(stderr,"Process %d on %s:MPI_Irecv failed\n",
			myid, processor_name);

		MPI_Finalize();
		exit(-1);
	}

	if (MPI_Wait(&sendreq, &status) != MPI_SUCCESS) {
		fprintf(stderr,"Process %d on %s:MPI_Wait failed:sendreq\n",
			myid, processor_name);

		MPI_Finalize();
		exit(-1);
	}

	fprintf(stderr,
		"Process %d on %s:successfully sent (%d) bytes to id (%d)\n",
			myid, processor_name, bufsize, right);

	if (MPI_Wait(&recvreq, &status) != MPI_SUCCESS) {
		fprintf(stderr,"Process %d on %s:MPI_Wait failed:sendreq\n",
			myid, processor_name);

		MPI_Finalize();
		exit(-1);
	}

	fprintf(stderr,
		"Process %d on %s:successfully received (%d) bytes from id (%d)\n",
			myid, processor_name, bufsize, left);

	MPI_Barrier(MPI_COMM_WORLD);

	MPI_Finalize();
}
