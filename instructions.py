class Instruction:
    def __init__(self, name, inputs, output, instr_type, rounding_mode=None,
                 vlen=None, elem_type=None, mask=None, tail_policy=None):
        """初始化指令，存储名称、输入、输出和舍入模式（如果有的话）"""
        self.name = name                # 指令名称，如 FADD.d
        self.inputs = inputs            # 输入寄存器列表，例如 ["rs2", "rs1", "rm"]
        self.output = output            # 输出寄存器，通常为 "rd"
        self.instr_type = instr_type
        self.rounding_mode = rounding_mode  # 舍入模式（可选）
        self.vlen = vlen
        self.elem_type = elem_type
        self.mask = mask
        self.tail_policy = tail_policy
        

    def __repr__(self):
        """返回指令的字符串表示形式"""
        # 确保 output 是一个列表，即使它只包含一个元素
        if isinstance(self.output, list):
            output_str = self.output[0] if self.output else ""
        else:
            output_str = self.output

        # 确保 inputs 是一个列表，并且用逗号分隔输出
        inputs_str = ', '.join(self.inputs) if self.inputs else ""
        
        # 动态拼接各个可选字段
        params = []

        if self.vlen:
            params.append(f"{self.vlen}")
        if self.elem_type:
            params.append(f"{self.elem_type}")
        if self.mask:
            params.append(f"{self.mask}")
        if self.tail_policy:
            params.append(f"{self.tail_policy}")
        if self.rounding_mode:
            params.append(f"{self.rounding_mode}")

        # 组合主指令部分和附加的参数
        instruction_str = f"{self.name} {output_str}, {inputs_str}"

        if params:
            instruction_str += ", " + ", ".join(params)

        return instruction_str
        
        # if self.rounding_mode:
        #     return f"{self.name} {output_str}, {inputs_str}, {self.rounding_mode}"
        # if self.
        # else:
        #     return f"{self.name} {output_str}, {inputs_str}"
        
