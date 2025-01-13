# Barbusoft 9000

The Barbusoft 9000 is a computer built in [Logism-evolution](https://github.com/logisim-evolution/logisim-evolution) capable of interpreting 16-bit instructions. It has 4 general purpose registers, 2 RAMs (one to store instructions and the other to store runtime data), and an LED display. A custom compiler translates assembly code into image files that can be loaded and read by the computer. 

The computer was developed by [@JacobBarbulescu](https://www.github.com/JacobBarbulescu) for the Computer Architecture and Organization course offered at Stevens Institute of Technology.

## Features

- Custom assembly language (.barb) and compiler to write custom programs for the computer
  - Addition, subtraction, loading and storing from RAM, setting registers, and displaying registers supported
  - Support for immediate numbers
  - Comments/whitespace allowed
- Two RAMs
  - One stores a program's instructions
  - The other stores data values
- 4 general purpose registers
- LED display
- A manual detailing the design of the computer and how to use it
    
## Using the computer

The computer is built in [Logism-evolution](https://github.com/logisim-evolution/logisim-evolution) and as such requires the program to load the computer.

A [manual](Barbusoft%20Manual.pdf) is provided with the computer's files that outlines the computer's specifications, capabilites, and usage. Refer to this manual in order to write, compile, and run your own programs on the computer!

## Installation

[Click here](https://downgit.github.io/#/home?url=https://github.com/JacobBarbulescu/Barbusoft) to download the source files for the computer. Then, open the Barbusoft.circ file in [Logism-evolution](https://github.com/logisim-evolution/logisim-evolution) to "turn on" the computer.
