# Copyright (C) 2007 Samuel Abels, http://debain.org
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2, as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
import Expression
from Token import Token

class Assign(Token):
    def __init__(self, parser, parent):
        Token.__init__(self, 'Assign', parser)
        self.parent = parent

        # Extract the variable name.
        (type, self.varname) = parser.token()
        parser.expect('varname')
        parser.expect('whitespace')
        parser.expect('assign')
        parser.expect('whitespace')
        self.expression = Expression.Expression(parser, parent)
        self.parent.define(**{self.varname: None})


    def dump(self, indent = 0):
        print (' ' * indent) + self.name, self.varname, 'start'
        self.expression.dump(indent + 1)
        print (' ' * indent) + self.name, self.varname, 'start'


    def value(self):
        result = self.expression.value()
        self.parent.define(**{self.varname: result})
        return result