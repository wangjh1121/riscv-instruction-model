from instructions import Instruction
from dependency import InstructionDependency
from generate_code import generate_asm
from auto_generate import auto_generate_instructions

def main():
    # 定义指令列表，按新格式
    
    #extensions = ["D", "V", "M", "P"]
    extensions = ["V","D"]
    # 遍历每个扩展生成不同的汇编代码
    for extension in extensions:
        print(f"Generating assembly for extension: {extension}")
        
        # 自动生成指令
        instructions = auto_generate_instructions(20, [extension])

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
        
        # 打印生成的汇编代码
        print(f"Generated Assembly Code for {extension} extension:")
        print(asm_code)
        
        # 写入文件
        file_name = f"{extension.lower()}_extension.s"  # 根据扩展类型动态创建文件名
        with open(file_name, 'w') as f:
            f.write(asm_code)  # 将汇编代码写入文件

        print(f"Assembly code for {extension} extension has been written to {file_name}")


if __name__ == "__main__":
    main()