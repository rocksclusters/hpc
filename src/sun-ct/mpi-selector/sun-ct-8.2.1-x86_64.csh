#!/bin/csh
#
# adapted from the centos openmpi rpm for use with mpi-selector

if ("" == "`echo $path | grep /opt/sun-ct/bin/64`") then
	set path=(/opt/sun-ct/bin/64 $path)
endif

if ("1" == "$?ld_library_path") then
	if ("$ld_library_path" !~ */opt/sun-ct/lib/64*) then
		setenv ld_library_path /opt/sun-ct/lib/64:$ld_library_path
	endif
else
	setenv ld_library_path /opt/sun-ct/lib/64
endif
