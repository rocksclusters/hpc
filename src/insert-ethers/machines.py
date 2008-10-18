#
# Skeleton insert-ethers plugin module
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
# $Log: machines.py,v $
# Revision 1.3  2008/10/18 00:56:09  mjk
# copyright 5.1
#
# Revision 1.2  2008/03/06 23:41:53  mjk
# copyright storm on
#
# Revision 1.1  2008/02/07 20:31:13  bruno
# moved an HPC-specific insert-ethers plugin into the HPC roll
#
# Revision 1.8  2007/06/23 04:03:26  mjk
# mars hill copyright
#
# Revision 1.7  2006/09/15 02:38:21  mjk
# removed ROCK_ROOT variable, #80 (trac.rocksclusters.org)
#
# Revision 1.6  2006/09/11 22:47:30  mjk
# monkey face copyright
#
# Revision 1.5  2006/08/10 00:09:46  mjk
# 4.2 copyright
#
# Revision 1.4  2005/10/12 18:08:47  mjk
# final copyright for 4.1
#
# Revision 1.3  2005/09/16 01:02:26  mjk
# updated copyright
#
# Revision 1.2  2005/05/24 21:22:01  mjk
# update copyright, release is not any closer
#
# Revision 1.1  2005/03/14 20:25:18  fds
# Plugin architecture: service control is modular. Rolls can add hooks without
# touching insert-ethers itself. Plugins can be ordered relative to each other by
# filename.
#
#

import rocks.sql
import os
from syslog import syslog

class Plugin(rocks.sql.InsertEthersPlugin):
	"Make the MPICH machines file"

	def update(self):
		self.regenerate()

	def done(self):
		self.regenerate()

	def regenerate(self):
		cmd = 'find /opt/mpich -name "*LINUX"'
		for line in os.popen(cmd).readlines():
			i = line[:-1]
			if os.path.exists(i):
				os.system('/opt/rocks/bin/dbreport machines '+
					  ' > %s 2> /dev/null' % (i))

