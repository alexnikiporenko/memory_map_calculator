def to_hex(dec_int):
    return (hex(int(dec_int))[2:]).upper() + "h"

def memory_map_calculator(total_kb, top, *args): # arguments are in kilobytes
    tot_mem = "\nTotal memory = " + str(total_kb) + "kb. Hex = " + to_hex(total_kb * 1024 - 1)
    counter = 0
    memory = 0
    unused_size = total_kb - sum(args)
    if top != 0:
        unused_size = unused_size - sum(top)
    for arg in args:
        counter += 1
        print("\nMemory segment " + str(counter) + ". Size = " + str(arg) + "kb.\nFirst memory location = " + to_hex(memory))
        memory += (arg * 1024 - 1)
        print("Last memory location = " + to_hex(memory))
        memory += 1
    print("\nUnused memory. Size = " + str(unused_size) + "kb.\nFirst memory location = " + to_hex(memory))
    if top != 0:
        top_segments = []
        counter2 = 0
        memory2 = total_kb * 1024
        for n in top:
            top_segments.append("Last memory location = " + to_hex(memory2 - 1))
            memory2 -= n * 1024
            top_segments.append("\nTop segment " + str(len(top) - counter2) + ". Size = " + str(n) + "kb.\nFirst memory location = " + to_hex(memory2))
            counter2 += 1
        top_segments.append("Unused memory. Last memory location = " + to_hex(memory2 - 1))
        while len(top_segments) > 0:
            print(top_segments.pop())
    print(tot_mem)


# MEMORY MAP CALCULATOR
# to calculate memory map in hex values, run the below function with the following arguments:
# memory_map_calculator(total memory, [top memory mappings], other memory mappings)
# if there are no top memory mappings, replace the list with a 0

memory_map_calculator(1024, [0.25, 0.25, 0.25, 0.25], 128, 512) # arguments are in kilobytes
