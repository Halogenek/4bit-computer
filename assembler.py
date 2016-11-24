#!/usr/bin/python3

#This is an simple assembler for the asm code for the 4 bit processor
###############################################
#The instructions are:
#NOP    0x00 - do nothing
#
#TOG        0x1X - toggle
#    ROM       0 - ROM data bus connection
#    ALURES    1 - ALU result bus connection
#    RAMWR     2 - RAM write/read
#    RSEL      3 - select RAM
#
#WRI        0x2X - write to...
#    PCOU      0 - program counter
#    PARA      1 - program address register A
#    PARB      2 - program address register B
#    PARC      3 - program address register C
#    ALUAR     4 - ALU A register
#    ALUBR     5 - ALU B register
#    ALUOR     6 - ALU operation register
#    ALURR     7 - ALU result register
#    RARADDR   8 - RAM address register
#    PCOUZ     9 - program counter if zero flag
#    PCOUNZ    A - program counter if no zero flag
#    PCOUC     B - program counter if carry flag
#    PCOUNZ    C - program counter if no zero flag
#
#WRIDAT X    0x3X - write 4 bits of data to ROM register
#
#DJMP XXX    0x4X
#            0xXX - direct jump to a 12 bit ROM address, MSB first LSB last
###############################################
#Line starting with '#' will be ignored
#Every word that's not an instruction fron the list abowe will be ignored
#
#You can put labels in code with '&LABEL'
#Then you can direct jump to those labels example:
#&LABEL
#DJMP &LABEL
###############################################

import sys
if len(sys.argv) < 3:
    print('no path to input or output file')
    print('use: program [input_file] [output_file]')
    sys.exit(1)
elif len(sys.argv) > 3:
    print('too many arguments')
    print('use: program [input_file] [output_file]')
    sys.exit(1)
machine_code_fp = open(sys.argv[2], 'w')
machine_code_fp.write('v2.0 raw\r\n')
labels = {}
machine_code_line = 0
with open(sys.argv[1]) as asm_fp:
    for line in asm_fp:
        if line[0] == '#':
            continue
        elif line[0] == '&':
            labels[line.partition('&')[2].partition(' ')[0]] \
                = machine_code_fp.tell() - 1
        else:
            if 'NOP' in line:
                machine_code_fp.write('00\r\n')
                machine_code_line += 1
                continue
            elif 'TOG ' in line:
                if 'ROM' in line:
                    machine_code_fp.write('10\r\n')
                    machine_code_line += 1
                    continue
                elif 'ALURES' in line:
                    machine_code_fp.write('11\r\n')
                    machine_code_line += 1
                    continue
                elif 'RAMWR' in line:
                    machine_code_fp.write('12\r\n')
                    machine_code_line += 1
                    continue
                elif 'RSEL' in line:
                    machine_code_fp.write('13\r\n')
                    machine_code_line += 1
                    continue
                else:
                    sys.exit('unknown TOG argument in line ' \
                        + str(asm_fp.tell()) + ': ' + line)
            elif 'WRI ' in line:
                if 'PCOU' in line:
                    machine_code_fp.write('20\r\n')
                    machine_code_line += 1
                    continue
                elif 'PARA' in line:
                    machine_code_fp.write('21\r\n')
                    machine_code_line += 1
                    continue
                elif 'PARB' in line:
                    machine_code_fp.write('22\r\n')
                    machine_code_line += 1
                    continue
                elif 'PARC' in line:
                    machine_code_fp.write('23\r\n')
                    machine_code_line += 1
                    continue
                elif 'ALUAR' in line:
                    machine_code_fp.write('24\r\n')
                    machine_code_line += 1
                    continue
                elif 'ALUBR' in line:
                    machine_code_fp.write('25\r\n')
                    machine_code_line += 1
                    continue
                elif 'ALUOR' in line:
                    machine_code_fp.write('26\r\n')
                    machine_code_line += 1
                    continue
                elif 'ALURR' in line:
                    machine_code_fp.write('27\r\n')
                    machine_code_line += 1
                    continue
                elif 'RARADDR' in line:
                    machine_code_fp.write('28\r\n')
                    machine_code_line += 1
                    continue
                elif 'PCOUZ' in line:
                    machine_code_fp.write('29\r\n')
                    machine_code_line += 1
                    continue
                elif 'PCOUNZ' in line:
                    machine_code_fp.write('2a\r\n')
                    machine_code_line += 1
                    continue
                elif 'PCOUC' in line:
                    machine_code_fp.write('2b\r\n')
                    machine_code_line += 1
                    continue
                elif 'PCOUNZ' in line:
                    machine_code_fp.write('2c\r\n')
                    machine_code_line += 1
                    continue
                else:
                    sys.exit('unknown WRI argument in line ' \
                        + str(asm_fp.tell()) + ': ' + line)
            elif 'WRIDAT ' in line:
                temp_str = line.split()
                machine_code_fp.write('3'+temp_str[1]+'\r\n')
                machine_code_line += 1
                continue
            elif 'DJMP ' in line:
                if '&' in line:
                    machine_code_fp.write('4' + line.slit()[1])
                    machine_code_line += 2
                    continue
                else:
                    temp_str = line.split()
                    temp_str1 = list(temp_str[1])
                    machine_code_fp.write('4'+temp_str1[0]+'\r\n')
                    machine_code_fp.write(temp_str1[1]+temp_str1[2]+'\r\n')
                    machine_code_line += 2
                    continue
#TODO calculate jump addresses and write them in the machine code file
