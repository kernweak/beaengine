#!/usr/bin/python
# -*- coding: utf-8 -*-
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
# @author : beaengine@gmail.com

from headers.BeaEnginePython import *
from nose.tools import *

class TestSuite:
    def test(self):
        # 0F c0 /r
        # XADD r/m8, r8

        Buffer = '0fc09011223344'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0xfc0')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'xadd ')
        assert_equal(myDisasm.instr.repr, 'xadd byte ptr [rax+44332211h], dl')
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.AccessMode, WRITE)

        # REX + 0F C0 /r
        # XADD r/m8*, r8*

        Buffer = '410fc09011223344'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0xfc0')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'xadd ')
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.AccessMode, WRITE)
        assert_equal(myDisasm.instr.repr, 'xadd byte ptr [r8+44332211h], dl')

        # if LOCK and destination is not memory

        Buffer = 'f00fc0c011223344'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0xfc0')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'xadd ')
        assert_equal(myDisasm.instr.repr, 'lock xadd al, al')
        assert_equal(myDisasm.instr.Reserved_.ERROR_OPCODE, UD_)
