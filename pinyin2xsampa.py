#!/usr/bin/env python3

# Copyright (C) 2014  StarBrilliant <m13253@hotmail.com>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 3.0 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program.  If not,
# see <http://www.gnu.org/licenses/>.

# ============================================================================

# Modifications made by Ritchy Tang <mizuki.ykn@outlook.com>
# Copyright (C) 2024 Ritchy Tang <mizuki.ykn@outlook.com>
#
# Description of modifications:
# - changed the XSAMPA standard to the one used by Synthesizer V
#   - removed support for words end with 'r' 
#   - removed support for '\u00ea' ('ê') and 'eh'
#   - removed support for 'amg', 'emgs', 'um', 'em', etc.
#   - removed support for 'io'
# - modified the XSAMPA for 'yo' from 'j iAU' to 'j uo'

import sys
import json


if sys.version_info < (3,):
    sys.stderr.write('This script requires Python 3 or higher version.\n')
    sys.exit(1)


wholereplacetable = (
    ('yi', 'i'), ('wu', 'u'), ('yu', 'v'),
    ('bo', 'buo'), ('po', 'puo'), ('mo', 'muo'), ('fo', 'fuo'),
    ('zhi', 'zhirh'), ('chi', 'chirh'), ('shi', 'shirh'), ('ri', 'rirh'),
    ('zi', 'zih'), ('ci', 'cih'), ('si', 'sih')
)
localreplacetable = ( 
    ('\u00fc', 'v'),
    ('yu', 'y_v'), ('ju', 'jv'), ('qu', 'qv'), ('xu', 'xv'), 
    ('ui', 'uei'), ('un', 'uen'),
    ('w', 'w_u'), ('yi', 'y_i'), ('y', 'y_i')
)
initialtable = (
    ('b', 'p'), ('p', 'ph'), ('m', 'm'), ('f', 'f'), ('d', 't'), ('t', 'th'),
    ('ng', 'N'), ('n', 'n'), ('l', 'l'), ('g', 'k'), ('k', 'kh'), ('h', 'x'),
    ('j', 'ts\\'), ('q', 'ts\\h'), ('x', 's\\'), ('zh', 'ts`'),
    ('ch', 'ts`h'), ('sh', 's`'), ('r', 'z`'), ('w_', 'w'), ('y_', 'j'),
    ('z', 'ts'), ('c', 'tsh'), ('s', 's')
)
finaltable = (
    ('iang', 'iA N'), ('iong', 'iU N'), ('uang', 'uA N'), ('ueng', 'u@ N'),
    ('ang', 'A N'), ('eng', '@ N'), ('ing', 'i N'),
    ('ian', 'iE :n'), ('iao', 'iAU'), ('iai', 'ia :\\i'),
    ('iou', 'i@U'), ('ong', 'U N'), ('uai', 'ua :\\i'), 
    ('uan', 'ua :n'), ('uei', 'ue :\\i'), ('uen', 'u@ :n'),
    ('van', 'y{ :n'), ('ai', 'a :\\i'), ('an', 'a :n'),
    ('ao', 'AU'), ('ei', 'e :\\i'), ('en', '@ :n'), ('ia', 'ia'),
    ('ie', 'ie'), ('in', 'i :n'), ('iu', 'i@U'), ('ou', '@U'),
    ('ua', 'ua'), ('uo', 'uo'), ('ve', 'yE'), ('vn', 'yE :n'),
    ('ng', 'N'), ('n', 'n'), ('a', 'a'), ('o', 'o'),
    ('e', '7'), ('ih', 'i\\'), ('irh', 'i`'), ('i', 'i'), ('u', 'u'), ('v', 'y')
)


def pinyin2xsampa(word):
    if word == 'er':
        return 'a r\\`'
    if word == 'yo':
        return 'j uo'
    if word[1:].endswith('r'):
        return 'ERROR'
    
    for i in wholereplacetable:
        if word == i[0]:
            word = i[1]
            break
        
    # while True:
    for i in localreplacetable:
        wordnew = word.replace(i[0], i[1])
        if wordnew != word:
            word = wordnew
            break
        # else:
        #     break
        
    phonetics = []
    
    for i in initialtable:
        if word.startswith(i[0]):
            phonetics.append(i[1])
            word = word[len(i[0]):]
            break
    
    while True:
        for i in finaltable:
            if word.startswith(i[0]):
                phonetics.append(i[1])
                word = word[len(i[0]):]
                break
        else:
            break
    
    if word:
        return 'ERROR'

    phonetics = ' '.join(phonetics)
    return phonetics


def main():
    retval = 0
    while True:
        try:
            line = input('> ') if sys.stdin.isatty() else input()
        except EOFError:
            break
        line = line.replace("'", ' ')
        words = line.split()
        output_line = []
        for word in words:
            phonetics = pinyin2xsampa(word)
            output_line.append('[' + phonetics + ']')
        print(' '.join(output_line))
    return retval

def testbench():
    with open('pinyin2xsampa.json') as f:
        data = json.load(f)
    
    count_same = 0
    count_different = 0
    difference = []
    
    for key, value in data.items():
        phonetics = pinyin2xsampa(key)
        if phonetics == value:
            count_same += 1
        else:
            count_different += 1
            difference.append((key, value, phonetics))
    
    print(f"Same count: {count_same}")
    print(f"Different count: {count_different}")
    print(f"Difference: {difference}")

if __name__ == '__main__':
    
    testbench()
    sys.exit(main())
