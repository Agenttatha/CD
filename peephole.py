def algebraic_simplification(instructions):
    new_instructions = []
    for instruction in instructions:
        instruction = instruction.split(' ')
        op = instruction[0]
        operands = instruction[1].split(',')
        if op in ['LD', 'ST']:
            new_instructions.append(' '.join(instruction))
        elif op == 'ADD' and operands[1] == '0' or operands[2] == '0':
            new_instructions.append('MOV '+operands[0]+','+(operands[1] if operands[1] != '0' else operands[2]))
        elif op == 'SUB' and operands[2] == '0':
            new_instructions.append('MOV '+operands[0]+','+operands[1])
        elif op == 'MUL' and operands[1] == '1' or operands[2] == '1':
            new_instructions.append('MOV '+operands[0]+','+(operands[1] if operands[1] != '1' else operands[2]))
        elif op == 'DIV' and operands[2] == '1':
            new_instructions.append('MOV '+operands[0]+','+operands[1])
        else:
            new_instructions.append(' '.join(instruction))
    return new_instructions
# Example instructions
instructions = ["LD R0,b", "ADD R1,R0,0","ST a,R1", "LD R0,a", "ADD R1,0,R0", "ST d,R1"]
print("Original Instructions:", instructions)
new_instructions = algebraic_simplification(instructions)
print("Optimized Instructions:", new_instructions)
