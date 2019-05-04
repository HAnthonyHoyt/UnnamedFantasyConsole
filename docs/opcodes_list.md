# Opcodes List

This is the current actual list of Opcodes for the system, what the parameters
are and what they do.

## Reference

| Code | Name | Bytes | Flags | Parameters | Description |
|-|-|-|-|-|-|
|0x00|NOP|1|--||No operation|
|0x01|DI|1|--||Disable interupts|
|0x02|EI|1|--||Enable interupts|
|0x03|---|1|--||---|
|0x04|---|1|--||---|
|0x05|---|1|--||---|
|0x06|---|1|--||---|
|0x07|---|1|--||---|
|0x08|INC SP|1|--||Increment the Stack Pointer|
|0x09|DEC SP|1|--||Decrement the Stack Pointer|
|0x0A|LD CD, SP|1|--||LOAD the SP into CD|
|0x0B|LD EF, SP|1|--||LOAD the SP into EF|
|0x0C|LD SP, CD|1|--||LOAD CD into the SP|
|0x0D|LD SP, EF|1|--||LOAD CD into the SP|
|0x0E|LD SP, n16|3|--|n16|LOAD n16 into the SP|
|0x0F|---|1|--||---|
|0x10|LD A, n8|2|--|n8|LOAD n8 into A|
|0x11|LD A, B|1|--||LOAD B into A|
|0x12|LD A, C|1|--||LOAD C into A|
|0x13|LD A, D|1|--||LOAD D into A|
|0x14|LD A, E|1|--||LOAD E into A|
|0x15|LD A, F|1|--||LOAD F into A|
|0x16|LD A, \[CD]|1|--||LOAD the value located cat \[CD] into A|
|0x17|LD A, \[EF]|1|--||LOAD the value located cat \[EF] into A|
|0x18|LD B, A|1|--||LOAD A into B|
|0x19|LD B, n8|2|--|n8|LOAD n8 into B|
|0x1A|LD B, C|1|--||LOAD C into B|
|0x1B|LD B, D|1|--||LOAD D into B|
|0x1C|LD B, E|1|--||LOAD E into B|
|0x1D|LD B, F|1|--||LOAD F into B|
|0x1E|LD B, \[CD]|1|--||LOAD the value located cat \[CD] into B|
|0x1F|LD B, \[EF]|1|--||LOAD the value located cat \[EF] into B|
|0x20|LD C, A|1|--||LOAD A into C|
|0x21|LD C, B|1|--||LOAD B into C|
|0x22|LD C, n8|2|--|n8|LOAD n8 into C|
|0x23|LD C, D|1|--||LOAD D into C|
|0x24|LD C, E|1|--||LOAD E into C|
|0x25|LD C, F|1|--||LOAD F into C|
|0x26|LD C, \[CD]|1|--||LOAD the value located cat \[CD] into C|
|0x27|LD C, \[EF]|1|--||LOAD the value located cat \[EF] into C|
|0x28|LD D, A|1|--||LOAD A into D|
|0x29|LD D, B|1|--||LOAD B into D|
|0x2A|LD D, C|1|--||LOAD C into D|
|0x2B|LD D, n8|2|--|n8|LOAD n8 into D|
|0x2C|LD D, E|1|--||LOAD E into D|
|0x2D|LD D, F|1|--||LOAD F into D|
|0x2E|LD D, \[CD]|1|--||LOAD into located \[EF] the value C|
|0x2F|LD D, \[EF]|1|--||LOAD into located \[EF] the value C|
|0x30|LD E, A|1|--||LOAD A into E|
|0x31|LD E, B|1|--||LOAD B into E|
|0x32|LD E, C|1|--||LOAD C into E|
|0x33|LD E, D|1|--||LOAD D into E|
|0x34|LD E, n8|2|--|n8|LOAD n8 into E|
|0x35|LD E, F|1|--||LOAD F into E|
|0x36|LD E, \[CD]|1|--||LOAD into located \[EF] the value C|
|0x37|LD E, \[EF]|1|--||LOAD into located \[EF] the value C|
|0x38|LD F, A|1|--||LOAD A into F|
|0x39|LD F, B|1|--||LOAD B into F|
|0x3A|LD F, C|1|--||LOAD C into F|
|0x3B|LD F, D|1|--||LOAD D into F|
|0x3C|LD F, E|1|--||LOAD E into F|
|0x3D|LD F, n8|2|--|n8|LOAD n8 into F|
|0x3E|LD \[EF], C|1|--||LOAD into located \[EF] the value C|
|0x3F|LD \[EF], D|1|--||LOAD into located \[EF] the value D|
|0x40|LD A, \[n16]|3|--|n16|LOAD A with the value found at \[n16]|
|0x41|LD B, \[n16]|3|--|n16|LOAD B with the value found at \[n16]|
|0x42|LD C, \[n16]|3|--|n16|LOAD C with the value found at \[n16]|
|0x43|LD D, \[n16]|3|--|n16|LOAD D with the value found at \[n16]|
|0x44|LD E, \[n16]|3|--|n16|LOAD E with the value found at \[n16]|
|0x45|LD F, \[n16]|3|--|n16|LOAD F with the value found at \[n16]|
|0x46|LD \[CD], n8|2|--|n8|LOAD into location \[CD] the value n8|
|0x47|LD \[CD], \[EF]|1|--||LOAD into location \[CD] the value at location \[EF]|
|0x48|LD CD, n16|1|--||LOAD n16 value into CD|
|0x49|LD CD, EF|1|--||LOAD value of EF into CD|
|0x4A|LD EF, n16|1|--||LOAD n16 value into EF|
|0x4B|LD EF, CD|1|--||LOAD value of CD into EF|
|0x4C|LD \[CD], \[n16]|3|--||LOAD into location \[CD] the value at location \[n16]|
|0x4D|LD \[EF], \[n16]|3|--||LOAD into location \[EF] the value at location \[n16]|
|0x4E|LD \[EF], n8|2|--|n8|LOAD into location \[EF] the value n8|
|0x4F|LD \[EF], \[CD]|1|--||LOAD into location \[EF] the value at location \[CD]|
|0x50|ADD A, A|1|--||Add the value of A into A|
|0x51|ADD A, B|1|--||Add the value of B into A|
|0x52|ADD A, C|1|--||Add the value of C into A|
|0x53|ADD A, D|1|--||Add the value of D into A|
|0x54|ADD A, E|1|--||Add the value of E into A|
|0x55|ADD A, F|1|--||Add the value of F into A|
|0x56|ADD A, \[CD]|1|--||Add the value at \[CD] into A|
|0x57|ADD A, \[EF]|1|--||Add the value at \[EF] into A|
|0x58|ADD CD, CD|1|--||Add the value of CD into CD|
|0x59|ADD CD, EF|1|--||Add the value of EF into CD|
|0x5A|ADD CD, n16|3|--||Add teh value of n16 into CD|
|0x5B|---|1|--||---|
|0x5C|ADD EF, CD|1|--||Add the value of CD into EF|
|0x5D|ADD EF, EF|1|--||Add the value of EF into EF|
|0x5E|ADD EF, n16|3|--||Add the value of n16 into EF|
|0x5F|---|1|--||---|
|0x60|SUB A, A|1|--||Subtract the value of A into A|
|0x61|SUB A, B|1|--||Subtract the value of B into A|
|0x62|SUB A, C|1|--||Subtract the value of C into A|
|0x63|SUB A, D|1|--||Subtract the value of D into A|
|0x64|SUB A, E|1|--||Subtract the value of E into A|
|0x65|SUB A, F|1|--||Subtract the value of F into A|
|0x66|SUB A, \[CD]|1|--||Subtract the value at \[CD] into A|
|0x67|SUB A, \[EF]|1|--||Subtract the value at \[EF] into A|
|0x68|SUB CD, CD|1|--||Subtract the value of CD into CD|
|0x69|SUB CD, EF|1|--||Subtract the value of EF into CD|
|0x6A|SUB CD, n16|3|--||Subtract teh value of n16 into CD|
|0x6B|---|1|--||---|
|0x6C|SUB EF, CD|1|--||Subtract the value of CD into EF|
|0x6D|SUB EF, EF|1|--||Subtract the value of EF into EF|
|0x6E|SUB EF, n16|3|--||Subtract the value of n16 into EF|
|0x6F|---|1|--||---|
|0x70|AND A, A|1|--||AND the value of A into A|
|0x71|AND A, B|1|--||AND the value of B into A|
|0x72|AND A, C|1|--||AND the value of C into A|
|0x73|AND A, D|1|--||AND the value of D into A|
|0x74|AND A, E|1|--||AND the value of E into A|
|0x75|AND A, F|1|--||AND the value of F into A|
|0x76|AND A, \[CD]|1|--||AND the value at \[CD] into A|
|0x77|AND A, \[EF]|1|--||AND the value at \[EF] into A|
|0x78|OR A, A|1|--||OR the value of A into A|
|0x79|OR A, B|1|--||OR the value of B into A|
|0x7A|OR A, C|1|--||OR the value of C into A|
|0x7B|OR A, D|1|--||OR the value of D into A|
|0x7C|OR A, E|1|--||OR the value of E into A|
|0x7D|OR A, F|1|--||OR the value of F into A|
|0x7E|OR A, \[CD]|1|--||OR the value at \[CD] into A|
|0x7F|OR A, \[EF]|1|--||OR the value at \[EF] into A|
|0x80|XOR A, A|1|--||XOR the value of A into A|
|0x81|XOR A, B|1|--||XOR the value of B into A|
|0x82|XOR A, C|1|--||XOR the value of C into A|
|0x83|XOR A, D|1|--||XOR the value of D into A|
|0x84|XOR A, E|1|--||XOR the value of E into A|
|0x85|XOR A, F|1|--||XOR the value of F into A|
|0x86|XOR A, \[CD]|1|--||XOR the value at \[CD] into A|
|0x87|XOR A, \[EF]|1|--||XOR the value at \[EF] into A|
|0x88|ADD A, n8|2|--||Add the value of n8 into A|
|0x89|SUB A, n8|2|--||Subtract the value of n8 into A|
|0x8A|AND A, n8|2|--||AND the value of n8 into A|
|0x8B|OR A, n8|2|--||OR the value of n8 into A|
|0x8C|XOR A, n8|2|--||XOR the value of n8 into A|
|0x8D|---|1|--||---|
|0x8E|---|1|--||---|
|0x8F|---|1|--||---|
|0x90|INC A|1|--||Increment the value of A|
|0x91|INC B|1|--||Increment the value of B|
|0x92|INC C|1|--||Increment the value of C|
|0x93|INC D|1|--||Increment the value of D|
|0x94|INC E|1|--||Increment the value of E|
|0x95|INC F|1|--||Increment the value of F|
|0x96|INC CD|1|--||Increment the value of CD|
|0x97|INC EF|1|--||Increment the value of EF|
|0x98|INC \[CD]|1|--||Increment the value at \[CD]|
|0x99|INC \[EF]|1|--||Increment the value at \[CD]|
|0x9A|INC \[n16]|3|--||Increment the value at \[n16]|
|0x9B|---|1|--||---|
|0x9C|---|1|--||---|
|0x9D|---|1|--||---|
|0x9E|---|1|--||---|
|0x9F|---|1|--||---|
|0xA0|DEC A|1|--||Decrement the value of A|
|0xA1|DEC B|1|--||Decrement the value of B|
|0xA2|DEC C|1|--||Decrement the value of C|
|0xA3|DEC D|1|--||Decrement the value of D|
|0xA4|DEC E|1|--||Decrement the value of E|
|0xA5|DEC F|1|--||Decrement the value of F|
|0xA6|DEC CD|1|--||Decrement the value of CD|
|0xA7|DEC EF|1|--||Decrement the value of EF|
|0xA8|DEC \[CD]|1|--||Decrement the value at \[CD]|
|0xA9|DEC \[EF]|1|--||Decrement the value at \[CD]|
|0xAA|DEC \[n16]|3|--||Decrement the value at \[n16]|
|0xAB|---|1|--||---|
|0xAC|---|1|--||---|
|0xAD|---|1|--||---|
|0xAE|---|1|--||---|
|0xAF|---|1|--||---|
|0xB0|CP A, n8|2|--||Compare n8 to A|
|0xB1|CP A, B|1|--||Compare B to A|
|0xB2|CP A, C|1|--||Compare C to A|
|0xB3|CP A, D|1|--||Compare D to A|
|0xB4|CP A, E|1|--||Compare E to A|
|0xB5|CP A, F|1|--||Compare F to A|
|0xB6|CP A, \[CD]|1|--||Compare the value at \[CD] to A|
|0xB7|CP A, \[EF]|1|--||Compare the value at \[EF] to A|
|0xB8|BAND A, n8|2|--||Bitwise AND n8 to A|
|0xB9|BAND A, B|1|--||Bitwise AND B to A|
|0xBA|BAND A, C|1|--||Bitwise AND C to A|
|0xBB|BAND A, D|1|--||Bitwise AND D to A|
|0xBC|BAND A, E|1|--||Bitwise AND E to A|
|0xBD|BAND A, F|1|--||Bitwise AND F to A|
|0xBE|BAND A, \[CD]|1|--||Bitwise AND the value at \[CD] to A|
|0xBF|BAND A, \[EF]|1|--||Bitwise AND the value at \[EF] to A|
|0xC0|BOR A, n8|2|--||Bitwise OR n8 to A|
|0xC1|BOR A, B|1|--||Bitwise OR B to A|
|0xC2|BOR A, C|1|--||Bitwise OR C to A|
|0xC3|BOR A, D|1|--||Bitwise OR D to A|
|0xC4|BOR A, E|1|--||Bitwise OR E to A|
|0xC5|BOR A, F|1|--||Bitwise OR F to A|
|0xC6|BOR A, \[CD]|1|--||Bitwise OR the value at \[CD] to A|
|0xC7|BOR A, \[EF]|1|--||Bitwise OR the value at \[EF] to A|
|0xC8|JMP CD|1|--||JUMP to address defined at CD|
|0xC9|JMP EF|1|--||JUMP to address defined at EF|
|0xCA|JMP \[CD]|1|--||JUMP to address defined at the value pointed at \[CD]|
|0xCB|JMP \[EF]|1|--||JUMP to address defined at the value pointed at \[EF]|
|0xCC|JMP Z, \[n16]|1|--||JUMP to address defined at the value pointed at \[n16] if zero is set|
|0xCD|JMP NZ, \[n16]|1|--||JUMP to address defined at the value pointed at \[n16] if zero is not set|
|0xCE|JMP C, \[n16]|1|--||JUMP to address defined at the value pointed at \[n16] if carry is set|
|0xCF|JMP NC, \[n16]|1|--||JUMP to address defined at the value pointed at \[n16] if carry is not set|
|0xD0|LSH A|1|--||Left shift rotate A|
|0xD1|RSH A|1|--||Right shift rotate A|
|0xD2|LSH CD|1|--||Left shift rotate CD|
|0xD3|RSH CD|1|--||Right shift rotate CD|
|0xD4|LSH EF|1|--||Left shift rotate EF|
|0xD5|RSH EF|1|--||Right shift rotate EF|
|0xD6|JMP n16|3|--||JUMP to address n16|
|0xD7|JMP \[n16]|3|--||JUMP to the address defined at the value pointed at \[n16]|
|0xD8|JMP Z, CD|1|--||JUMP to address defined at CD if zero is set|
|0xD9|JMP NZ, CD|1|--||JUMP to address defined at CD if zero is not set|
|0xDA|JMP C, CD|1|--||JUMP to address defined at CD if carry is set|
|0xDB|JMP NC, CD|1|--||JUMP to address defined at CD if carry is not set|
|0xDC|JMP Z, EF|1|--||JUMP to address defined at EF if zero is set|
|0xDD|JMP NZ, EF|1|--||JUMP to address defined at EF if zero is not set|
|0xDE|JMP C, EF|1|--||JUMP to address defined at EF if carry is set|
|0xDF|JMP NC, EF|1|--||JUMP to address defined at EF if carry is not set|
|0xE0|CALL CD|1|--||CALL the method starting at CD|
|0xE1|CALL EF|1|--||CALL the method starting at EF|
|0xE2|CALL n16|3|--||CALL the method starting at n16|
|0xE3|CALL \[n16]|3|--||CALL the method starting at the address defined at the value pointed at \[n16]|
|0xE4|CALL Z, CD|1|--||CALL the method starting at CD if zero is set|
|0xE5|CALL NZ, CD|1|--||CALL the method starting at CD if zero is not set|
|0xE6|CALL C, CD|1|--||CALL the method starting at CD if carry is set|
|0xE7|CALL NC, CD|1|--||CALL the method starting at CD if carry is not set|
|0xE8|CALL Z, EF|1|--||CALL the method starting at EF if zero is set|
|0xE9|CALL NZ, EF|1|--||CALL the method starting at EF if zero is not set|
|0xEA|CALL C, EF|1|--||CALL the method starting at EF if carry is set|
|0xEB|CALL NC, EF|1|--||CALL the method starting at EF if carry is not set|
|0xEC|CALL Z, n16|3|--||CALL the method starting at n16 if zero is set|
|0xED|CALL NZ, n16|3|--||CALL the method starting at n16 if zero is not set|
|0xEE|CALL C, n16|3|--||CALL the method starting at n16 if carry is set|
|0xEF|CALL NC, n16|3|--||CALL the method starting at n16 if carry is not set|
|0xF0|CALL Z, \[n16]|3|--||CALL the method starting at \[n16] if zero is set|
|0xF1|CALL NZ, \[n16]|3|--||CALL the method starting at \[n16] if zero is not set|
|0xF2|CALL C, \[n16]|3|--||CALL the method starting at \[n16] if carry is set|
|0xF3|CALL NC, \[n16]|3|--||CALL the method starting at \[n16] if carry is not set|
|0xF4|PUSH CD|1|--||PUSH the value of CD into the stack|
|0xF5|PUSH EF|1|--||PUSH the value of EF into the stack|
|0xF6|POP CD|1|--||POP the value on the stack into CD|
|0xF7|POP EF|1|--||PIP the value on the stack into EF|
|0xF8|RET|1|--||Return subroutine|
|0xF9|RETI|1|--||Return interrupt|
|0xFA|RET Z|1|--||Return if zero is set|
|0xFB|RET NZ|1|--||Return if non-zero is set|
|0xFC|RET C|1|--||Return if carry is set|
|0xFD|RET NC|1|--||return if non-carry is set|
|0xFE|---|1|--||---|
|0xFF|HALT|1|--||Halt all further processing|
