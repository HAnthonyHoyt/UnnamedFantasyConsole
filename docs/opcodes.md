# Opcodes

A generalized list of opcodes that we might need

## Details

* r8 = 8-bit registers (A, B, C, D, E, F)
* r16 = 16-bit registers (CD, EF)
* n8 = 8-bit integer constant
* n16 = 16-bit integer constant
* \[x\] = Value referenced at location x.  x can be a r16 or a n16
* cc = Conditional codes
    * Z = True if ZERO is set
    * NZ = True if ZERO is not set
    * C = True if CARRY is set
    * NC = True if CARRY is not set

## How to read opcodes

&lt;code&gt; &lt;destination&gt; &lt;source&gt;

code = The actual name of the code, usually desribes the action being taken place
destination = Usually where the data is finally going.
source = Usually what's going to alter the destination.

For example `ADD r8, n8` means "Add the value n8 to r8 and store it in r8"

## Thoughts

Due to only having 256 maximum opcodes available and trying to reduce the number
of extra bytes per opcode, I've opted to go with the following limitations

* A is the only 8-bit register wtih all arithmetic and logic available to it
* CD and EF are intended to be 'destination' and 'source' registers most of the time

## Actual codes

### 8-bit Arithmetic

#### Add a value

* ADD A, n8
* ADD A, r8
* ADD A, \[n16]
* ADD A, \[r16]
* ADD r16, n16
* ADD r16, r16
* ADD r16, \[n16]
* ADD r16, \[r16]

#### Subtract a value

* SUB A, n8
* SUB A, r8
* SUB A, \[n16]
* SUB A, \[r16]
* SUB r16, n16
* SUB r16, r16
* SUB r16, \[n16]
* SUB r16, \[r16]

#### Increments

* INC r8
* INC r16
* INC \[r16]
* INC \[n16]
* DEC r8
* DEC r16
* DEC \[r16]
* DEC \[n16]

#### Companions

* CP A, r8
* CP A, \[r16]
* CP A, \[n16]
* CP r16, r16
* CP r16, \[r16]
* CP r16, \[n16]
    * All will set "ZERO" to 1 if True

#### Bitewise

* AND r8, r8
* AND r8, n8
* AND r8, \[r16]
* AND r8, \[n16]
* AND r16, r16
* AND r16, n16
* OR r8, r8
* OR r8, n8
* OR r8, \[r16]
* OR r8, \[n16]
* OR r16, r16
* OR r16, n16
* XOR r8, r8
* XOR r8, n8
* XOR r8, \[r16]
* XOR r8, \[n16]
* XOR r16, r16
* XOR r16, n16

### Bitwise left shift

* LSH A
* LSH r16

### Bitwise right shift

* RSH A
* RSH r16

### Loading

* LD r8, r8
* LD r8, n8
* LD r8, \[r16]
* LD r8, \[n16]
* LD r16, r16
* LD r16, n16
* LD \[r16], r8
* LD \[r16], n8
* LD \[n16], r8
* LD \[n16], n8

### Jumps and subroutines

* CALL n16
* CALL r16
* CALL \[n16]
* CALL cc, r16
* CALL cc, \[n16]
* JP r16
* JP n16
* JP cc, r16
* JP cc, n16
* RET
* RET cc

### Stack instructions

* PUSH n8
* PUSH r8
* PUSH n16
* PUSH r16
* POP r8
* POP r16
