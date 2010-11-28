#
# $Id: Makefile,v 1.22 2010/11/28 00:40:34 anoop Exp $
#
# @Copyright@
# 
# 				Rocks(r)
# 		         www.rocksclusters.org
# 		         version 5.4 (Maverick)
# 
# Copyright (c) 2000 - 2010 The Regents of the University of California.
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
# Revision 1.22  2010/11/28 00:40:34  anoop
# Solaris 64-bit support for iozone
#
# Revision 1.21  2010/09/07 23:53:20  bruno
# star power for gb
#
# Revision 1.20  2009/11/25 18:51:02  anoop
# Upgraded iozone
#
# Revision 1.19  2009/10/07 17:10:22  bruno
# workaround for a bad checkin
#
# Revision 1.18  2009/10/01 21:07:56  bruno
# refresh for 5.3
#
# Revision 1.17  2009/05/01 19:07:18  mjk
# chimi con queso
#
# Revision 1.16  2008/10/18 00:56:09  mjk
# copyright 5.1
#
# Revision 1.15  2008/10/15 20:13:04  mjk
# - more changes to build outside of the tree
# - removed some old fds-only targets
#
# Revision 1.14  2008/05/21 17:46:55  anoop
# Merginig code from mercurial.
# This change makes the HPC roll more solaris friendly
#
# Revision 1.13  2008/03/06 23:41:53  mjk
# copyright storm on
#
# Revision 1.12  2007/06/23 04:03:39  mjk
# mars hill copyright
#
# Revision 1.11  2006/09/11 22:48:51  mjk
# monkey face copyright
#
# Revision 1.10  2006/08/10 00:10:56  mjk
# 4.2 copyright
#
# Revision 1.9  2006/07/01 16:56:46  bruno
# refreshed iozone and converted the build procedure from SRPM-based to
# tarball-based.
#
#

PKGROOT		= /opt/iozone
REDHAT.ROOT     = $(CURDIR)/../../

-include $(ROCKSROOT)/etc/Rules.mk
include Rules.mk

BINARIES	= iozone fileop Generate_Graphs gengnuplot.sh gnu3d.dem
DOCS		= IOzone_msword_98.pdf Run_rules.doc IOzone_msword_98.doc \
			Iozone_ps.gz 


build:
	$(TAR) xf $(NAME)$(IOZONE_VERSION).tar
	-(cd patch-files && \
		find $(NAME)$(IOZONE_VERSION) -type f | \
		grep -v CVS | cpio -pudv ../;		\
	)
	(								\
		cd $(NAME)$(IOZONE_VERSION)/src/current;		\
		$(MAKE) $(TARGET);					\
	)

install::
	mkdir -p $(ROOT)/$(PKGROOT)/bin
	(								\
		cd $(NAME)$(IOZONE_VERSION)/src/current;		\
		cp $(BINARIES) $(ROOT)/$(PKGROOT)/bin;			\
	)
	mkdir -p $(ROOT)/$(PKGROOT)/docs
	(								\
		cd $(NAME)$(IOZONE_VERSION)/docs;			\
		cp $(DOCS) $(ROOT)/$(PKGROOT)/docs;			\
	)
	(								\
		cd $(NAME)$(IOZONE_VERSION)/src/current;		\
		cp Gnuplot.txt $(ROOT)/$(PKGROOT)/docs;			\
	)


clean::
	rm -rf $(NAME)$(IOZONE_VERSION)
	rm -f $(NAME).spec.in

