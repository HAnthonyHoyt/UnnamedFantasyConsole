# Design notes

Each class is intended to represent a board, chip or just a basic component.  Here are some thoughts about each of them.  Now, I'm not a hardware designer.  As a matter of fact, I have no idea what I'm doing here.  I'm creating a fantasy computer based on how I assume some of this works or copying ideas from other real life systems just because they sound interesting. So if some of my ideas don't make sense or are completely bogus, then let do let me know. I would like this to simulate something vaugly realistic but it is just a Fantasy Computer.  Just something in my head.

## Clock

The clock object simulates the crystal on the chip that would be use to send pulses to all the compontents to let them know they can act for one cycle.  Eventually I would like this to run at something like 4MHz to simulate the speed of a possible real world machine of the era.

## CPU

So we're talking about an 8-bit processor, so at the moment I would like to cap it at 256 instructions.  Looks like the original Gameboy had almost double that due to some interesting bit/shift instructions but at the moment I'm not going to dive into that.  Lets go with eight 8-bit registers (A-H), a stack pointer (SP), a program counter (PC), a flag register (Maybe named FL?).  Maybe the main registers could be paired up for some 16-bit addressing as well if we need to.  So AB, CD, EF, and GH.  For now, all instructions take 1 clock cycle to complete.  In the future, it would obviously make more sense that some would take more than others but for now, let's just keep it easy.

## GPU

The graphics object will simulate the graphics chip and the video display.  The system will have a 120 x 120 pixel display area with support for some kind of limitation on color graphics (Maybe 256?).  The GameBoy also used tiles to display everything but the sprites and sprites had some really hard limitations.  So my feeling is this, let's take direct video access off the equasion.  So the system renders everything in tiles.  Tiles are 8 pixels square but you can have sprites composed of multiple tiles.  Be it a 1x1 tile sprite, 1x2, 2x1 or 2x2.  It just feels that a 16x16 tile sprite would cover most games.  For the others, they can combine tiles like you see already with lots of GameBoy games.  We'll allow up to 20 sprites and also have the 10 sprites per line limitation.  Initally, I wanted to go with a 160 x 160 display.  This would have meant for a clean 20 x 20 tiles display.  I'm tempted to go with perhaps a more rectangular display with something like 160 x 120 (Based off a display I have for my Raspberry Pi), but then we have a 20 x 15 tile display.  The original GBC was 20x18, so I would like to stay in that range.

## Sound

The sound chip should be pretty basic. 4 voices.  Each voice can have one of 4 different sound waves, volume, pitch, length, on/off flag, ... Maybe flags for things like decay, or frequency sweep?

## Input

It takes the current input, and sets the bits in memory to the current values.  That's about it.  At some point, I would like to have it support 4 player games but for now, this if fine.

## Cartridge slot

So by default, the system will only have a 16bit address space, so that's 64KB.  Since a lot of games from that era tend to have bank switching, we can include that here as well.  Let's have a theoretical limit of 4MB but it might make sense that there's no real limit here