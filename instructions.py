class Instruction:
    def __init__(self, name, inputs, output, rounding_mode=None):
        """初始化指令，存储名称、输入、输出和舍入模式（如果有的话）"""
        self.name = name                # 指令名称，如 FADD.d
        self.inputs = inputs            # 输入寄存器列表，例如 ["rs2", "rs1", "rm"]
        self.output = output            # 输出寄存器，通常为 "rd"
        self.rounding_mode = rounding_mode  # 舍入模式（可选）

    def __repr__(self):
        """返回指令的字符串表示形式"""
        if self.rounding_mode:
            return f"{self.name} {self.output}, {', '.join(self.inputs)}, {self.rounding_mode}"
        else:
            return f"{self.name} {self.output}, {', '.join(self.inputs)}"