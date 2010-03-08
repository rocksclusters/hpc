#!/bin/bash
#
# Adapted from the CentOS OpenMPI rpm for use with mpi-selector

if [ -z "`echo $PATH | grep /opt/openmpi/bin`" ]; then
    export PATH=/opt/openmpi/bin:$PATH
fi

if [ -z "`echo $LD_LIBRARY_PATH | grep /opt/openmpi/lib`" ]; then
    if [ -n "$LD_LIBRARY_PATH" ]; then
    	export LD_LIBRARY_PATH=/opt/openmpi/lib:$LD_LIBRARY_PATH
    else
    	export LD_LIBRARY_PATH=/opt/openmpi/lib
    fi
fi
