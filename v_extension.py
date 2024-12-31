# v_extension.py
from instructions import Instruction
# 定义 D 扩展指令集的指令属性映射
v_instruction_properties  = {
    "vadd.d": {"inputs": 2, "outputs": 1, "inputs_type": "v", "outputs_type": "v", "extension": "V_extension", "instr_type": "Arithmetic"},
}


