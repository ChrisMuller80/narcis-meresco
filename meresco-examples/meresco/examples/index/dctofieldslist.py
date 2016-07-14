## begin license ##
#
# "Meresco Examples" is a project demonstrating some of the
# features of various components of the "Meresco Suite".
# Also see http://meresco.org.
#
# Copyright (C) 2016 Seecr (Seek You Too B.V.) http://seecr.nl
#
# This file is part of "Meresco Examples"
#
# "Meresco Examples" is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# "Meresco Examples" is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with "Meresco Examples"; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#
## end license ##

from meresco.core import Observable
from meresco.xml.namespaces import tagToCurie

class DcToFieldsList(Observable):

    def add(self, lxmlNode, **kwargs):
        fieldslist = []
        for child in lxmlNode.getroot().getchildren():
            fieldname = tagToCurie(child.tag)
            fieldslist.append((fieldname, child.text))
            # if fieldname == 'dc:identifier' and child.text=='http://meresco.com?record=1':
            # 	fieldslist.append(('genre', 'boek'))
            # elif fieldname == 'dc:identifier':
            # 	fieldslist.append(('genre', 'boek'))

        yield self.all.add(fieldslist=fieldslist, **kwargs)