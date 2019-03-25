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
|0x48|XXX|1|--||xxxx|
|0x49|XXX|1|--||xxxx|
|0x4A|XXX|1|--||xxxx|
|0x4B|XXX|1|--||xxxx|
|0x4C|XXX|1|--||xxxx|
|0x4D|XXX|1|--||xxxx|
|0x4E|XXX|1|--||xxxx|
|0x4F|XXX|1|--||xxxx|
|0x50|XXX|1|--||xxxx|
|0x51|XXX|1|--||xxxx|
|0x52|XXX|1|--||xxxx|
|0x53|XXX|1|--||xxxx|
|0x54|XXX|1|--||xxxx|
|0x55|XXX|1|--||xxxx|
|0x56|XXX|1|--||xxxx|
|0x57|XXX|1|--||xxxx|
|0x58|XXX|1|--||xxxx|
|0x59|XXX|1|--||xxxx|
|0x5A|XXX|1|--||xxxx|
|0x5B|XXX|1|--||xxxx|
|0x5C|XXX|1|--||xxxx|
|0x5D|XXX|1|--||xxxx|
|0x5E|XXX|1|--||xxxx|
|0x5F|XXX|1|--||xxxx|
|0x60|XXX|1|--||xxxx|
|0x61|XXX|1|--||xxxx|
|0x62|XXX|1|--||xxxx|
|0x63|XXX|1|--||xxxx|
|0x64|XXX|1|--||xxxx|
|0x65|XXX|1|--||xxxx|
|0x66|XXX|1|--||xxxx|
|0x67|XXX|1|--||xxxx|
|0x68|XXX|1|--||xxxx|
|0x69|XXX|1|--||xxxx|
|0x6A|XXX|1|--||xxxx|
|0x6B|XXX|1|--||xxxx|
|0x6C|XXX|1|--||xxxx|
|0x6D|XXX|1|--||xxxx|
|0x6E|XXX|1|--||xxxx|
|0x6F|XXX|1|--||xxxx|
|0x70|XXX|1|--||xxxx|
|0x71|XXX|1|--||xxxx|
|0x72|XXX|1|--||xxxx|
|0x73|XXX|1|--||xxxx|
|0x74|XXX|1|--||xxxx|
|0x75|XXX|1|--||xxxx|
|0x76|XXX|1|--||xxxx|
|0x77|XXX|1|--||xxxx|
|0x78|XXX|1|--||xxxx|
|0x79|XXX|1|--||xxxx|
|0x7A|XXX|1|--||xxxx|
|0x7B|XXX|1|--||xxxx|
|0x7C|XXX|1|--||xxxx|
|0x7D|XXX|1|--||xxxx|
|0x7E|XXX|1|--||xxxx|
|0x7F|XXX|1|--||xxxx|
|0x80|XXX|1|--||xxxx|
|0x81|XXX|1|--||xxxx|
|0x82|XXX|1|--||xxxx|
|0x83|XXX|1|--||xxxx|
|0x84|XXX|1|--||xxxx|
|0x85|XXX|1|--||xxxx|
|0x86|XXX|1|--||xxxx|
|0x87|XXX|1|--||xxxx|
|0x88|XXX|1|--||xxxx|
|0x89|XXX|1|--||xxxx|
|0x8A|XXX|1|--||xxxx|
|0x8B|XXX|1|--||xxxx|
|0x8C|XXX|1|--||xxxx|
|0x8D|XXX|1|--||xxxx|
|0x8E|XXX|1|--||xxxx|
|0x8F|XXX|1|--||xxxx|
|0x90|XXX|1|--||xxxx|
|0x91|XXX|1|--||xxxx|
|0x92|XXX|1|--||xxxx|
|0x93|XXX|1|--||xxxx|
|0x94|XXX|1|--||xxxx|
|0x95|XXX|1|--||xxxx|
|0x96|XXX|1|--||xxxx|
|0x97|XXX|1|--||xxxx|
|0x98|XXX|1|--||xxxx|
|0x99|XXX|1|--||xxxx|
|0x9A|XXX|1|--||xxxx|
|0x9B|XXX|1|--||xxxx|
|0x9C|XXX|1|--||xxxx|
|0x9D|XXX|1|--||xxxx|
|0x9E|XXX|1|--||xxxx|
|0x9F|XXX|1|--||xxxx|
|0xA0|XXX|1|--||xxxx|
|0xA1|XXX|1|--||xxxx|
|0xA2|XXX|1|--||xxxx|
|0xA3|XXX|1|--||xxxx|
|0xA4|XXX|1|--||xxxx|
|0xA5|XXX|1|--||xxxx|
|0xA6|XXX|1|--||xxxx|
|0xA7|XXX|1|--||xxxx|
|0xA8|XXX|1|--||xxxx|
|0xA9|XXX|1|--||xxxx|
|0xAA|XXX|1|--||xxxx|
|0xAB|XXX|1|--||xxxx|
|0xAC|XXX|1|--||xxxx|
|0xAD|XXX|1|--||xxxx|
|0xAE|XXX|1|--||xxxx|
|0xAF|XXX|1|--||xxxx|
|0xB0|XXX|1|--||xxxx|
|0xB1|XXX|1|--||xxxx|
|0xB2|XXX|1|--||xxxx|
|0xB3|XXX|1|--||xxxx|
|0xB4|XXX|1|--||xxxx|
|0xB5|XXX|1|--||xxxx|
|0xB6|XXX|1|--||xxxx|
|0xB7|XXX|1|--||xxxx|
|0xB8|XXX|1|--||xxxx|
|0xB9|XXX|1|--||xxxx|
|0xBA|XXX|1|--||xxxx|
|0xBB|XXX|1|--||xxxx|
|0xBC|XXX|1|--||xxxx|
|0xBD|XXX|1|--||xxxx|
|0xBE|XXX|1|--||xxxx|
|0xBF|XXX|1|--||xxxx|
|0xC0|XXX|1|--||xxxx|
|0xC1|XXX|1|--||xxxx|
|0xC2|XXX|1|--||xxxx|
|0xC3|XXX|1|--||xxxx|
|0xC4|XXX|1|--||xxxx|
|0xC5|XXX|1|--||xxxx|
|0xC6|XXX|1|--||xxxx|
|0xC7|XXX|1|--||xxxx|
|0xC8|XXX|1|--||xxxx|
|0xC9|XXX|1|--||xxxx|
|0xCA|XXX|1|--||xxxx|
|0xCB|XXX|1|--||xxxx|
|0xCC|XXX|1|--||xxxx|
|0xCD|XXX|1|--||xxxx|
|0xCE|XXX|1|--||xxxx|
|0xCF|XXX|1|--||xxxx|
|0xD0|XXX|1|--||xxxx|
|0xD1|XXX|1|--||xxxx|
|0xD2|XXX|1|--||xxxx|
|0xD3|XXX|1|--||xxxx|
|0xD4|XXX|1|--||xxxx|
|0xD5|XXX|1|--||xxxx|
|0xD6|XXX|1|--||xxxx|
|0xD7|XXX|1|--||xxxx|
|0xD8|XXX|1|--||xxxx|
|0xD9|XXX|1|--||xxxx|
|0xDA|XXX|1|--||xxxx|
|0xDB|XXX|1|--||xxxx|
|0xDC|XXX|1|--||xxxx|
|0xDD|XXX|1|--||xxxx|
|0xDE|XXX|1|--||xxxx|
|0xDF|XXX|1|--||xxxx|
|0xE0|XXX|1|--||xxxx|
|0xE1|XXX|1|--||xxxx|
|0xE2|XXX|1|--||xxxx|
|0xE3|XXX|1|--||xxxx|
|0xE4|XXX|1|--||xxxx|
|0xE5|XXX|1|--||xxxx|
|0xE6|XXX|1|--||xxxx|
|0xE7|XXX|1|--||xxxx|
|0xE8|XXX|1|--||xxxx|
|0xE9|XXX|1|--||xxxx|
|0xEA|XXX|1|--||xxxx|
|0xEB|XXX|1|--||xxxx|
|0xEC|XXX|1|--||xxxx|
|0xED|XXX|1|--||xxxx|
|0xEE|XXX|1|--||xxxx|
|0xEF|XXX|1|--||xxxx|
|0xF0|XXX|1|--||xxxx|
|0xF1|XXX|1|--||xxxx|
|0xF2|XXX|1|--||xxxx|
|0xF3|XXX|1|--||xxxx|
|0xF4|XXX|1|--||xxxx|
|0xF5|XXX|1|--||xxxx|
|0xF6|XXX|1|--||xxxx|
|0xF7|XXX|1|--||xxxx|
|0xF8|XXX|1|--||xxxx|
|0xF9|XXX|1|--||xxxx|
|0xFA|XXX|1|--||xxxx|
|0xFB|XXX|1|--||xxxx|
|0xFC|XXX|1|--||xxxx|
|0xFD|XXX|1|--||xxxx|
|0xFE|XXX|1|--||xxxx|
|0xFF|XXX|1|--||xxxx|
