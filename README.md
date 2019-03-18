# Unnamed Fantasy Portable Console

The idea of this project is to design in code a Fantasy Computer.  In this case, an 8-bit handheld console not unlike the original GameBoy Color.

The specs for this fantasy console should be as follows

* 8-bit instructions
* 16-bit address space (i.e. 64k of RAM)
* Graphics
    * Color display
    * 160 x 160 pixel resolution
    * No direct video access
    * 8x8 pixel tiles
    * Sprite support
        * Up to 20 sprites
        * Max 10 sprites in a line
        * 8x8, 8x16, 16x8 and 16x16 pixel sprites
* Audio
    * 4 channels
    * Square, Triangle, sawtooth and noise
* "Cartridge" slot
    * Code just loads into fixed memory
    * Bank switching to have games up to 4MB in size
* Controller
    * Directional Pad
    * A, B, X, Y, L and R buttons
    * Start & Select

The idea of these specs is to limit the design of the system, obviously.  It's intended to simulate something that might have come out in the mid to late 90's.
