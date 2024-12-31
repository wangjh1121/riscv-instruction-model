from random import choice
from instructions import Instruction
from d_extension import d_instruction_properties
from v_extension import v_instruction_properties
from typing import List

def generate_registers_from_types(input_type: str, output_type: str, register_count: int = 7) -> dict:
    """
    根据输入和输出类型生成相应的寄存器名。
    
    参数:
    input_type (str): 输入寄存器的类型
    output_type (str): 输出寄存器的类型
    register_count (int): 每个类型的寄存器数量，默认是 7
    
    返回:
    dict: 包含输入和输出寄存器的字典
    """

    # 根据前缀生成寄存器名称
    input_registers = [f"{input_type}{i}" for i in range(1, register_count + 1)]
    output_registers = [f"{output_type}{i}" for i in range(1, register_count + 1)]

    return {
        "inputs": input_registers,
        "outputs": output_registers
    }
    
def auto_generate_instructions(num_instructions: int, extension_type: str) -> list:
    """
    自动生成指定数量的指令，并为每条指令生成相应的寄存器。

    参数:
    num_instructions (int): 要生成的指令数量。

    返回:
    list: 生成的指令列表
    """
    instructions = []
    
    if extension_type == ["D"]:  # D 扩展
        for i in range(7):
            inputs = [f"{8 * i}(a0)"] 
            outputs = [f"fa{i+1}"]  
            instructions.append(Instruction("fld", inputs, outputs, "Load"))
            
    elif extension_type == ["V"]:
        inputs = [f"a0"]
        outputs = [f"zero"]
        instructions.append(Instruction("vsetvli", inputs, outputs , "e8", "mf8", "ta", "ma"))
        
    # 遍历生成指令
    for _ in range(num_instructions):
          # 如果扩展类型是 "D"，选择一个 "D" 扩展指令
        if extension_type == ["D"]:  # D 扩展
            name = choice(list(d_instruction_properties.keys()))
            properties = d_instruction_properties[name]
        elif extension_type == ["V"]:
            name = choice(list(v_instruction_properties.keys()))
            properties = v_instruction_properties[name]
        else:
            # 可以添加对其他扩展类型的处理
            print(f"Unsupported extension type: {extension_type}")
            continue  # 如果不支持该扩展类型，跳过

        input_type = properties["inputs_type"]
        output_type = properties["outputs_type"]
        input_count = properties["inputs"]
        output_count = properties["outputs"]
        
        extension = properties["extension"]
        instr_type = properties["instr_type"]
        rounding_mode = properties.get("rounding_mode", None) 

        # 根据 input_type 和 output_type 选择寄存器
        registers = generate_registers_from_types(input_type, output_type)
        
        # 随机选择输入寄存器
        inputs = [choice(registers["inputs"]) for _ in range(input_count)]

        # 随机选择输出寄存器
        outputs = [choice(registers["outputs"]) for _ in range(output_count)]

        instruction = Instruction(name, inputs, outputs, instr_type, rounding_mode)
        instructions.append(instruction)
    if extension_type == ["D"]:  # D 扩展
        for i in range(7):
            inputs = [f"{8 * i}(a0)"]
            outputs = [f"fa{i+1}"]  
            instructions.append(Instruction("fsd", inputs, outputs, "Store"))

    return instructions
