#!/usr/bin/python

#This is an simple assembler for the asm code for the 4 bit processor
#
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
with open(sys.argv[1]) as asm_fp:
    for line in asm_fp:
        if 'NOP' in line:
            machine_code_fp.write('00\r\n')
            continue
        elif 'TOG ' in line:
            if 'ROM' in line:
                machine_code_fp.write('10\r\n')
                continue
            elif 'ALURES' in line:
                machine_code_fp.write('11\r\n')
                continue
            elif 'RAMWR' in line:
                machine_code_fp.write('12\r\n')
                continue
            elif 'RSEL' in line:
                machine_code_fp.write('13\r\n')
                continue
            else:
                sys.exit('unknown TOG argument')
        elif 'WRI ' in line:
            if 'PCOU' in line:
                machine_code_fp.write('20\r\n')
                continue
            elif 'PARA' in line:
                machine_code_fp.write('21\r\n')
                continue
            elif 'PARB' in line:
                machine_code_fp.write('22\r\n')
                continue
            elif 'PARC' in line:
                machine_code_fp.write('23\r\n')
                continue
            elif 'ALUAR' in line:
                machine_code_fp.write('24\r\n')
                continue
            elif 'ALUBR' in line:
                machine_code_fp.write('25\r\n')
                continue
            elif 'ALUOR' in line:
                machine_code_fp.write('26\r\n')
                continue
            elif 'ALURR' in line:
                machine_code_fp.write('27\r\n')
                continue
            elif 'RARADDR' in line:
                machine_code_fp.write('28\r\n')
                continue
            elif 'PCOUZ' in line:
                machine_code_fp.write('29\r\n')
                continue
            elif 'PCOUNZ' in line:
                machine_code_fp.write('2a\r\n')
                continue
            elif 'PCOUC' in line:
                machine_code_fp.write('2b\r\n')
                continue
            elif 'PCOUNZ' in line:
                machine_code_fp.write('2c\r\n')
                continue
            else:
                sys.exit('unknown WRI argument')
        if 'WRIDAT ' in line:
            temp_str = line.split()
            machine_code_fp.write('3'+temp_str[1]+'\r\n')
            continue

#TODO calculate jump addresses and write them in the machine code file
