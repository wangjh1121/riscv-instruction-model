from instructions import Instruction
from dependency import InstructionDependency
from generate_code import generate_asm
from auto_generate import auto_generate_instructions

def main():
    # 定义指令列表，按新格式
    
    instructions = []
    instructions = auto_generate_instructions(15)

    # 创建依赖关系模型
    dep_model = InstructionDependency()

    # 添加指令到模型中
    for instruction in instructions:
        dep_model.add_instruction(instruction)

    # 自动检测指令之间的依赖关系
    dep_model.detect_dependencies()

    # 获取排序后的指令执行顺序
    ordered_instructions = dep_model.get_ordered_instructions()

    # 生成并输出汇编代码
    asm_code = generate_asm(ordered_instructions)
    print("Generated Assembly Code:")
    print(asm_code)


if __name__ == "__main__":
    main()