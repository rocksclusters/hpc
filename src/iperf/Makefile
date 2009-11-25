# --------------------------------------------------- -*- Makefile -*- --
# $Id: Makefile,v 1.15 2009/11/25 23:20:51 anoop Exp $
#
# @Copyright@
# 
# 				Rocks(r)
# 		         www.rocksclusters.org
# 		       version 5.2 (Chimichanga)
# 
# Copyright (c) 2000 - 2009 The Regents of the University of California.
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
# Revision 1.15  2009/11/25 23:20:51  anoop
# Mods to support sunos patching for iperf
#
# Revision 1.14  2009/05/01 19:07:18  mjk
# chimi con queso
#
# Revision 1.13  2008/10/18 00:56:10  mjk
# copyright 5.1
#
# Revision 1.12  2008/10/15 20:13:04  mjk
# - more changes to build outside of the tree
# - removed some old fds-only targets
#
# Revision 1.11  2008/05/21 17:46:55  anoop
# Merginig code from mercurial.
# This change makes the HPC roll more solaris friendly
#
# Revision 1.10  2008/03/06 23:41:53  mjk
# copyright storm on
#
# Revision 1.9  2008/02/28 17:32:55  bruno
# nuked the spec file for iperf
#
# Revision 1.8  2007/06/23 04:03:39  mjk
# mars hill copyright
#
# Revision 1.7  2006/09/11 22:48:52  mjk
# monkey face copyright
#
# Revision 1.6  2006/08/10 00:10:57  mjk
# 4.2 copyright
#
# Revision 1.5  2005/10/12 18:09:46  mjk
# final copyright for 4.1
#
# Revision 1.4  2005/09/16 01:03:24  mjk
# updated copyright
#
# Revision 1.3  2005/05/24 21:22:49  mjk
# update copyright, release is not any closer
#
# Revision 1.2  2005/03/14 21:31:37  fds
# Fixed subtle name collision during build process.
#
# Revision 1.1  2005/02/17 01:32:02  bruno
# moved iperf source into the hpc roll
#
# Revision 1.3  2003/05/29 02:37:13  bruno
# added iperf 1.7
#
# Revision 1.2  2002/10/07 04:34:46  mjk
# builds under new structure
#
#

REDHAT.ROOT     = $(CURDIR)/../../

-include $(ROCKSROOT)/etc/Rules.mk
include Rules.mk

prep:
	gunzip -c iperf-$(VERSION).tar.gz | $(TAR) -xf -
	-(cd patch-files/iperf-$(VERSION)/$(OS); \
	  find . -type f | grep -v CVS | 	\
	  cpio -pudv ../../../iperf-$(VERSION))


build: prep
	(					\
		cd iperf-$(VERSION) ;		\
		./configure --prefix=$(PKGROOT);\
		$(MAKE) ;			\
	)
install::
	mkdir -p $(ROOT)/$(PKGROOT)
	(							\
		cd iperf-$(VERSION) ;				\
		$(MAKE) prefix=$(ROOT)/$(PKGROOT) install ;	\
	)


clean::
	rm -rf iperf-$(VERSION)
