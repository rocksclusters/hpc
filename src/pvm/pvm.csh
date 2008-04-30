## Set up PVM ROOT, ARCH and add to PATH
setenv PVM_ROOT /usr/share/pvm3
setenv PVM_ARCH `$PVM_ROOT/lib/pvmgetarch`
set path=($path $PVM_ROOT/bin/$PVM_ARCH)
