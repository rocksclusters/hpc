#
# $Id: Makefile,v 1.19 2012/11/27 00:49:01 phil Exp $
#
# @Copyright@
# 
# 				Rocks(r)
# 		         www.rocksclusters.org
# 		         version 6.2 (SideWinder)
# 		         version 7.0 (Manzanita)
# 
# Copyright (c) 2000 - 2017 The Regents of the University of California.
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
# $Log: Makefile,v $
# Revision 1.19  2012/11/27 00:49:01  phil
# Copyright Storm for Emerald Boa
#
# Revision 1.18  2012/05/06 05:49:10  phil
# Copyright Storm for Mamba
#
# Revision 1.17  2012/05/06 01:11:06  phil
# Add default module definition for rocks-openmpi.
#
# Revision 1.16  2011/07/23 02:31:06  phil
# Viper Copyright
#
# Revision 1.15  2010/09/07 23:53:21  bruno
# star power for gb
#
# Revision 1.14  2009/05/04 17:56:00  phil
# Update to streams 5.9. Supports OpenMP Threads
#
# Revision 1.13  2009/05/01 19:07:18  mjk
# chimi con queso
#
# Revision 1.12  2008/10/18 00:56:10  mjk
# copyright 5.1
#
# Revision 1.11  2008/10/15 20:13:05  mjk
# - more changes to build outside of the tree
# - removed some old fds-only targets
#
# Revision 1.10  2008/05/21 17:46:56  anoop
# Merginig code from mercurial.
# This change makes the HPC roll more solaris friendly
#
# Revision 1.9  2008/03/06 23:41:54  mjk
# copyright storm on
#
# Revision 1.8  2007/06/23 04:03:41  mjk
# mars hill copyright
#
# Revision 1.7  2007/01/17 15:19:49  bruno
# nuked spec file for stream
#
#


RPM.EXTRAS=%define __os_install_post /usr/lib/rpm/brp-compress
REDHAT.ROOT     = $(CURDIR)/../../
-include $(ROCKSROOT)/etc/Rules.mk
include Rules.mk
-include $(OS).mk

SUPPORTFILES = READ.ME HISTORY.txt LICENSE.txt ROCKS.txt
CODEFILES = stream.c stream.f mysecond.c Makefile linux.mk sunos.mk version.mk

build: stream stream_f

stream: stream.o
	$(CC) $(CFLAGS) -o $@ $^

stream.o: stream.c
	$(CC) $(CFLAGS) -c -DN=$(MEMSIZE) -o$@ $^

stream_f: stream.f mysecond.o
	$(CC) $(CFLAGS) -c mysecond.c
	$(FORTRAN) $(FFLAGS) -c stream.f -o stream_f.o
	$(FORTRAN) stream_f.o mysecond.o -o stream_f

	
install::
	mkdir -p $(ROOT)/$(PKGROOT)/bin
	$(INSTALL) -m555 stream stream_f $(ROOT)/$(PKGROOT)/bin
	mkdir -p $(ROOT)/$(PKGROOT)/docs
	$(INSTALL) -m644 $(SUPPORTFILES) $(CODEFILES) $(ROOT)/$(PKGROOT)/docs


clean::
	$(RM) -f *.o
	$(RM) -f stream stream_f
	$(RM) -f $(NAME).spec.in

