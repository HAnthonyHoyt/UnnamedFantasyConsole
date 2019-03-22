# Opcodes

A generalized list of opcodes that we might need

r8 = Any of the 8-bit registers (A, B, C, D, E, F, G, H)
r16 = Any of the 16-bit registers (AB, CD, EF, GH)
n8 = 8-bit integer constant
n16 = 16-bit integer constant
n8 = static value
[x] = Value referenced at location x.  x can be a r16 or a n16
cc = Conditional codes
    Z = True if ZERO is set
    NZ = True if ZERO is not set
    C = True if CARRY is set
    NC = True if CARRy is not set
[r] = Memory address from register
[s] = Specific memory address

How to read opcodes

<code> <destination> <source>

code = The actual name of the code, usually desribes the action being taken place
destination = Usually where the data is finally going.
source = Usually what's going to alter the destination.

For example `ADD r8, n8` means "Add the value n8 to r8 and store it in r8"

## Quick thoughts
Now, there maybe way too many opcodes here.  It seems like with systems like the GB, all the real arithmetic took place on register A, and maybe that's good enough because with all the extra 'opcodes', we're losing space to actions we actually might need.  Plus, some might be really unrealistic with a 'real' processor.  

## Actual codes

### 8-bit Arithmetic

Add a value
ADD r8, n8
ADD r8, r8
ADD r16, n16
ADD r16, r16
ADD r8, [n16]
ADD r8, [r16]
ADD r16, [n16]
ADD r16, [r16]

Subtract a value
SUB r8, n8
SUB r8, r8
SUB r16, n16
SUB r16, r16
SUB r8, [n16]
SUB r8, [r16]
SUB r16, [n16]
SUB r16, [r16]

Increments
INC r8
INC r16
DEC r8
DEC r16

Companions
CP r8, r8
CP r16, r16
CP r8, [r16]
CP r8, [n16]
CP r16, [r16]
CP r16, [n16]
* All will set "Z" to 1 if True

Bitewise
AND r8, r8
AND r8, n8
AND r16, r16
AND r16, n16
AND r8, [r16]
AND r8, [n16]

OR r8, r8
OR r8, n8
OR r16, r16
OR r16, n16
OR r8, [r16]
OR r8, [n16]

XOR r8, r8
XOR r8, n8
XOR r16, r16
XOR r16, n16
XOR r8, [r16]
XOR r8, [n16]

# Bitwise test the destination with source.  Set Z based on result, don't modify any values
BIT r8, r8
BIT r8, n8
BIT r16, r16
BIT r16, n16
BIT r8, [r16]
BIT r8, [n16]

# Bitwise left shift
LSH r8
LSH r16

# Bitwise right shift
RSH r8
RSH r16

### Loading

LD r8, r8
LD r8, n8
LD r16, r16
LD r16, n16
LD r8, [r16]
LD r8, [n16]
LD [r16], r8
LD [r16], n8
LD [n16], r8
LD [n16], n8

### Jumps and subroutines
CALL n16
CALL [n16]
CALL r16
JP r16
JP n16
RET
RET cc
RET
