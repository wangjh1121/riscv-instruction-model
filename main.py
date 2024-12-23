from instructions import Instruction
from dependency import InstructionDependency
from generate_code import generate_asm

def main():
    # 定义指令列表，按新格式
    instructions = [
        
        Instruction(name="fmadd.d", inputs=["fa3", "fa2", "fa1"], output="fa4", rounding_mode="0"),
        Instruction(name="fmsub.d", inputs=["fa4", "fa2", "fa1"], output="fa5", rounding_mode="0"),
        Instruction(name="fnmusb.d", inputs=["fa5", "fa3", "fa2"], output="fa5", rounding_mode="0"),
        Instruction(name="fnmadd.d", inputs=["fa4", "fa3", "fa1"], output="fa6", rounding_mode="0"),
        Instruction(name="fadd.d", inputs=["fa3", "fa2"], output="fa4", rounding_mode="0"),
        Instruction(name="feq.d", inputs=["fa4", "fa3"], output="fa5", rounding_mode="0"),
        Instruction(name="fsqrt.d", inputs=["fa5"], output="fa6", rounding_mode="0"),
        Instruction(name="fsub.d", inputs=["fa6", "fa2"], output="fa7", rounding_mode="0"),
        Instruction(name="fld", inputs=["0(a0)"], output="fa1", rounding_mode="011"),
        Instruction(name="fld", inputs=["24(a0)"], output="fa2", rounding_mode="011"),
        Instruction(name="fsign_inject.d", inputs=["fa1", "fa2"], output="fa3", rounding_mode="010"),
    ]

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