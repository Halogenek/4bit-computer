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
#Then you can direct jump to those labels
#Instructions below the label will be executed
#example:
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
labels = {}
machine_code = []
machine_code.append('v2.0 raw')
asm_fp = open(sys.argv[1], 'r')
lines_list = asm_fp.readlines()
for line in lines_list:
    if line[0] == '#':
        continue
    elif line[0] == '&':
        labels[line.split()[0]] = len(machine_code) + 1
    else:
        if 'NOP' in line:
            machine_code.append('00')
            continue
        elif 'TOG ' in line:
            if 'ROM' in line:
                machine_code.append('10')
                continue
            elif 'ALURES' in line:
                machine_code.append('11')
                continue
            elif 'RAMWR' in line:
                machine_code.append('12')
                continue
            elif 'RSEL' in line:
                machine_code.append('13')
                continue
            else:
                sys.exit('unknown TOG argument in line ' \
                    + lines_list.index(line) + ': ' + line)
        elif 'WRI ' in line:
            if 'PCOU' in line:
                machine_code.append('20')
                continue
            elif 'PARA' in line:
                machine_code.append('21')
                continue
            elif 'PARB' in line:
                machine_code.append('22')
                continue
            elif 'PARC' in line:
                machine_code.append('23')
                continue
            elif 'ALUAR' in line:
                machine_code.append('24')
                continue
            elif 'ALUBR' in line:
                machine_code.append('25')
                continue
            elif 'ALUOR' in line:
                machine_code.append('26')
                continue
            elif 'ALURR' in line:
                machine_code.append('27')
                continue
            elif 'RARADDR' in line:
                machine_code.append('28')
                continue
            elif 'PCOUZ' in line:
                machine_code.append('29')
                continue
            elif 'PCOUNZ' in line:
                machine_code.append('2a')
                continue
            elif 'PCOUC' in line:
                machine_code.append('2b')
                continue
            elif 'PCOUNZ' in line:
                machine_code.append('2c')
                continue
            else:
                sys.exit('unknown WRI argument in line ' \
                    + lines_list.index(line) + ': ' + line)
        elif 'WRIDAT ' in line:
            machine_code.append('3' + line.split() + '')
            continue
        elif 'DJMP ' in line:
            if '&' in line:
                machine_code.append('4' + ' ' + line.split()[1])
                machine_code.append('place_holder')
                continue
            else:
                machine_code.append('4' + list(line.split()[1])[0])
                machine_code.append(list(line.split()[1])[1] + \
                    list(line.split()[1])[2])
                continue
for command in machine_code:
    if '&' in command:
        hexaddress_str = "%0.3X" % labels[command.split()[1]]
        index_of_label = machine_code.index(command)
        machine_code[index_of_label] = command[0] \
            + hexaddress_str[0]
        machine_code[index_of_label + 1] = hexaddress_str[1:3]
for line in machine_code:
    machine_code_fp.write(line + '\r\n')
