import re

# Token types
class TokenType:
    NUMBER = 'NUMBER'
    PLUS = 'PLUS'
    MINUS = 'MINUS'
    MULTIPLY = 'MULTIPLY'
    END = 'END'

# Token structure
class Token:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value

# Function to get the next token from input
def get_next_token(input_str):
    input_str = input_str.lstrip()  # Remove leading whitespace
    if input_str == '':
        return Token(TokenType.END)
    match = re.match(r'^(\d+)', input_str)
    if match:
        number = int(match.group())
        return Token(TokenType.NUMBER, number)
    if input_str[0] == '+':
        return Token(TokenType.PLUS)
    elif input_str[0] == '-':
        return Token(TokenType.MINUS)
    elif input_str[0] == '*':
        return Token(TokenType.MULTIPLY)
    else:
        raise ValueError(f"Invalid character '{input_str[0]}'")

def main():
    input_str = "12 + 34 - 5 * 6"
    while True:
        token = get_next_token(input_str)
        if token.type == TokenType.END:
            print("End of input")
            break
        elif token.type == TokenType.NUMBER:
            print("Number:", token.value)
        elif token.type == TokenType.PLUS:
            print("Operator: +")
        elif token.type == TokenType.MINUS:
            print("Operator: -")
        elif token.type == TokenType.MULTIPLY:
            print("Operator: *")
        input_str = input_str[len(str(token.value)):] if token.type == TokenType.NUMBER else input_str[1:]

if __name__ == '__main__':
    main()
