#!/bin/csh
#
# Adapted from the CentOS OpenMPI rpm for use with mpi-selector

if ("" == "`echo $path | grep /opt/openmpi/bin`") then
	set path=(/opt/openmpi/bin $path)
endif

if ("1" == "$?LD_LIBRARY_PATH") then
	if ("$LD_LIBRARY_PATH" !~ */opt/openmpi/lib*) then
		setenv LD_LIBRARY_PATH /opt/openmpi/lib:$LD_LIBRARY_PATH
	endif
else
	setenv LD_LIBRARY_PATH /opt/openmpi/lib
endif
