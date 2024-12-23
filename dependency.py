from collections import defaultdict
class InstructionDependency:
    def __init__(self):
        """初始化指令依赖关系模型"""
        self.instructions = []            # 存储指令列表
        self.dependencies = defaultdict(list)  # 存储依赖关系
        self.in_degree = defaultdict(int)  # 存储指令的入度，用于拓扑排序

    def add_instruction(self, instruction):
        """向模型中添加指令"""
        self.instructions.append(instruction)
        self.in_degree[instruction] = 0  # 初始入度为 0

    def add_dependency(self, from_instruction, to_instruction):
        """手动添加依赖关系（from_instruction 到 to_instruction）"""
        self.dependencies[from_instruction].append(to_instruction)
        self.in_degree[to_instruction] += 1  # 增加入度

    def detect_dependencies(self):
        """根据寄存器的使用情况自动检测依赖关系"""
        for i, instruction in enumerate(self.instructions):
            for j, other_instruction in enumerate(self.instructions):
                if i != j:  # 避免自己依赖自己
                    # 检查 other_instruction 是否依赖于 instruction 的输出
                    if instruction.output in other_instruction.inputs:
                        self.add_dependency(instruction, other_instruction)

    def get_ordered_instructions(self):
        """获取按依赖关系排序后的指令列表（拓扑排序）"""
        ordered = []
        zero_in_degree = [instr for instr, degree in self.in_degree.items() if degree == 0]

        while zero_in_degree:
            current = zero_in_degree.pop(0)
            ordered.append(current)

            for dependent in self.dependencies.get(current, []):
                self.in_degree[dependent] -= 1
                if self.in_degree[dependent] == 0:
                    zero_in_degree.append(dependent)

        return ordered