#buble sort
#5 2 1 3 4

#load numbers to ram
TOG ROM            connect rom register to data bus (on)
WRIDAT 5           write 5 to the rom register (1 element)
TOG RSEL           selct ram (write to ram)
WRIDAT 1           write 1 to the rom register
WRI RAMADDR        write data (1) from bus to ram address register
WRIDAT 2           write 2 to the rom register (2 element)
TOG RSEL           selct ram (write to ram)
WRIDAT 2           write 2 to the rom register
WRI RAMADDR        write data (2) from bus to ram address register
WRIDAT 1           write 2 to the rom register (3 element)
TOG RSEL           selct ram (write to ram)
WRIDAT 3           write 3 to the rom register
WRI RAMADDR        write data (3) from bus to ram address register
WRIDAT 3           write 3 to the rom register (4 element)
TOG RSEL           selct ram (write to ram)
WRIDAT 4           write 4 to the rom register
WRI RAMADDR        write data (4) from bus to ram address register
WRIDAT 4           write 4 to the rom register (5 element)
TOG RSEL           selct ram (write to ram)

&LOOP_COUNTS_RESET
WRI ALUOR          write (4) to the alu op register (add)
WRIDAT F           write f to the rom register
WRI RAMADDR        write data (f) from bus to ram address register
WRIDAT 5           write 5 to the rom register (for 5 elements)
TOG RSEL           selct ram (write to ram)

&CHECK_IF_IN_ORDER_LOOP
NOP

&DECRESE_COUNTER
WRIDAT F           write f to the rom register
WRI RAMADDR        write data (f) from bus to ram address register
WRI ALUOR          write data (f) from bus to alu op register
WRIDAT 1           write 1 to the rom register
WRI ALUBR          write data (1) to alu b register
TOG ROM            disconnect rom register from data bus (off)
TOG RAMWR          toggle write/read on ram (read)
TOG RSEL           select ram (read from ram)
WRI ALUAR          write to alu a register
TOG RAMWR          toggle write/read on ram (write)
WRI ALURR          write result to alu res register
TOG ALURES         connect alu res register to bus (on)
TOG RSEL           select ram (write to ram)
TOG ALURES         disconnect alu res register from bus (off)
TOG ROM            connect rom register from data bus (on)
DJMPZF &ALL_IN_ORDER_CHECK
DJMP &CHECK_IF_IN_ORDER_LOOP

&ALL_IN_ORDER_CHECK

&NEVER_ENDING_STORY
DJMP &NEVER_ENDING_STORY
