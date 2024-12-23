from random import choice
from instructions import Instruction
from typing import List

# 示例寄存器前缀字典
register_prefixes = {
    "D_extension": "fa",  # 浮点扩展寄存器
    "M_extension": "x",   # 整数扩展寄存器
    "F_extension": "fa",  # 浮点扩展寄存器
}

# 定义指令类型与扩展类型的映射
instruction_properties = {
    "fmadd.d": {"inputs": 3, "outputs": 1, "extension": "D_extension"},
    "fmsub.d": {"inputs": 3, "outputs": 1, "extension": "D_extension"},
    "fadd.d": {"inputs": 2, "outputs": 1, "extension": "D_extension"},
    "fsub.d": {"inputs": 2, "outputs": 1, "extension": "D_extension"},
    "feq.d": {"inputs": 2, "outputs": 1, "extension": "D_extension"},
    "fsqrt.d": {"inputs": 1, "outputs": 1, "extension": "D_extension"},
    #"fld": {"inputs": 1, "outputs": 1, "extension": "M_extension"},
    "fnmadd.d": {"inputs": 3, "outputs": 1, "extension": "F_extension"},
    #"add": {"inputs": 2, "outputs": 1, "extension": "M_extension"},
    #"mul": {"inputs": 2, "outputs": 1, "extension": "M_extension"},
    #"fld": {"inputs": 1, "outputs": 1, "extension": "D_extension"}
}

def generate_register_pools(register_prefixes: dict, register_count: int = 7) -> dict:
    """
    根据给定的寄存器前缀和寄存器数量，生成不同类型的寄存器池。
    
    参数:
    register_prefixes (dict): 一个字典，其中包含扩展类型与其对应的寄存器前缀。
    register_count (int): 每个扩展类型的寄存器数量，默认值为 7。
    
    返回:
    dict: 生成的寄存器池字典，包含每个扩展类型的输入和输出寄存器。
    """
    # 初始化 REGISTER_POOLS 字典
    REGISTER_POOLS = {}

    # 使用 for 循环来动态填充寄存器池
    for extension_type, prefix in register_prefixes.items():
        # 填充 inputs 和 outputs 列表
        inputs = [f"{prefix}{i}" for i in range(1, register_count + 1)]  # 根据寄存器数量生成寄存器名
        outputs = inputs  # 假设 outputs 与 inputs 相同

        # 更新 REGISTER_POOLS
        REGISTER_POOLS[extension_type] = {
            "inputs": inputs,
            "outputs": outputs
        }

    return REGISTER_POOLS

def auto_generate_instructions(num_instructions: int) -> List[Instruction]:
    """
    自动生成指定数量的指令，每个指令的名称、输入、输出寄存器随机生成。
    
    参数:
    num_instructions (int): 要生成的指令数量。
    
    返回:
    List[Instruction]: 生成的指令列表。
    """
    instructions = []
    register_pools = generate_register_pools(register_prefixes)  # 调用生成寄存器池函数
    
    # 随机生成指令
    for _ in range(num_instructions):
        name = choice(list(instruction_properties.keys()))
        input_count = instruction_properties[name]["inputs"]  # 根据指令名称选择输入数量
        output_count = instruction_properties[name]["outputs"]  # 根据指令名称选择输出数量
        extension = instruction_properties[name]["extension"]  # 获取扩展类型

        # 获取对应扩展类型的寄存器池
        input_registers = register_pools[extension]["inputs"]  # 使用局部变量 register_pools
        output_registers = register_pools[extension]["outputs"]

        # 随机选择输入寄存器
        inputs = [choice(input_registers) for _ in range(input_count)]

        # 随机选择输出寄存器
        outputs = [choice(output_registers) for _ in range(output_count)]

        # 创建指令并添加到列表
        instruction = Instruction(name, inputs, outputs)
        instructions.append(instruction)
    
    return instructions
