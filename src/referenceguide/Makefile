#
# $Id: Makefile,v 1.9 2008/03/06 23:41:54 mjk Exp $
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
# Revision 1.9  2008/03/06 23:41:54  mjk
# copyright storm on
#
# Revision 1.8  2007/06/23 04:03:40  mjk
# mars hill copyright
#
# Revision 1.7  2006/09/11 22:48:54  mjk
# monkey face copyright
#
# Revision 1.6  2006/08/10 00:10:59  mjk
# 4.2 copyright
#
# Revision 1.5  2006/01/31 18:01:49  bruno
# updated to 4.1 build environment
#
# Revision 1.4  2005/10/12 18:09:50  mjk
# final copyright for 4.1
#
# Revision 1.3  2005/09/16 01:03:27  mjk
# updated copyright
#
# Revision 1.2  2005/05/24 21:22:52  mjk
# update copyright, release is not any closer
#
# Revision 1.1  2005/03/15 01:28:45  fds
# Moved docs source into roll
#
# Revision 1.2  2004/05/04 20:01:58  fds
# Fixed link to pdf
#
# Revision 1.1  2004/04/14 19:49:59  fds
# A reference guide for APIs in Rocks.
#
#

GUIDENAME = rocks-documentation/reference-guide/$(VERSION)
PKGROOT = /var/www/html/$(GUIDENAME)
ROOT =
TESTUSER = $(USER)
OUTPUT = /var/www/html/test/$(GUIDENAME)
TESTOUTPUT = /home/$(TESTUSER)/public_html/$(GUIDENAME)

REDHAT.ROOT = $(PWD)/../../
DOCROOT = ../../../../../doc/etc
ROCKSROOT = ../../../../..
-include $(ROCKSROOT)/etc/Rules.mk
include Rules.mk

default: $(NAME).spec ../$(NAME)-$(VERSION).tar.gz

-include ../Rules.mk
include Rules.mk

html:	index.sgml
	jw --backend html --dsl $(PWD)/rocks.dsl#html \
		--output $(ROOT)/$(PKGROOT) index.sgml

index.sgml: index.sgml.in
	$(SED) $(SEDSPEC) $^ > $@

testinstall: pretar
	mkdir -p $(TESTOUTPUT)
	$(MAKE) ROOT=$(TESTOUTPUT) PKGROOT= install

# A proof is for running as a user.
proof: testinstall index.sgml
	jw --backend html --dsl $(PWD)/rocks.dsl#html \
		--output $(TESTOUTPUT) index.sgml

# Use test target if you are root.
test: testinstall index.sgml
	jw --backend html --dsl $(PWD)/rocks.dsl#html \
		--output $(OUTPUT) index.sgml
	install -ma+r rocks.css $(OUTPUT)

pdf: index.sgml
	jw --backend pdf --dsl $(PWD)/rocks.dsl#print index.sgml || true
ifdef ROOT
	install -ma+r index.pdf \
		$(ROOT)/$(PKGROOT)/rocks-referenceguide-$(VERSION).pdf
else
	mv index.pdf rocks-referenceguide-$(VERSION).pdf
endif

build:

pretar::
	cp -r $(DOCROOT)/rocks.* .
	cp -r $(DOCROOT)/stylesheet-images .

install::
	mkdir -p $(ROOT)/$(PKGROOT)/images/install
	mkdir -p $(ROOT)/$(PKGROOT)/images/rollguide
	mkdir -p $(ROOT)/$(PKGROOT)/papers
	mkdir -p $(ROOT)/$(PKGROOT)/stylesheet-images

	install -ma+r images/*.png $(ROOT)/$(PKGROOT)/images
	install -ma+r images/rollguide/*.png $(ROOT)/$(PKGROOT)/images/rollguide
	install -ma+r stylesheet-images/*.png \
		$(ROOT)/$(PKGROOT)/stylesheet-images
	install -ma+r rocks.css $(ROOT)/$(PKGROOT)/

clean::
	rm -f *.html
	rm -f index.pdf
	rm -f index.sgml
	rm -f jade-errors.txt
	rm -rf stylesheet-images
	rm -f rocks.css rocks.dsl

