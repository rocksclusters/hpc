## Set up PVM ROOT, ARCH and add to PATH
export PVM_ROOT=/usr/share/pvm3
export PVM_ARCH=`$PVM_ROOT/lib/pvmgetarch`
export PATH=$PATH:$PVM_ROOT/bin/$PVM_ARCH
