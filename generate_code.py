def generate_asm(instructions):
    """根据指令列表生成汇编代码"""
    asm_code = []
    for instruction in instructions:
        if len(instruction.inputs) == 1:  # 处理只包含一个输入的指令
            asm_code.append(f"    {instruction.name} {instruction.output[0]}, {instruction.inputs[0]}")
        else:
            asm_code.append(f"    {instruction.name} {instruction.output[0]}, {', '.join(instruction.inputs)}")
    return "\n".join(asm_code)
