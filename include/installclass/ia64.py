# $Id: ia64.py,v 1.19 2012/11/27 00:49:00 phil Exp $
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
# $Log: ia64.py,v $
# Revision 1.19  2012/11/27 00:49:00  phil
# Copyright Storm for Emerald Boa
#
# Revision 1.18  2012/05/06 05:49:09  phil
# Copyright Storm for Mamba
#
# Revision 1.17  2011/07/23 02:31:03  phil
# Viper Copyright
#
# Revision 1.16  2010/09/07 23:53:20  bruno
# star power for gb
#
# Revision 1.15  2009/05/01 19:07:18  mjk
# chimi con queso
#
# Revision 1.14  2008/10/18 00:56:09  mjk
# copyright 5.1
#
# Revision 1.13  2008/03/06 23:41:53  mjk
# copyright storm on
#
# Revision 1.12  2007/06/23 04:03:38  mjk
# mars hill copyright
#
# Revision 1.11  2006/09/11 22:48:46  mjk
# monkey face copyright
#
# Revision 1.10  2006/08/10 00:10:50  mjk
# 4.2 copyright
#
# Revision 1.9  2006/06/05 17:57:39  bruno
# first steps towards 4.2 beta
#
# Revision 1.8  2005/10/12 18:09:40  mjk
# final copyright for 4.1
#
# Revision 1.7  2005/09/16 01:03:17  mjk
# updated copyright
#
# Revision 1.6  2005/05/24 21:22:42  mjk
# update copyright, release is not any closer
#
# Revision 1.5  2005/03/31 22:47:37  fds
# Cleanup duplicate code
#
# Revision 1.4  2004/03/25 03:16:08  bruno
# touch 'em all!
#
# update version numbers to 3.2.0 and update copyrights
#
# Revision 1.3  2003/08/13 17:18:51  bruno
# put in rocks copyright for 3.0.0
#
# Revision 1.2  2003/08/13 15:22:53  bruno
# added public domain dedication
#
# Revision 1.1  2003/07/07 20:47:51  bruno
# initial release
#
# Revision 1.3  2003/05/22 16:36:35  mjk
# copyright
#
# Revision 1.2  2003/04/25 18:15:09  bruno
# first pass at adding all the new rocks config screens
#
# Revision 1.1  2003/04/24 16:59:41  mjk
# - add order tags
# - edge and order tags can have children
# 	This just make the graph look nicer, no functional change
# - added include directory
# - moved install class code into include directory
# - dependecies enforced via topological sort
# - weight attributes are dead
# - long live order tags
# - the 'gen' attribute is currently ignored.  This will be used to support
#   other graph ordering requirements (e.g. testing, cfengine, ...)
#


from kickstart import *
from users import *

class CustomKickstart(RocksCustomKickstart):
	
	def getEFIDiskInfo(self):
		efipartname = ''

		#
		# before we read the partitions, make sure the kernel
		# can see all the partitions on all the drives.
		#
		cmd = '/tmp/updates/rocks/bin/make-bootable-disks ' \
			+ '> /dev/null 2>&1' 
		os.system(cmd)

		#
		# now walk through all the partitions
		#
		file = open('/proc/partitions', 'r')

		basedevname = 'this is the first entry'

		#
		# look for an EFI partition (but need to toss the
		# first two lines)
		#
		lines = file.readlines()
		for line in lines[2:]:
			tokens = string.split(line)

			major = tokens[0]
			minor = tokens[1]
			blocks = tokens[2]
			devname = tokens[3]

			match = string.count(devname, basedevname)

			if match == 0:
				basedevname = devname
			else:
				#
				# make the device node
				#
				devicename = tempfile.mktemp()

				os.system('mknod %s b %s %s' %
					(devicename, major, minor))

				#
				# make the mount point
				#
				mountpoint = tempfile.mktemp()
				os.makedirs(mountpoint)

				#
				# mount the device
				#
				os.system('mount %s %s' \
					% (devicename, mountpoint) + \
						' > /dev/null 2>&1')

				if os.path.exists(mountpoint + '/startup.nsh'):
					#
					# assign the name of the rocks
					# root partition
					#
					efipartname = devname

				os.system('umount %s' % (mountpoint) +
					' > /dev/null 2>&1')
					
				os.removedirs(mountpoint)
				os.unlink(devicename)

		return efipartname

	def diskPartition(self, id):
		self.id = id

		# raise NameError, 'in diskPartition'

		rootpartname, devnames = RocksCustomKickstart.getDiskInfo(self)

		if rootpartname != '':
			#
			# rocks has been installed on this node before.
			# just reinstall the base operating environment,
			# that is, reinstall '/' but leave all the other
			# file systems alone.
			#
			efipartname = self.getEFIDiskInfo()

			args = [ "/boot/efi" , "--size" , "1",
				"--fstype", "vfat", 
				"--onpart", efipartname ]

			#
			# set the values in the installer
			#
			KickstartBase.definePartition(self, id, args)

		else:
			args = [ "/boot/efi" , "--size" , "1000",
				"--fstype", "vfat", 
				"--ondisk", devnames[0] ]

			KickstartBase.definePartition(self, id, args)

		#
		# call the diskPartition from the Rocks class
		#
		RocksCustomKickstart.diskPartition(self, id)


	def __init__(self, file, serial):
		RocksCustomKickstart.__init__(self, file, serial)


