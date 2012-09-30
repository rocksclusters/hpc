# Get the Openmpi version from it's version.mk file. See Makefile
VERSION.MK.MASTER = version.mk
VERSION.MK.MASTER.DIR = ../openmpi
VERSION.MK.INCLUDE = openmpi.version.mk

include $(VERSION.MK.INCLUDE) 
NAME		= rocks-openmpi-modules
RELEASE		= 1
RPM.REQUIRES	= environment-modules
