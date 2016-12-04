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

#ROM connected to bus

&LOOP_COUNTS_RESET
WRIDAT F           write f to the rom register
WRI RAMADDR        write data (f) from bus to ram address register
WRIDAT 4           write 4 to the rom register (for 5 elements)
TOG RSEL           selct ram (write to ram)

#ROM connected to bus

&CALCULATE_ADDRESSES_AND_GET_VALUES
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
WRI RAMADDR        write data from bus to ram address register
TOG ALURES         disconnect alu res register from bus (off)

TOG RAMWR          toggle write/read on ram (read)
WRI ALUBR          write to alu b register
TOG RAMWR          toggle write/read on ram (write)

TOG ROM            connect rom register to data bus (on)
WRIDAT F           write f to the rom register
WRI RAMADDR        write data (f) from bus to ram address register
TOG ROM            disconnect rom register from data bus (off)

TOG RAMWR          toggle write/read on ram (read)
WRI RAMADDR        write data from bus to ram address register
WRI ALUAR          write data to alu a register
TOG RAMWR          toggle write/read on ram (write)

TOG ROM            connect rom register to data bus (on)

#ROM connected to bus

#if values in order skip the swap part
DJMPCF &DECRESE_COUNTER
#########################################
&SWAP_VALUES
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
TOG ROM            connect rom register to data bus (on)
WRIDAT E           write e to the rom register
WRI RAMADDR        write data (e) from bus to ram address register
TOG ROM            disconnect rom register from data bus (off)
TOG ALURES         connect alu res register to bus (on)
TOG RSEL           select ram (write to ram)
TOG ALURES         disconnect alu res register from bus (off)

#save value from r address to d cell in ram
TOG ROM            connect rom register to data bus (on)
WRIDAT 0           write 0 to the rom register
WRI ALUBR          write data (0) to alu b register
WRIDAT F           write f to the rom register
WRI RAMADDR        write data (f) from bus to ram address register
TOG ROM            disconnect rom register from data bus (off)
TOG RAMWR          toggle write/read on ram (read)
TOG RSEL           select ram (read from ram)
WRI RAMADDR        write data from bus to ram address register
TOG RSEL           select ram (read from ram)
WRI ALUAR          write to alu a register
TOG RAMWR          toggle write/read on ram (write)
TOG ROM            connect rom register to data bus (on)
WRIDAT D           write d to the rom register
WRI RAMADDR        write data (d) from bus to ram address register
TOG ROM            disconnect rom register from data bus (off)
WRI ALURR          write result to alu res register
TOG ALURES         connect alu res register to bus (on)
TOG RSEL           selct ram (write to ram)
TOG ALURES         disconnect alu res register from bus (off)

#value from e adress save to cell with address in f
TOG ROM            connect rom register to data bus (on)
WRIDAT E           write e to the rom register
WRI RAMADDR        write data (e) from bus to ram address register
TOG ROM            disconnect rom register from data bus (off)
TOG RAMWR          toggle write/read on ram (read)
TOG RSEL           select ram (read from ram)
WRI RAMADDR        write data from bus to ram address register
TOG RSEL           select ram (read from ram)
WRI ALUAR          write to alu a register
TOG RAMWR          toggle write/read on ram (write)
WRI ALURR          write result to alu res register
TOG ROM            connect rom register to data bus (on)
WRIDAT F           write f to the rom register
WRI RAMADDR        write data (f) from bus to ram address register
TOG ROM            disconnect rom register from data bus (off)
TOG RAMWR          toggle write/read on ram (read)
TOG RSEL           select ram (read from ram)
WRI RAMADDR        write data from bus to ram address register
TOG RAMWR          toggle write/read on ram (write)
TOG ALURES         connect alu res register to bus (on)
TOG RSEL           selct ram (write to ram)
TOG ALURES         disconnect alu res register from bus (off)

#value from d call save to cell with e address
TOG ROM            connect rom register to data bus (on)
WRIDAT D           write d to the rom register
WRI RAMADDR        write data (d) from bus to ram address register
TOG ROM            disconnect rom register from data bus (off)
TOG RAMWR          toggle write/read on ram (read)
TOG RSEL           select ram (read from ram)
WRI RAMADDR        write data from bus to ram address register
TOG RSEL           select ram (read from ram)
WRI ALUAR          write to alu a register
TOG RAMWR          toggle write/read on ram (write)
WRI ALURR          write result to alu res register
TOG ROM            connect rom register to data bus (on)
WRIDAT E           write e to the rom register
WRI RAMADDR        write data (e) from bus to ram address register
TOG ROM            disconnect rom register from data bus (off)
TOG RAMWR          toggle write/read on ram (read)
TOG RSEL           select ram (read from ram)
WRI RAMADDR        write data from bus to ram address register
TOG RAMWR          toggle write/read on ram (write)
TOG ALURES         connect alu res register to bus (on)
TOG RSEL           selct ram (write to ram)
TOG ALURES         disconnect alu res register from bus (off)

TOG ROM            connect rom register to data bus (on)

#ROM connected to bus

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

TOG ROM            connect rom register to data bus (on)

#ROM connected to bus

#if counter will be zero jump to getting values
#if not jump to counter initialization
DJMPZF &LOOP_COUNTS_RESET
DJMP &CALCULATE_ADDRESSES_AND_GET_VALUES

&NEVER_ENDING_STORY
DJMP &NEVER_ENDING_STORY
