# $Id: Makefile,v 1.19 2008/10/18 00:56:09 mjk Exp $
#
# @Copyright@
# 
# 				Rocks(r)
# 		         www.rocksclusters.org
# 		           version 5.1  (VI)
# 
# Copyright (c) 2000 - 2008 The Regents of the University of California.
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
# Revision 1.19  2008/10/18 00:56:09  mjk
# copyright 5.1
#
# Revision 1.18  2008/10/15 20:13:04  mjk
# - more changes to build outside of the tree
# - removed some old fds-only targets
#
# Revision 1.17  2008/05/21 17:46:55  anoop
# Merginig code from mercurial.
# This change makes the HPC roll more solaris friendly
#
# Revision 1.16  2008/03/06 23:41:53  mjk
# copyright storm on
#
# Revision 1.15  2008/03/03 18:21:30  bruno
# no more lam
#
# Revision 1.14  2007/12/03 22:34:48  bruno
# don't build lam
#
# Revision 1.13  2007/08/14 20:28:40  anoop
# Makefiles fitted so that compilation occurs without errors
# on Solaris
#
# Revision 1.12  2007/06/23 04:03:38  mjk
# mars hill copyright
#
# Revision 1.11  2006/12/05 14:50:55  bruno
# added 'pkg'
#
# Revision 1.10  2006/09/11 22:48:46  mjk
# monkey face copyright
#
# Revision 1.9  2006/08/10 00:10:51  mjk
# 4.2 copyright
#
# Revision 1.8  2005/10/12 18:09:40  mjk
# final copyright for 4.1
#
# Revision 1.7  2005/09/16 01:03:17  mjk
# updated copyright
#
# Revision 1.6  2005/06/16 00:26:37  bruno
# make sure atlas is built everytime.
#
# Revision 1.5  2005/05/24 21:22:42  mjk
# update copyright, release is not any closer
#
# Revision 1.4  2005/03/12 00:01:58  bruno
# minor checkin
#
# Revision 1.3  2005/03/08 00:59:09  fds
# Works with empty src directories.
#
# Revision 1.2  2004/03/25 03:16:09  bruno
# touch 'em all!
#
# update version numbers to 3.2.0 and update copyrights
#
# Revision 1.1  2004/02/09 06:10:05  bruno
# new version of mpich
#
# Revision 1.2  2004/01/09 19:55:36  bruno
# added mpd to intel roll
#
# restructured the way in which mpich is built for the various packages
# in order to leverage code reuse
#
# Revision 1.1  2003/12/17 23:17:56  bruno
# new intel rpms (version 8 of the compiler) and config
#
# Revision 1.2  2003/08/27 23:10:55  mjk
# - copyright update
# - rocks-dist uses getArch() fix the i686 distro bug
# - ganglia-python spec file fixes (bad service start code)
# - found some 80col issues while reading code
# - WAN ks support starting
#
# Revision 1.1  2003/07/30 22:24:25  mjk
# *** empty log message ***
#

-include $(shell $(ROCKSROOT)/bin/os).mk

default:	rpm

copyright rpm pkg clean::
	for i in $(SRCDIRS) ; do \
		if [ -f $$i/Makefile ]; then \
			(cd $$i; $(MAKE) $@) ; \
		fi ; \
	done

