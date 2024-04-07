from bitin.universal import Universal

class Basic:
    def __init__(self):
        self.u = Universal()

    def logical_or(self, input1, input2, gate_type = 'nand'):
        if gate_type == 'nand':
            a_or = self.u.logical_nand(input1, input1)
            b_or = self.u.logical_nand(input2, input2)
            return self.u.logical_nand(a_or, b_or)
        elif gate_type == 'nor':
            a_or = self.u.logical_nor(input1, input2)
            return self.u.logical_nor(a_or, a_or)
        else:
            raise ValueError("Invalid gate type")

    def logical_and(self, input1, input2, gate_type = 'nand'):
        if gate_type == 'nand':
            a_and = self.u.logical_nand(input1, input2)
            return self.u.logical_nand(a_and, a_and)
        elif gate_type == 'nor':
            a_and = self.u.logical_nor(input1, input1)
            b_and = self.u.logical_nor(input2, input2)
            return self.u.logical_nor(a_and, b_and)
        else:
            raise ValueError("Invalid gate type")

    def logical_not(self, input1, gate_type = 'nand'):
        if gate_type == 'nand':
            return self.u.logical_nand(input1, input1)
        elif gate_type == 'nor':
            return self.u.logical_nor(input1, input1)
        else:
            raise ValueError("Invalid gate type")

    def logical_xor(self, input1, input2, gate_type = 'nand'):
        if gate_type == 'nand':
            a_xor = self.u.logical_nand(input1, input2)
            b_xor = self.u.logical_nand(input1, a_xor)
            c_xor = self.u.logical_nand(input2, a_xor)
            return self.u.logical_nand(b_xor, c_xor)
        elif gate_type == 'nor':
            a_xor = self.u.logical_nor(input1, input2)
            b_xor = self.u.logical_nor(input1, a_xor)
            c_xor = self.u.logical_nor(input2, a_xor)
            d_xor = self.u.logical_nor(b_xor, c_xor)
            return self.u.logical_nor(d_xor, d_xor)
        else:
            raise ValueError("Invalid gate type")

    def logical_xnor(self, input1, input2, gate_type = 'nand'):
        if gate_type == 'nand':
            a_xnor = self.u.logical_nand(input1, input2)
            b_xnor = self.u.logical_nand(input1, a_xnor)
            c_xnor = self.u.logical_nand(input2, a_xnor)
            d_xnor = self.u.logical_nand(b_xnor, c_xnor)
            return self.u.logical_nand(d_xnor, d_xnor)
        elif gate_type == 'nor':
            a_xnor = self.u.logical_nor(input1, input2)
            b_xnor = self.u.logical_nor(input1, a_xnor)
            c_xnor = self.u.logical_nor(input2, a_xnor)
            return self.u.logical_nor(b_xnor, c_xnor)
        else:
            raise ValueError("Invalid gate type")

# XOR + NAND = XNOR (change 1) -> 07.04.2024
