
from typing import List  # Add this import
from instructions import Instruction
def generate_asm(instructions: List[Instruction]) -> str:
    """生成汇编代码"""
    asm_code = ".global _start\n_start:\n"
    asm_code += "    addi sp, sp, -64\n"  # 栈空间分配
    # 保存寄存器 (可选) 
    asm_code += "    sd ra, 56(sp)\n"
    asm_code += "    sd s0, 48(sp)\n"
    # 加载数据到寄存器
    asm_code += "    la a0, data\n"
    # 初始化 a1 寄存器 (假设初始化为 10)
    asm_code += "    li a1, 10\n"  
    
    for i, instr in enumerate(instructions):
        asm_code += f"    {instr}\n"
        # if instr.instr_type == "Comparison":
        #     jump_label = f".LBB_{i}_2"
        #     asm_code += f"    bnez {instr.output}, {jump_label}\n"  # 跳转指令
        
    asm_code += "    ld ra, 56(sp)\n"
    asm_code += "    ld s0, 48(sp)\n"
    asm_code += "    addi sp, sp, 64\n"
    asm_code += "    li a7, 93\n"
    asm_code += "    li a0, 0\n"
    asm_code += "    ecall\n"
    
    # 单独处理 feq.d 跳转逻辑
    # for i, instr in enumerate(instructions):
    #     if instr.instr_type == "Comparison":
    #         jump_label = f".LBB_{i}_2"
            
    #         # 错误处理代码（跳转标签后执行的代码）
    #         asm_code += f"{jump_label}:\n"
    #         asm_code += "    addi sp, sp, -16\n"  # 分配栈空间
    #         asm_code += "    sw ra, 12(sp)\n"     # 保存 ra 寄存器
    #         asm_code += "    call abort\n\n"        # 调用 abort 函数
            
    asm_code += ".data\n"
    asm_code += ".align 8\n"
    asm_code += "data: .double 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0\n\n"
   
    asm_code += ".global main\n"
    asm_code += "main:\n"
    asm_code += "    j _start"
    return asm_code
