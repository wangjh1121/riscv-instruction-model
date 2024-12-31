# d_extension.py
from instructions import Instruction
# 定义 D 扩展指令集的指令属性映射
d_instruction_properties  = {
    "fmadd.d": {"inputs": 3, "outputs": 1, "inputs_type": "f", "outputs_type": "f", "extension": "D_extension", "instr_type": "Arithmetic"},
    "fmsub.d": {"inputs": 3, "outputs": 1, "inputs_type": "f", "outputs_type": "f", "extension": "D_extension", "instr_type": "Arithmetic"},
    "fnmsub.d": {"inputs": 3, "outputs": 1, "inputs_type": "f", "outputs_type": "f", "extension": "D_extension", "instr_type": "Arithmetic"},
    "fnmadd.d": {"inputs": 3, "outputs": 1, "inputs_type": "f", "outputs_type": "f", "extension": "D_extension", "instr_type": "Arithmetic"},

    "fadd.d": {"inputs": 2, "outputs": 1, "inputs_type": "f", "outputs_type": "f", "extension": "D_extension", "instr_type": "Arithmetic"},
    "fsub.d": {"inputs": 2, "outputs": 1, "inputs_type": "f", "outputs_type": "f", "extension": "D_extension", "instr_type": "Arithmetic"},
    "fmul.d": {"inputs": 2, "outputs": 1, "inputs_type": "f", "outputs_type": "f", "extension": "D_extension", "instr_type": "Arithmetic"},
    "fdiv.d": {"inputs": 2, "outputs": 1, "inputs_type": "f", "outputs_type": "f", "extension": "D_extension", "instr_type": "Arithmetic"},
    "fsqrt.d": {"inputs": 1, "outputs": 1, "inputs_type": "f", "outputs_type": "f", "extension": "D_extension", "instr_type": "Arithmetic"},

    "fsgnj.d": {"inputs": 2, "outputs": 1, "inputs_type": "f", "outputs_type": "f", "extension": "D_extension", "instr_type": "Sign_Inject"},
    "fsgnjn.d": {"inputs": 2, "outputs": 1, "inputs_type": "f", "outputs_type": "f", "extension": "D_extension", "instr_type": "Sign_Inject"},
    "fsgnjx.d": {"inputs": 2, "outputs": 1, "inputs_type": "f", "outputs_type": "f", "extension": "D_extension", "instr_type": "Sign_Inject"},

    "fmin.d": {"inputs": 2, "outputs": 1, "inputs_type": "f", "outputs_type": "f", "extension": "D_extension", "instr_type": "max_min"},
    "fmax.d": {"inputs": 2, "outputs": 1, "inputs_type": "f", "outputs_type": "f", "extension": "D_extension", "instr_type": "max_min"},
    "feq.d": {"inputs": 2, "outputs": 1, "inputs_type": "f", "outputs_type": "x", "extension": "D_extension", "instr_type": "Comparison"},
    "flt.d": {"inputs": 2, "outputs": 1, "inputs_type": "f", "outputs_type": "x", "extension": "D_extension", "instr_type": "Comparison"},
    "fle.d": {"inputs": 2, "outputs": 1, "inputs_type": "f", "outputs_type": "x", "extension": "D_extension", "instr_type": "Comparison"},

    "fcvt.s.d": {"inputs": 1, "outputs": 1, "inputs_type": "f", "outputs_type": "f", "extension": "D_extension", "instr_type": "Convert"},
    "fcvt.d.s": {"inputs": 1, "outputs": 1, "inputs_type": "f", "outputs_type": "f", "extension": "D_extension", "instr_type": "Convert"},
    "fcvt.w.d": {"inputs": 1, "outputs": 1, "inputs_type": "f", "outputs_type": "x", "extension": "D_extension", "instr_type": "Convert", "rounding_mode": "rtz"},
    "fcvt.wu.d": {"inputs": 1, "outputs": 1, "inputs_type": "f", "outputs_type": "x", "extension": "D_extension", "instr_type": "Convert", "rounding_mode": "rtz"},
    "fcvt.d.w": {"inputs": 1, "outputs": 1, "inputs_type": "x", "outputs_type": "f", "extension": "D_extension", "instr_type": "Convert"},
    "fcvt.d.wu": {"inputs": 1, "outputs": 1, "inputs_type": "x", "outputs_type": "f", "extension": "D_extension", "instr_type": "Convert"},
    "fcvt.l.d": {"inputs": 1, "outputs": 1, "inputs_type": "f", "outputs_type": "x", "extension": "D_extension", "instr_type": "Convert"},
    "fcvt.lu.d": {"inputs": 1, "outputs": 1, "inputs_type": "f", "outputs_type": "x", "extension": "D_extension", "instr_type": "Convert"},
    "fcvt.d.l": {"inputs": 1, "outputs": 1, "inputs_type": "x", "outputs_type": "f", "extension": "D_extension", "instr_type": "Convert"},
    "fcvt.d.lu": {"inputs": 1, "outputs": 1, "inputs_type": "x", "outputs_type": "f", "extension": "D_extension", "instr_type": "Convert"},

    "fmv.x.d": {"inputs": 1, "outputs": 1, "inputs_type": "f", "outputs_type": "x", "extension": "D_extension", "instr_type": "Move"},
    "fmv.d.x": {"inputs": 1, "outputs": 1, "inputs_type": "x", "outputs_type": "f", "extension": "D_extension", "instr_type": "Move"},

    "fclass.d": {"inputs": 1, "outputs": 1, "inputs_type": "f", "outputs_type": "x", "extension": "D_extension", "instr_type": "Categorization"}
}

