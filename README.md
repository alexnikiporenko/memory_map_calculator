# memory_map_calculator
A python function to convert decimal values to hex, and calculate memory map values.

Can be used to solve the questions such as:
"Draw a memory map for a system with 1MBytes of memory, 128K ROM, 512K ram and three IO devices with 8 registers each mapped to a 1k block with 4 IO slots (only three used)."

To solve the above question, run the function with the following values: `memory_map_calculator(1024, [0.25, 0.25, 0.25, 0.25], 128, 512)`

The output will be:

`Memory segment 1. Size = 128kb.`<br>
`First memory location = 0h`<br>
`Last memory location = 1FFFFh`

`Memory segment 2. Size = 512kb.`<br>
`First memory location = 20000h`<br>
`Last memory location = 9FFFFh`

`Unused memory. Size = 383.0kb.`<br>
`First memory location = A0000h`<br>
`Unused memory. Last memory location = FFBFFh`

`Top segment 1. Size = 0.25kb.`<br>
`First memory location = FFC00h`<br>
`Last memory location = FFCFFh`

`Top segment 2. Size = 0.25kb.`<br>
`First memory location = FFD00h`<br>
`Last memory location = FFDFFh`

`Top segment 3. Size = 0.25kb.`<br>
`First memory location = FFE00h`<br>
`Last memory location = FFEFFh`

`Top segment 4. Size = 0.25kb.`<br>
`First memory location = FFF00h`<br>
`Last memory location = FFFFFh`

`Total memory = 1024kb. Hex = FFFFFh`
