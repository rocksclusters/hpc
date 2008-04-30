#
# $Id: Makefile,v 1.11 2008/03/06 23:41:53 mjk Exp $
#
# @Copyright@
# 
# 				Rocks(r)
# 		         www.rocksclusters.org
# 		            version 5.0 (V)
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
# Revision 1.11  2008/03/06 23:41:53  mjk
# copyright storm on
#
# Revision 1.10  2008/03/03 18:49:13  bruno
# added mpich2
#
# Revision 1.9  2007/06/23 04:03:39  mjk
# mars hill copyright
#
# Revision 1.8  2006/09/11 22:48:52  mjk
# monkey face copyright
#
# Revision 1.7  2006/08/10 00:10:57  mjk
# 4.2 copyright
#
# Revision 1.6  2005/10/12 18:09:48  mjk
# final copyright for 4.1
#
# Revision 1.5  2005/09/16 01:03:25  mjk
# updated copyright
#
# Revision 1.4  2005/08/09 17:50:28  mjk
# nuke mpd
#
# Revision 1.3  2005/06/07 01:20:34  najib
# Shared libraries are now enabled and made available.
#
# Revision 1.2  2005/05/24 21:22:50  mjk
# update copyright, release is not any closer
#
# Revision 1.1  2005/02/17 00:29:46  bruno
# mpich is now parameterized for both ethernet and mpd
#
#

MAKE.rpmflag = -bs

REDHAT.ROOT     = $(PWD)/../../
ROCKSROOT       = ../../../../..

-include $(ROCKSROOT)/etc/Rules.mk
include Rules.mk

SRPM = $(NAME)-%{interconnect}-%{compiler}-$(VERSION)-$(RELEASE).src.rpm


rpm::
	rpmbuild --rebuild \
		--define "interconnect ethernet" \
		--define "compiler gnu" \
		--define "use_cc gcc" \
		--define "use_cxx g++" \
		--define "use_fc g77" \
		--define "use_f90 gfortran" \
		--define "mpich_dir /opt/mpich" \
		--define "rsh_command ssh" \
		--define "mpi_install_opts %{nil}" \
		--define "mpich_configure --with-comm=shared \
			--enable-sharedlib \
			--disable-devdebug \
			-opt=-O2 \
			--with-arch=LINUX \
			--with-romio=--enable-aio \
			--enable-f90" \
				$(REDHAT.SRPMS)/$(SRPM)

