# $Id: frontend.py,v 1.91 2012/11/27 00:49:00 phil Exp $
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
# $Log: frontend.py,v $
# Revision 1.91  2012/11/27 00:49:00  phil
# Copyright Storm for Emerald Boa
#
# Revision 1.90  2012/05/06 05:49:09  phil
# Copyright Storm for Mamba
#
# Revision 1.89  2011/07/23 02:31:03  phil
# Viper Copyright
#
# Revision 1.88  2010/09/07 23:53:20  bruno
# star power for gb
#
# Revision 1.87  2009/05/01 19:07:18  mjk
# chimi con queso
#
# Revision 1.86  2008/10/18 00:56:09  mjk
# copyright 5.1
#
# Revision 1.85  2008/03/06 23:41:53  mjk
# copyright storm on
#
# Revision 1.84  2007/06/23 04:03:38  mjk
# mars hill copyright
#
# Revision 1.83  2006/09/11 22:48:46  mjk
# monkey face copyright
#
# Revision 1.82  2006/08/10 00:10:50  mjk
# 4.2 copyright
#
# Revision 1.81  2006/07/07 20:06:08  bruno
# cleanup
#
# Revision 1.80  2006/07/06 23:53:19  bruno
# stripped out old upgrade procedure
#
# Revision 1.79  2006/06/05 17:57:38  bruno
# first steps towards 4.2 beta
#
# Revision 1.78  2006/01/18 21:17:50  yuchan
# add code _ and rhpl.translate for supporting localization - yuchan
#
# Revision 1.77  2005/12/15 19:33:08  bruno
# move the file preservation from the installclass to the 'restore' roll
#
# Revision 1.76  2005/10/12 18:09:40  mjk
# final copyright for 4.1
#
# Revision 1.75  2005/10/06 22:24:31  bruno
# make sure the installer doesn't crash on a frontend upgrade when the
# /tmp/clusterold.sql file doesn't exist.
#
# this can happen when upgrading from a x86_64 release to a i386 release.
# the file /tmp/clusterold.sql won't be created because the installer is
# trying to use the tools from the previous installation (x86_64) in the
# install environment (i386). that is, you can't run a 64-bit program
# in a 32-bit environment.
#
# Revision 1.74  2005/10/06 16:26:43  bruno
# must explicitly put the steps to skip in order to do manual partitioning
# on the frontend.
#
# Revision 1.73  2005/10/04 21:21:23  bruno
# have frontend use 'manual' partition directive when user selects manual
# partitioning
#
# Revision 1.72  2005/09/30 20:46:25  bruno
# on frontend's, only re-partition the first drive that linux finds.
#
# leave all other drives untouched.
#
# Revision 1.71  2005/09/28 22:46:27  bruno
# bug fixes for frontend installs with mixed IDE and SCSI drives including
# some of these drives being configured as software RAID(s).
#
# Revision 1.70  2005/09/20 23:04:02  bruno
# no longer remove all partitions before displaying the partition screen.
#
# Revision 1.69  2005/09/19 22:08:36  bruno
# partitioning tuning.
#
# - the frontend and NAS appliance will no longer nuke all partitions before
#   the partitioning screen
# - a NAS appliance always displays the partitioning screen
# - added a nas-exports node to make it easier for people to customize
#   their export directories on NAS appliances
# - hardened the software raid partitioning code
#
# Revision 1.68  2005/09/16 01:03:17  mjk
# updated copyright
#
# Revision 1.67  2005/07/03 08:55:42  tsailm
# A better choice for public ntp servers.
#
# Revision 1.66  2005/05/31 18:18:33  bruno
# suppress harmless python warning
#
# Revision 1.65  2005/05/24 21:22:42  mjk
# update copyright, release is not any closer
#
# Revision 1.64  2005/05/24 13:37:12  bruno
# support for frontend upgrades and for newly-installed frontends
#
# Revision 1.63  2005/05/23 23:55:27  fds
# Fixed recent checkin log
#
# Revision 1.62  2005/05/23 23:52:43  fds
# Frontend Restore
#
# Revision 1.61  2005/04/25 23:30:43  bruno
# upgrade fix
#
# Revision 1.60  2005/04/12 01:56:14  fds
# Moved certificate management earlier in the install process.
#
# Revision 1.59  2005/04/08 23:49:55  fds
# Dont insert duplicate roll entries into database for multi-disk rolls.
#
# Revision 1.58  2005/03/31 22:38:59  fds
# Secure WAN kickstart
#
# Revision 1.57  2005/03/18 00:15:41  fds
# Structure for using secure keys on USB drives.
#
# Revision 1.56  2005/03/16 03:36:30  fds
# Actually inserting selected rolls into database.
#
# Revision 1.55  2005/03/15 21:26:50  bruno
# utilize the 'force-default' functionality to make a frontend's disk
# become a rocks default disk
#
# Revision 1.54  2005/03/15 17:50:20  bruno
# initialize
#
# Revision 1.53  2005/03/15 05:59:18  bruno
# don't do self on initialization
#
# Revision 1.52  2005/03/15 02:35:35  fds
# Record selected rolls in site.xml. Started self.log() for debugging.
#
# Revision 1.51  2005/03/12 00:01:53  bruno
# minor checkin
#
# Revision 1.50  2005/02/13 22:16:27  fds
# 411 version 2, part of the friday checkin. Tested in San Diego.
#
# Revision 1.49  2004/12/13 14:45:38  bruno
# took away the DHCP and 'activate on boot' option from eth0 and eth1
# for a frontend installation.
#
# Revision 1.48  2004/11/03 23:19:45  fds
# whrandom module is depricated in favor of random, but the anaconda
# installer environment has only whrandom.
#
# Revision 1.47  2004/11/03 00:16:37  fds
# Typo
#
# Revision 1.46  2004/11/03 00:03:56  fds
# Multicast choice conforms to RFC 1700.
#
# Revision 1.45  2004/11/02 00:26:44  fds
# Ganglia gets a random mcast channel.
#
# Revision 1.44  2004/10/04 21:17:28  bruno
# force grub-install to run
#
# give the user the ability to 'force-default' partition on a compute node
#
# Revision 1.43  2004/08/26 23:11:02  fds
# Do not seem to need this anymore
#
# Revision 1.42  2004/08/25 05:05:55  bruno
# need to import time before using sleep function
#
# Revision 1.41  2004/08/24 22:00:59  fds
# Tweak to NTP screen spacing
#
# Revision 1.40  2004/08/24 01:56:12  fds
# Gateway and NS guesses. Also dont save easily-mangled motd accross
# updates.
#
# Revision 1.39  2004/08/23 23:26:03  bruno
# we now have user-settable timezones and an ntp server.
#
# this address bug 6.
#
# Revision 1.38  2004/08/20 22:01:15  fds
# Gateway set to a guess based on eth1. This fixes bug 16
#
# Revision 1.37  2004/08/11 22:38:50  bruno
# the real fix for bug 16
#
# Revision 1.36  2004/08/10 14:37:26  bruno
# first pass at installing a frontend from a distribution that is housed
# on the frontend's local disk.
#
# Revision 1.35  2004/08/09 23:47:49  fds
# Carry over ca serial number.
#
# Revision 1.34  2004/07/28 21:34:12  fds
# App_globals: dhcpd filename and --url correct now.
#
# Revision 1.33  2004/07/26 21:57:39  fds
# Resurrect previous keys for 411, CA, and our cluster cert. Since loader
# makes disks bootable now, removed some dead code.
#
# Revision 1.32  2004/07/16 18:13:29  bruno
# make sure the 'gateway' field on the network configuration screen is
# clear (and not defaulted to 10.x.x.x).
#
# this fixes bug 16.
#
# Revision 1.31  2004/07/15 18:58:14  fds
# Removed hostname screen. We are not setting network.hostname for
# anaconda, but things still seem ok.
#
# Revision 1.30  2004/07/13 23:26:55  fds
# Use new FQDN input from cluster info screen
#
# Revision 1.29  2004/07/12 21:29:12  fds
# no external
#
# Revision 1.28  2004/06/21 20:34:50  fds
# Store our kickstart parent.
#
# Revision 1.27  2004/05/28 23:24:38  bruno
# do the sure kill of mysqld when doing an upgrade
#
# Revision 1.26  2004/05/27 01:19:56  bruno
# make sure the saved site.xml on the frontend is only readable by root
#
# Revision 1.25  2004/04/28 17:34:19  bruno
# added support for variable-sized root and swap partitions
#
# Revision 1.24  2004/04/26 20:12:03  fds
# Added rocks-boot-auto to frontend. It is off by default. Also put
# kickstart central host in app_globals if available.
#
# Revision 1.23  2004/04/07 23:33:01  bruno
# make root 6 GB
#
# Revision 1.22  2004/03/25 03:16:08  bruno
# touch 'em all!
#
# update version numbers to 3.2.0 and update copyrights
#
# Revision 1.21  2004/03/19 03:30:16  bruno
# need to return a string from mask2cidr in order to write the returned value
# to the site.xml file
#
# Revision 1.20  2004/03/08 23:14:18  fds
# Here is Postfix.
#
# Revision 1.19  2004/03/05 03:10:19  bruno
# change root file system to be 8000 MB
#
# Revision 1.18  2004/03/05 01:17:53  fds
# We need CIDR netmasks for postfix. Here they are.
#
# Revision 1.17  2004/03/02 22:24:15  bruno
# now handle multiple DNS servers
#
# Revision 1.16  2004/02/20 13:24:32  bruno
# added code to detect and write secondary and ternary nameserver info
# into database
#
# Revision 1.15  2004/02/12 00:39:23  fds
# Moved functionality into base.
#
# Revision 1.14  2004/02/02 21:08:11  fds
# Doing it the right way. A new frontend-wan file defines the main
# kickstart section for Wide Area kickstart installs (instead of
# hard-coding it in kcgi.)
#
# Revision 1.13  2004/02/02 18:30:41  fds
# Hijacking the interactive kickstart command to include path to external rolls.
#
# Revision 1.12  2004/01/09 02:31:59  bruno
# make ext3 default file system on frontend
#
# Revision 1.11  2003/12/19 16:37:35  bruno
# fix for frontend upgrade
#
# Revision 1.10  2003/12/17 01:32:50  bruno
# moved private/public message to ekv
#
# Revision 1.9  2003/12/16 19:27:44  bruno
# me not so smart
#
# Revision 1.8  2003/10/16 18:22:04  bruno
# changes for x86_64
#
# Revision 1.7  2003/10/02 20:34:51  fds
# We dont use usher anymore (although it was cool).
#
# Revision 1.6  2003/08/27 23:10:55  mjk
# - copyright update
# - rocks-dist uses getArch() fix the i686 distro bug
# - ganglia-python spec file fixes (bad service start code)
# - found some 80col issues while reading code
# - WAN ks support starting
#
# Revision 1.5  2003/08/13 17:18:51  bruno
# put in rocks copyright for 3.0.0
#
# Revision 1.4  2003/08/13 15:22:53  bruno
# added public domain dedication
#
# Revision 1.3  2003/07/25 20:48:59  fds
# Setting the Public DNS Domain.
#
# Revision 1.2  2003/07/25 19:51:43  bruno
# added modal dialog
#
# Revision 1.1  2003/07/07 20:47:51  bruno
# initial release
#
# Revision 1.10  2003/06/24 20:44:00  fds
# Private frontend name is host-only.
#
# Revision 1.9  2003/05/27 21:00:35  fds
# Changed default private domain name to .local
#
# Revision 1.8  2003/05/23 01:20:09  fds
# Recommitting my DNS changes from installclass-frontend.xml version 1.52
#
# Revision 1.7  2003/05/22 16:36:35  mjk
# copyright
#
# Revision 1.6  2003/04/28 20:04:04  mjk
# no more over ticking
#
# Revision 1.5  2003/04/28 19:54:13  mjk
# more installclass fixes
#
# Revision 1.4  2003/04/28 18:44:12  mjk
# install class fixes
#
# Revision 1.3  2003/04/25 18:40:59  bruno
# try to be a bit more tricky with the way Info values are included.
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
import crypt
import whrandom
import string
from dispatch import installSteps
import isys
import urlparse


class CustomKickstart(RocksCustomKickstart):

	rockslog = None

	def log(self, msg):
		logname = '/tmp/rocks.debug'
		if not self.rockslog:
			self.rockslog = open(logname, 'a')
		self.rockslog.write(msg + '\n')

	def setSteps(self, dispatch):
		RocksCustomKickstart.setSteps(self, dispatch)            

		#
		# call the frontend specific file system setup method
		#
		index = 0
		for key in installSteps:
			if key[0] == "enablefilesystems":
				break
			index = index + 1

		installSteps[index] = ("enablefilesystems",
			FrontendRocksTurnOnFilesystems,
			("dir", "id.fsset", "id.diskset", "id.partitions",
				"id.upgrade", "instPath"))

		dispatch.skipStep("enablefilesystems", skip = 0)

		return


	def __init__(self, file, serial):
		# need to copy the kickstart file to another location
		# because there is a bug in the __init__ method below
		# that removes the kickstart file after parsing the
		# installclass section

		rocksfile = file + ".rocks"
		os.link(file, rocksfile)

		RocksCustomKickstart.__init__(self, rocksfile, serial)


def FrontendRocksTurnOnFilesystems(dir, thefsset, diskset, partitions, upgrade,
	instPath):

	from packages import turnOnFilesystems

	turnOnFilesystems(dir, thefsset, diskset, partitions, upgrade, instPath)

	#
	# mark all the disks as 'seen' by rocks
	#
	rocksdiskset = RocksDiskSet(diskset, thefsset, None)
	rocksdiskset.rocksDiskStamp()

	import os

	cwd = os.getcwd()
	os.chdir('/mnt/sysimage')
	try:
		os.symlink('state/partition1', 'export')
	except:
		pass

	os.chdir(cwd)

	return

