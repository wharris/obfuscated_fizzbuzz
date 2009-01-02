#!/usr/bin/env python
# encoding: utf-8

# colourwords.py - play fizzbuzz.
# Copyright (C) 2008  Will Harris
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

debug=False
def deb(s):
    if debug:
        print s

def run(program, stack):
    deb("  %r" % stack)
    pc = 0
    while pc < len(program):
        ch = program[pc]
        pc += 1
        if ch == '%':
            y, x = stack.pop(), stack.pop()
            stack.append(x%y)
        elif ch in '0123456789':
            stack.append(ord(ch) - ord('0'))
        elif ch in 'abcdef':
            stack.append(ord(ch) - ord('a') + 10)
        elif ch == "<":
            stack.append(stack.pop() << stack.pop())
        elif ch == '=':
            stack.append(stack.pop() == stack.pop())
        elif ch == 'P':
            print ("%s" % stack.pop()),
        elif ch == 'C':
            stack.append(chr(stack.pop()))
        elif ch == '+':
            stack.append(stack.pop() + stack.pop())
        elif ch == '?':
            deb("  ----")
            t, f, c = stack.pop(), stack.pop(), stack.pop()
            deb("  %(t)r if %(c)r else %(f)s" % locals())
            stack.append(t if c else f)
        elif ch == 'D':
            stack.append(stack[-1])
        elif ch == 'S':
            x, y = stack.pop(), stack.pop()
            stack.append(x)
            stack.append(y)
        elif ch == '!':
            i = stack.pop()
            c = stack.pop()
            if c:
                pc = i
        else:
            continue
        deb("%s %r" % (ch, stack))
    return stack

program = (
"1DDf%0=SD3%0=SD5%0=S47<a+C47<a+C+47<5+C+46<2+C+?47<a+C47<a+C+46<9+C+46<6+C+?"
"47<a+C47<a+C+47<5+C+46<2+C+47<a+C+47<a+C+46<9+C+46<6+C+?P1+D46<4+=10==1!")

run(program, [])
