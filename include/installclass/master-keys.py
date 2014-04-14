#
# Get master crypto certificates. For frontends.
#
# @Copyright@
# 
# 				Rocks(r)
# 		         www.rocksclusters.org
# 		       version 6.1.1 (Sand Boa)
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
# $Log: master-keys.py,v $
# Revision 1.16  2012/11/27 00:49:00  phil
# Copyright Storm for Emerald Boa
#
# Revision 1.15  2012/05/06 05:49:09  phil
# Copyright Storm for Mamba
#
# Revision 1.14  2011/07/23 02:31:05  phil
# Viper Copyright
#
# Revision 1.13  2010/09/07 23:53:20  bruno
# star power for gb
#
# Revision 1.12  2009/05/01 19:07:18  mjk
# chimi con queso
#
# Revision 1.11  2008/10/18 00:56:09  mjk
# copyright 5.1
#
# Revision 1.10  2008/03/06 23:41:53  mjk
# copyright storm on
#
# Revision 1.9  2007/06/23 04:03:38  mjk
# mars hill copyright
#
# Revision 1.8  2006/09/11 22:48:46  mjk
# monkey face copyright
#
# Revision 1.7  2006/08/10 00:10:50  mjk
# 4.2 copyright
#
# Revision 1.6  2005/10/12 18:09:40  mjk
# final copyright for 4.1
#
# Revision 1.5  2005/09/16 01:03:17  mjk
# updated copyright
#
# Revision 1.4  2005/05/24 21:22:42  mjk
# update copyright, release is not any closer
#
# Revision 1.3  2005/04/18 23:22:33  fds
# Save important files before drives get nuked.
#
# Revision 1.2  2005/04/14 00:22:22  fds
# Simpler master key management: on catastrophic recovery, we manually
# move CA and 411 keys. Makes USB security key operation more intuitive.
#
# Revision 1.1  2005/04/12 01:56:15  fds
# Moved certificate management earlier in the install process.
#
#

def getRocksFrontendCerts():
	"""Saves Grandfathered master keys and certs on old disks or 
	USB keys. Keys on USB drive take priority. May already be there
	from frontend kickstart file (<pre> section)."""

	# 
	# Only proceed if we are on a frontend.
	#
	if not os.path.exists('/tmp/asked-for-rolls'):
		return
		
	partition = RocksPartition(0, 0, '', '',
		'/mnt/runtime/usr/sbin/e2label',
		'/tmp/etc/fstab')

	# Do not automatically copy master keys from the USB drive. If disaster
	# recovery is needed, move them by hand to the appropriate locations.

	# Master keys on disk from our previous installation
	keys = [('/etc/411-security/shared.key','/tmp/security/411-shared.key'),
		('/etc/411-security/master.key','/tmp/security/411-master.key'),
		('/etc/security/ca/ca.key','/tmp/security/ca.key'),
		('/etc/security/ca/ca.crt','/tmp/security/ca.crt'),
		('/etc/security/ca/ca.serial','/tmp/security/ca.serial')
		]

	for src, dst in keys:
		partition.saveFile(src, dst)

	log("ROCKS:Frontend saved keys")

