class ThreeAddressGenerator:
    def _init_(self):
        self.temp_count = 0
        self.code = []

    def generate_code(self, expression):
        self.temp_count = 0
        self.code = []
        self.parse_expression(expression)
        return self.code

    def generate_temp(self):
        temp_var = f"t{self.temp_count}"
        self.temp_count += 1
        return temp_var

    def parse_expression(self, expression):
        tokens = expression.split("=")
        if len(tokens) != 2:
            raise ValueError(
                "Invalid expression format. Expected 'variable = expression'"
            )
        result_variable = tokens[0].strip()
        expression = tokens[1].strip()
        if not expression:
            raise ValueError("Expression cannot be empty")
        temp_stack = []
        op_stack = []
        precedence = {"+": 1, "-": 1, "*": 2, "/": 2}
        for char in expression:
            if char == "(":
                op_stack.append(char)
            elif char == ")":
                while op_stack and op_stack[-1] != "(":
                    operator = op_stack.pop()
                    right_operand = temp_stack.pop()
                    left_operand = temp_stack.pop()
                    result_temp = self.generate_temp()
                    self.code.append(
                        f"{result_temp} = {left_operand} {operator} {right_operand}"
                    )
                    temp_stack.append(result_temp)
                op_stack.pop()  # Discard '('
            elif char in ("+", "-", "*", "/"):
                while op_stack and precedence.get(op_stack[-1], 0) >= precedence[char]:
                    operator = op_stack.pop()
                    right_operand = temp_stack.pop()
                    left_operand = temp_stack.pop()
                    result_temp = self.generate_temp()
                    self.code.append(
                        f"{result_temp} = {left_operand} {operator} {right_operand}"
                    )
                    temp_stack.append(result_temp)
                op_stack.append(char)
            else:
                temp_stack.append(char)
        while op_stack:
            operator = op_stack.pop()
            right_operand = temp_stack.pop()
            left_operand = temp_stack.pop()
            result_temp = self.generate_temp()
            self.code.append(
                f"{result_temp} = {left_operand} {operator} {right_operand}"
            )
            temp_stack.append(result_temp)
        self.code.append(f"{result_variable} = {temp_stack.pop()}")


def main():
    generator = ThreeAddressGenerator()
    expression = "a=(b+c)*((d-e)/f)"  # Example expression
    code = generator.generate_code(expression)
    print("Three Address Code:")
    for instruction in code:
        print(instruction)
    print(f"Result: {expression}")


if __name__ == "__main__":
    main()
