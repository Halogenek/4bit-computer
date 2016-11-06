#!/usr/bin/python

#This is an assembler for the asm code for the
#4 bit processor
#
#The instructions are:
#
###############################################
import sys
machine_code_fp = open('code.txt', 'w+')
with open(sys.argv[1]) as asm_fp:
    for line in asm_fp:
        print line
#TODO check for instruction
#TODO save machine code to file
#TODO calculate jump addresses and write them in the machine code file
