#!/bin/sh
#
# This file should remain OS independent
#
# $Id: bootstrap.sh,v 1.17 2012/11/27 19:31:18 phil Exp $
#
# @Copyright@
# 
# 				Rocks(r)
# 		         www.rocksclusters.org
# 		         version 6.2 (SideWinder)
# 
# Copyright (c) 2000 - 2014 The Regents of the University of California.
# All rights reserved.	
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
# 
# 1. Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
# 
# 2. Redistributions in binary form must reproduce the above copyright
# notice unmodified and in its entirety, this list of conditions and the
# following disclaimer in the documentation and/or other materials provided 
# with the distribution.
# 
# 3. All advertising and press materials, printed or electronic, mentioning
# features or use of this software must display the following acknowledgement: 
# 
# 	"This product includes software developed by the Rocks(r)
# 	Cluster Group at the San Diego Supercomputer Center at the
# 	University of California, San Diego and its contributors."
# 
# 4. Except as permitted for the purposes of acknowledgment in paragraph 3,
# neither the name or logo of this software nor the names of its
# authors may be used to endorse or promote products derived from this
# software without specific prior written permission.  The name of the
# software includes the following terms, and any derivatives thereof:
# "Rocks", "Rocks Clusters", and "Avalanche Installer".  For licensing of 
# the associated name, interested parties should contact Technology 
# Transfer & Intellectual Property Services, University of California, 
# San Diego, 9500 Gilman Drive, Mail Code 0910, La Jolla, CA 92093-0910, 
# Ph: (858) 534-5815, FAX: (858) 534-7345, E-MAIL:invent@ucsd.edu
# 
# THIS SOFTWARE IS PROVIDED BY THE REGENTS AND CONTRIBUTORS ``AS IS''
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS
# BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
# BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN
# IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# 
# @Copyright@
#
# $Log: bootstrap.sh,v $
# Revision 1.17  2012/11/27 19:31:18  phil
# compile/install rocks-openmpi, rocks-openmpi-modules so that elements in bio roll will build
#
# Revision 1.16  2012/11/27 00:49:00  phil
# Copyright Storm for Emerald Boa
#
# Revision 1.15  2012/09/30 21:58:55  phil
# Update openmpi to 1.6.2.
# Create Modules for ethernet and IB
# Add IB support - packages, openmpi configuration, udev rules
#
# Revision 1.14  2012/05/06 05:49:09  phil
# Copyright Storm for Mamba
#
# Revision 1.13  2011/07/23 02:31:02  phil
# Viper Copyright
#
# Revision 1.12  2010/09/07 23:53:20  bruno
# star power for gb
#
# Revision 1.11  2009/12/03 22:36:55  bruno
# openmpi directory makes an RPM named rocks-openmpi
#
# Revision 1.10  2009/11/25 23:43:20  anoop
# bootstrapping the HPC roll for sunos
#
# Revision 1.9  2009/05/01 19:07:18  mjk
# chimi con queso
#
# Revision 1.8  2008/10/18 00:56:09  mjk
# copyright 5.1
#
# Revision 1.7  2008/10/15 20:13:04  mjk
# - more changes to build outside of the tree
# - removed some old fds-only targets
#
# Revision 1.6  2008/03/06 23:41:53  mjk
# copyright storm on
#
# Revision 1.5  2007/06/23 04:03:38  mjk
# mars hill copyright
#
# Revision 1.4  2006/09/11 22:48:45  mjk
# monkey face copyright
#
# Revision 1.3  2006/08/10 00:10:50  mjk
# 4.2 copyright
#
# Revision 1.2  2006/07/11 17:52:40  anoop
# Added openmpi
#
# Revision 1.1  2006/07/03 19:56:41  bruno
# bootstrap for hpc roll
#
# Revision 1.5  2006/02/07 22:00:30  mjk
# *** empty log message ***
#
# Revision 1.4  2006/01/19 21:27:11  mjk
# more foundation changes
#
# Revision 1.3  2006/01/18 06:12:41  mjk
# more foundation work
#
# Revision 1.2  2006/01/17 03:45:58  mjk
# might be complete now
#
# Revision 1.1  2006/01/17 00:14:23  mjk
# bootstrap roll development
#

if [ ! -f "$ROLLSROOT/../../bin/get_sources.sh" ]; then
	echo "To compile this roll on Rocks 6.1.1 or older you need to install a newer rocks-devel rpm.
Install it with:
rpm -Uvh https://googledrive.com/host/0B0LD0shfkvCRRGtadUFTQkhoZWs/rocks-devel-6.2-3.x86_64.rpm
If you need an older version of this roll you can get it from:
https://github.com/rocksclusters-attic"
	exit 1
fi

. $ROLLSROOT/etc/bootstrap-functions.sh

if [ `./_os` == "linux" ]; then
	yum -y install libibverbs libusnic_verbs
	install_os_packages hpc-base 
	compile openmpi
	install rocks-openmpi
	compile_and_install rocks-openmpi-modules
fi

if [ `./_os` == "sunos" ]; then
	(cd src/sun-ct && gmake bootstrap)
fi
