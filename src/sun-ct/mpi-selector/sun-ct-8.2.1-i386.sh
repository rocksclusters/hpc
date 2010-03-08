#!/bin/bash
#
# adapted from the centos openmpi rpm for use with mpi-selector

if [ -z "`echo $path | grep /opt/sun-ct/bin`" ]; then
    export path=/opt/sun-ct/bin:$path
fi

if [ -z "`echo $ld_library_path | grep /opt/sun-ct/lib`" ]; then
    if [ -n "$ld_library_path" ]; then
    	export ld_library_path=/opt/sun-ct/lib:$ld_library_path
    else
    	export ld_library_path=/opt/sun-ct/lib
    fi
fi
